import logging
import typing as t

from pydantic import AliasPath, BaseModel, Field, model_validator

from qqqr.message import select_captcha_input
from qqqr.utils.jsjson import json_loads
from qqqr.utils.net import ClientAdapter

from .._model import ClickCfg, PrehandleResp, Sprite
from ..capsess import BaseTcaptchaSession
from ..img_utils import *

log = logging.getLogger(__name__)
_TyHook = type(select_captcha_input)


class SelectBgElemCfg(Sprite):
    click_cfg: ClickCfg
    img_url: str


class SelectRegion(BaseModel):
    id: int
    left: int = Field(validation_alias=AliasPath("range", 0))
    top: int = Field(validation_alias=AliasPath("range", 1))
    right: int = Field(validation_alias=AliasPath("range", 2))
    bottom: int = Field(validation_alias=AliasPath("range", 3))


class SelectJsonPayload(BaseModel):
    select_region_list: t.List[SelectRegion]
    prompt_id: int
    picture_ids: t.List[int]

    def __len__(self):
        return len(self.picture_ids)


class SelectCaptchaDisplay(BaseModel):
    instruction: str
    bg: SelectBgElemCfg = Field(alias="bg_elem_cfg")
    verify_trigger_cfg: dict
    color_scheme: str  # pydantic_extra_types.color
    json_payload: SelectJsonPayload

    @model_validator(mode="before")
    def parse_json(cls, v: dict):
        v["json_payload"] = json_loads(v["json_payload"])
        return v


class SelectCaptchaSession(BaseTcaptchaSession):
    select_captcha_input: _TyHook

    def __init__(self, prehandle: PrehandleResp) -> None:
        super().__init__(prehandle)

    def parse_captcha_data(self):
        super().parse_captcha_data()
        self.render = SelectCaptchaDisplay.model_validate(self.conf.render)
        if self.render.bg.click_cfg.data_type:
            self.data_type = self.render.bg.click_cfg.data_type[0]

    async def get_captcha_problem(self, client: ClientAdapter):
        async with client.get(self._cdn_join(self.render.bg.img_url)) as r:
            img = frombytes(await r.content.read())

        self.cdn_imgs = [
            tobytes(img[r.top : r.bottom, r.left : r.right])
            for r in self.render.json_payload.select_region_list
        ]

    async def solve_captcha(self) -> str:
        if not self.select_captcha_input.has_impl:
            log.warning("select_captcha_input has no impls.")
            return ""

        i = await self.select_captcha_input(self.render.instruction, tuple(self.cdn_imgs))
        if 0 <= i < len(self.render.json_payload):
            return str(self.render.json_payload.picture_ids[i])

        log.warning(f"Invalid answer {i}")
        return ""
