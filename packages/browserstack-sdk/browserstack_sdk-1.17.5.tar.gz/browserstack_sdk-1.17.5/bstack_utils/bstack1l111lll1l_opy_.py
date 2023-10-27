# coding: UTF-8
import sys
bstack1l1l11_opy_ = sys.version_info [0] == 2
bstack1111lll_opy_ = 2048
bstack11_opy_ = 7
def bstack111_opy_ (bstack11111l1_opy_):
    global bstack1ll111l_opy_
    bstack1ll1l1l_opy_ = ord (bstack11111l1_opy_ [-1])
    bstack1l11111_opy_ = bstack11111l1_opy_ [:-1]
    bstack1111111_opy_ = bstack1ll1l1l_opy_ % len (bstack1l11111_opy_)
    bstack1ll1ll1_opy_ = bstack1l11111_opy_ [:bstack1111111_opy_] + bstack1l11111_opy_ [bstack1111111_opy_:]
    if bstack1l1l11_opy_:
        bstack1l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack1111lll_opy_ - (bstack1l11_opy_ + bstack1ll1l1l_opy_) % bstack11_opy_) for bstack1l11_opy_, char in enumerate (bstack1ll1ll1_opy_)])
    else:
        bstack1l11l_opy_ = str () .join ([chr (ord (char) - bstack1111lll_opy_ - (bstack1l11_opy_ + bstack1ll1l1l_opy_) % bstack11_opy_) for bstack1l11_opy_, char in enumerate (bstack1ll1ll1_opy_)])
    return eval (bstack1l11l_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1lllll111_opy_, bstack1l1ll1ll1l_opy_
from bstack_utils.bstack1l1l111ll1_opy_ import bstack1l1l111111_opy_
class bstack1l11l11111_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l111l111l_opy_=None, framework=None, tags=[], scope=[], bstack1l111l1l1l_opy_=None, bstack1l11l111ll_opy_=True, bstack1l11l11l11_opy_=None, bstack1111lll1_opy_=None, result=None, duration=None, meta={}):
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1l11l111ll_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l111l111l_opy_ = bstack1l111l111l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1l111l1l1l_opy_ = bstack1l111l1l1l_opy_
        self.bstack1l11l11l11_opy_ = bstack1l11l11l11_opy_
        self.bstack1111lll1_opy_ = bstack1111lll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack1l111ll111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1l111lllll_opy_(self):
        bstack1l111l1ll1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᄬ"): bstack1l111l1ll1_opy_,
            bstack111_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᄭ"): bstack1l111l1ll1_opy_,
            bstack111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᄮ"): bstack1l111l1ll1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᄯ") + key)
            setattr(self, key, val)
    def bstack1l111l1l11_opy_(self):
        return {
            bstack111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᄰ"): self.name,
            bstack111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᄱ"): {
                bstack111_opy_ (u"࠭࡬ࡢࡰࡪࠫᄲ"): bstack111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᄳ"),
                bstack111_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᄴ"): self.code
            },
            bstack111_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᄵ"): self.scope,
            bstack111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᄶ"): self.tags,
            bstack111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᄷ"): self.framework,
            bstack111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᄸ"): self.bstack1l111l111l_opy_
        }
    def bstack1l111l11ll_opy_(self):
        return {
         bstack111_opy_ (u"࠭࡭ࡦࡶࡤࠫᄹ"): self.meta
        }
    def bstack1l111l11l1_opy_(self):
        return {
            bstack111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᄺ"): {
                bstack111_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᄻ"): self.bstack1l111l1l1l_opy_
            }
        }
    def bstack1l11l11l1l_opy_(self, bstack1l111ll1ll_opy_, details):
        step = next(filter(lambda st: st[bstack111_opy_ (u"ࠩ࡬ࡨࠬᄼ")] == bstack1l111ll1ll_opy_, self.meta[bstack111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᄽ")]), None)
        step.update(details)
    def bstack1l111llll1_opy_(self, bstack1l111ll1ll_opy_):
        step = next(filter(lambda st: st[bstack111_opy_ (u"ࠫ࡮ࡪࠧᄾ")] == bstack1l111ll1ll_opy_, self.meta[bstack111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᄿ")]), None)
        step.update({
            bstack111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᅀ"): bstack1lllll111_opy_()
        })
    def bstack1l11l111l1_opy_(self, bstack1l111ll1ll_opy_, result):
        bstack1l11l11l11_opy_ = bstack1lllll111_opy_()
        step = next(filter(lambda st: st[bstack111_opy_ (u"ࠧࡪࡦࠪᅁ")] == bstack1l111ll1ll_opy_, self.meta[bstack111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᅂ")]), None)
        step.update({
            bstack111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᅃ"): bstack1l11l11l11_opy_,
            bstack111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᅄ"): bstack1l1ll1ll1l_opy_(step[bstack111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᅅ")], bstack1l11l11l11_opy_),
            bstack111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᅆ"): result.result,
            bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᅇ"): str(result.exception) if result.exception else None
        })
    def bstack1l111lll11_opy_(self):
        return {
            bstack111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᅈ"): self.bstack1l111ll111_opy_(),
            **self.bstack1l111l1l11_opy_(),
            **self.bstack1l111lllll_opy_(),
            **self.bstack1l111l11ll_opy_()
        }
    def bstack1l11l11ll1_opy_(self):
        data = {
            bstack111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᅉ"): self.bstack1l11l11l11_opy_,
            bstack111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᅊ"): self.duration,
            bstack111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᅋ"): self.result.result
        }
        if data[bstack111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᅌ")] == bstack111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᅍ"):
            data[bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᅎ")] = self.result.bstack1ll1111111_opy_()
            data[bstack111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᅏ")] = [{bstack111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᅐ"): self.result.bstack1l1ll1lll1_opy_()}]
        return data
    def bstack1l1111llll_opy_(self):
        return {
            bstack111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᅑ"): self.bstack1l111ll111_opy_(),
            **self.bstack1l111l1l11_opy_(),
            **self.bstack1l111lllll_opy_(),
            **self.bstack1l11l11ll1_opy_(),
            **self.bstack1l111l11ll_opy_()
        }
    def bstack1l111ll1l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if event == bstack111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᅒ"):
            return self.bstack1l111lll11_opy_()
        elif event == bstack111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᅓ"):
            return self.bstack1l1111llll_opy_()
    def bstack1l111ll11l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l11l11l11_opy_ = time if time else bstack1lllll111_opy_()
        self.duration = duration if duration else bstack1l1ll1ll1l_opy_(self.bstack1l111l111l_opy_, self.bstack1l11l11l11_opy_)
        if result:
            self.result = result
class bstack1l11l1111l_opy_(bstack1l11l11111_opy_):
    def __init__(self, *args, hooks=[], **kwargs):
        self.hooks = hooks
        super().__init__(*args, **kwargs, bstack1111lll1_opy_=bstack111_opy_ (u"ࠬࡺࡥࡴࡶࠪᅔ"))
    @classmethod
    def bstack1l111l1lll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111_opy_ (u"࠭ࡩࡥࠩᅕ"): id(step),
                bstack111_opy_ (u"ࠧࡵࡧࡻࡸࠬᅖ"): step.name,
                bstack111_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩᅗ"): step.keyword,
            })
        return bstack1l11l1111l_opy_(
            **kwargs,
            meta={
                bstack111_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪᅘ"): {
                    bstack111_opy_ (u"ࠪࡲࡦࡳࡥࠨᅙ"): feature.name,
                    bstack111_opy_ (u"ࠫࡵࡧࡴࡩࠩᅚ"): feature.filename,
                    bstack111_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪᅛ"): feature.description
                },
                bstack111_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨᅜ"): {
                    bstack111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᅝ"): scenario.name
                },
                bstack111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᅞ"): steps,
                bstack111_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫᅟ"): bstack1l1l111111_opy_(test)
            }
        )
    def bstack1l111l1111_opy_(self):
        return {
            bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᅠ"): self.hooks
        }
    def bstack1l1111llll_opy_(self):
        return {
            **super().bstack1l1111llll_opy_(),
            **self.bstack1l111l1111_opy_()
        }
    def bstack1l111ll11l_opy_(self):
        return bstack111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᅡ")