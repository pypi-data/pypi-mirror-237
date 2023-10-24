import asyncio
import base64
import json
import logging
import re
from contextlib import suppress
from hashlib import md5
from ipaddress import IPv4Address
from random import random
from time import time
from typing import List, Tuple

from chaosvm import prepare
from chaosvm.proxy.dom import TDC
from pydantic import ValidationError
from tenacity import retry, retry_if_exception_type, stop_after_attempt
from yarl import URL

from ...utils.iter import first
from ...utils.net import ClientAdapter
from .._model import PrehandleResp, SlideCaptchaDisplay, VerifyResp
from .jigsaw import Jigsaw, imitate_drag

PREHANDLE_URL = "https://t.captcha.qq.com/cap_union_prehandle"
SHOW_NEW_URL = "https://t.captcha.qq.com/cap_union_new_show"
VERIFY_URL = "https://t.captcha.qq.com/cap_union_new_verify"

time_ms = lambda: int(1e3 * time())
"""+new Date"""
rnd6 = lambda: str(random())[2:8]
log = logging.getLogger(__name__)


def hex_add(h: str, o: int):
    if h.endswith("#"):
        return h + str(o)
    if not h:
        return o
    return hex(int(h, 16) + o)[2:]


class TcaptchaSession:
    def __init__(
        self,
        prehandle: PrehandleResp,
    ) -> None:
        super().__init__()
        self.prehandle = prehandle
        self.set_captcha()

    def set_captcha(self):
        self.conf = self.prehandle.captcha
        self.ip = self.prehandle.uip
        if not isinstance(self.conf.render, SlideCaptchaDisplay):
            raise NotImplementedError(self.conf.render)
        self.cdn_urls = (
            self._cdn(self.conf.render.bg.img_url),
            self._cdn(self.conf.render.sprite_url),
        )
        self.cdn_imgs: List[bytes] = []
        self.piece_sprite = first(self.conf.render.sprites, lambda s: s.move_cfg)

    def set_drag_track(self, xs: List[int], ys: List[int]):
        self.mouse_track = list(zip(xs, ys))

    def solve_workload(self, *, timeout: float = 30.0):
        """
        The solve_workload function solves the workload from Tcaptcha:
        It solves md5(:obj:`PowCfg.prefix` + str(?)) == :obj:`PowCfg.md5`.
        The result and the calculating duration will be saved into this session.

        :param timeout: Calculating timeout, default as 30 seconds.
        :return: None
        """

        pow_cfg = self.conf.common.pow_cfg
        nonce = str(pow_cfg.prefix).encode()
        target = pow_cfg.md5.lower()

        start = time()
        cnt = 0

        while time() - start < timeout:
            if md5(nonce + str(cnt).encode()).hexdigest() == target:
                break
            cnt += 1

        self.pow_ans = cnt
        # on some environment this time is too low... add a limit
        self.duration = max(int((time() - start) * 1e3), 50)

    def set_captcha_answer(self, left: int, top: int):
        self.jig_ans = left, top

    def set_js_env(self, tdc: TDC):
        self.tdc = tdc

    def _cdn(self, rel_path: str) -> URL:
        return URL("https://t.captcha.qq.com").with_path(rel_path, encoded=True)

    def tdx_js_url(self):
        assert self.conf
        return URL("https://t.captcha.qq.com").with_path(self.conf.common.tdc_path, encoded=True)

    def vmslide_js_url(self):
        raise NotImplementedError


class Captcha:
    # (c_login_2.js)showNewVC-->prehandle
    # prehandle(recall)--call tcapcha-frame.*.js-->new_show
    # new_show(html)--js in html->loadImg(url)
    def __init__(self, client: ClientAdapter, appid: int, sid: str, xlogin_url: str):
        """
        :param client: network client
        :param appid: Specify the appid of the application
        :param sid: Session id got from :meth:`UpWebLogin.new`
        :param xlogin_url: :obj:`LoginBase.xlogin_url`
        """

        super().__init__()
        self.client = client
        self.appid = appid
        self.sid = sid
        self.xlogin_url = xlogin_url
        self.client.referer = "https://xui.ptlogin2.qq.com/"

    @property
    def base64_ua(self):
        """
        The base64_ua function encodes the User-Agent header in base64.

        :return: A string containing the base64 encoded user agent
        """

        return base64.b64encode(self.client.headers["User-Agent"].encode()).decode()

    async def new(self):
        """``prehandle``. Call this method to generate a new verify session.

        :raises NotImplementedError: if not a slide captcha.
        :return: a tcaptcha session
        """
        CALLBACK = "_aq_596882"
        const = {
            "protocol": "https",
            "noheader": 1,
            "showtype": "embed",
            "enableDarkMode": 0,
            "grayscale": 1,
            "clientype": 2,
            "cap_cd": "",
            "uid": "",
            "wxLang": "",
            "lang": "zh-CN",
            "sess": "",
            "fb": 1,
            "aged": 0,
            "enableAged": 0,
            "elder_captcha": 0,
            "login_appid": "",
            "wb": 2,
        }
        data = {
            "aid": self.appid,
            "accver": 1,
            "ua": self.base64_ua,
            "sid": self.sid,
            "entry_url": self.xlogin_url,
            # 'js': '/tcaptcha-frame.a75be429.js'
            "subsid": 1,
            "callback": CALLBACK,
        }
        data.update(const)

        @retry(stop=stop_after_attempt(2), retry=retry_if_exception_type(ValidationError))
        async def retry_closure():
            async with self.client.get(PREHANDLE_URL, params=data) as r:
                r.raise_for_status()
                m = re.search(CALLBACK + r"\((\{.*\})\)", await r.text())

            assert m
            return PrehandleResp.model_validate_json(m.group(1))

        return TcaptchaSession(await retry_closure())

    async def iframe(self):
        """call this right after calling :meth:`.prehandle`"""
        async with self.client.get("https://t.captcha.qq.com/template/drag_ele.html") as r:
            return r.text

    prehandle = new
    """alias of :meth:`.new`"""

    async def get_captcha_problem(self, sess: TcaptchaSession):
        """
        The get_captcha_problem function is a coroutine that accepts a TcaptchaSession object as an argument.
        It then uses the session to make an HTTP GET request to the captcha images (the problem). The images
        will be stored in the given session.

        :param sess: captcha session
        :return: None
        """

        async def r(url) -> bytes:
            async with self.client.get(url) as r:
                r.raise_for_status()
                return await r.content.read()

        sess.cdn_imgs = list(await asyncio.gather(*(r(i) for i in sess.cdn_urls)))

    def solve_captcha(self, sess: TcaptchaSession):
        """
        The solve_captcha function solves the captcha problem. It assumes that :obj:`TcaptchaSession.cdn_imgs`
        is already initialized, so call :meth:`.get_captcha_problem` firstly.

        It then solve the captcha as that in :class:`.Jigsaw`. The answer is saved into `sess`.

        This function will also call :meth:`TDC.set_data` to imitate human behavior when solving captcha.

        :param sess: Store the information of the current session
        :return: None
        """

        assert sess.cdn_imgs

        get_slice = lambda i: slice(
            sess.piece_sprite.sprite_pos[i],
            sess.piece_sprite.sprite_pos[i] + sess.piece_sprite.size_2d[i],
        )
        piece_pos = get_slice(0), get_slice(1)

        jig = Jigsaw(*sess.cdn_imgs, piece_pos=piece_pos, top=sess.piece_sprite.init_pos[1])
        # BUG: +1 to ensure left > init_pos[0], otherwise it's >=.
        # However if left == init_pos[0] + 1, it is certainly a wrong result.
        left = jig.solve(sess.piece_sprite.init_pos[0] + 1)
        sess.set_captcha_answer(left, jig.top)

        xs, ys = imitate_drag(sess.piece_sprite.init_pos[0], left, jig.top)
        sess.set_drag_track(xs, ys)

    async def get_tdc(self, sess: TcaptchaSession):
        """
        The get_tdc function is a coroutine that sets an instance of the :class:`TDC` class to `sess`.

        :param sess: captcha session
        :return: None
        """
        async with self.client.get(sess.tdx_js_url()) as r:
            r.raise_for_status()
            tdc = prepare(
                await r.text(),
                ip=sess.ip,
                ua=self.client.headers["User-Agent"],
                mouse_track=sess.mouse_track,
            )

        sess.set_js_env(tdc)

    async def verify(self):
        """
        :raise NotImplementedError: from :meth:`.new`.
        """
        sess = await self.new()

        await self.get_captcha_problem(sess)
        sess.solve_workload()
        self.solve_captcha(sess)
        await self.get_tdc(sess)

        assert sess.piece_sprite.move_cfg
        assert sess.piece_sprite.move_cfg.data_type

        collect = str(sess.tdc.getData(None, True))  # BUG: maybe a String(), convert to str

        ans = dict(
            elem_id=1,
            type=sess.piece_sprite.move_cfg.data_type[0],
            data="{0},{1}".format(*sess.jig_ans),
        )
        data = {
            "collect": collect,
            "tlg": len(collect),
            "eks": sess.tdc.getInfo()["info"],
            "sess": sess.prehandle.sess,
            "ans": json.dumps(ans),
            "pow_answer": hex_add(sess.conf.common.pow_cfg.prefix, sess.pow_ans),
            "pow_calc_time": sess.duration,
        }
        log.debug(f"verify post data: {data}")

        async with self.client.post(VERIFY_URL, data=data) as r:
            r = VerifyResp.model_validate_json(await r.text())

        return r
