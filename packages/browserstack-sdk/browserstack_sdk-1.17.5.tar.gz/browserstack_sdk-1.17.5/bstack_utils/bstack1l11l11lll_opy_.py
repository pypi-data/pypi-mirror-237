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
import json
import os
from bstack_utils.helper import bstack1l1lll1l1l_opy_, bstack1ll1llll11_opy_, bstack1111ll1l_opy_, \
    bstack1ll1111lll_opy_
def bstack1llll1l111_opy_(bstack1l11l1l11l_opy_):
    for driver in bstack1l11l1l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1llllll_opy_(type, name, status, reason, bstack1111lll11_opy_, bstack1l11ll1l1_opy_):
    bstack11111111_opy_ = {
        bstack111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧᄉ"): type,
        bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᄊ"): {}
    }
    if type == bstack111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫᄋ"):
        bstack11111111_opy_[bstack111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᄌ")][bstack111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᄍ")] = bstack1111lll11_opy_
        bstack11111111_opy_[bstack111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᄎ")][bstack111_opy_ (u"࠭ࡤࡢࡶࡤࠫᄏ")] = json.dumps(str(bstack1l11ll1l1_opy_))
    if type == bstack111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᄐ"):
        bstack11111111_opy_[bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᄑ")][bstack111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᄒ")] = name
    if type == bstack111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᄓ"):
        bstack11111111_opy_[bstack111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᄔ")][bstack111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᄕ")] = status
        if status == bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᄖ") and str(reason) != bstack111_opy_ (u"ࠢࠣᄗ"):
            bstack11111111_opy_[bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᄘ")][bstack111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᄙ")] = json.dumps(str(reason))
    bstack11l11111l_opy_ = bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᄚ").format(json.dumps(bstack11111111_opy_))
    return bstack11l11111l_opy_
def bstack1l1l1l11_opy_(url, config, logger, bstack111ll1l1_opy_=False):
    hostname = bstack1ll1llll11_opy_(url)
    is_private = bstack1111ll1l_opy_(hostname)
    try:
        if is_private or bstack111ll1l1_opy_:
            file_path = bstack1l1lll1l1l_opy_(bstack111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᄛ"), bstack111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᄜ"), logger)
            if os.environ.get(bstack111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᄝ")) and eval(
                    os.environ.get(bstack111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᄞ"))):
                return
            if (bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᄟ") in config and not config[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᄠ")]):
                os.environ[bstack111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᄡ")] = str(True)
                bstack1l11l1l111_opy_ = {bstack111_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ᄢ"): hostname}
                bstack1ll1111lll_opy_(bstack111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᄣ"), bstack111_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫᄤ"), bstack1l11l1l111_opy_, logger)
    except Exception as e:
        pass
def bstack1llll11lll_opy_(caps, bstack1l11l1l1l1_opy_):
    if bstack111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᄥ") in caps:
        caps[bstack111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᄦ")][bstack111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᄧ")] = True
        if bstack1l11l1l1l1_opy_:
            caps[bstack111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᄨ")][bstack111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᄩ")] = bstack1l11l1l1l1_opy_
    else:
        caps[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪᄪ")] = True
        if bstack1l11l1l1l1_opy_:
            caps[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᄫ")] = bstack1l11l1l1l1_opy_