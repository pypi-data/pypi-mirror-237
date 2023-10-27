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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack1l1ll1ll11_opy_, bstack11l1l1ll_opy_, get_host_info, bstack1l1ll1l1ll_opy_, bstack1l1ll1l11l_opy_, bstack1l1llll1ll_opy_, \
    bstack1l1ll11l11_opy_, bstack1l1lll11ll_opy_, bstack1l1l1111l_opy_, bstack1l1lll1ll1_opy_, bstack1l1lll1111_opy_, bstack1ll1111ll1_opy_
from bstack_utils.bstack1l11lll11l_opy_ import bstack1l11ll11l1_opy_
from bstack_utils.bstack1l111lll1l_opy_ import bstack1l11l11111_opy_
bstack11lll1lll1_opy_ = [
    bstack111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᅢ"), bstack111_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪᅣ"), bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᅤ"), bstack111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᅥ"),
    bstack111_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᅦ"), bstack111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᅧ"), bstack111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᅨ")
]
bstack11lllllll1_opy_ = bstack111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᅩ")
logger = logging.getLogger(__name__)
class bstack1111llll_opy_:
    bstack1l11lll11l_opy_ = None
    bs_config = None
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def launch(cls, bs_config, bstack11llll1111_opy_):
        cls.bs_config = bs_config
        if not cls.bstack1l111111l1_opy_():
            return
        cls.bstack11llllll11_opy_()
        bstack1l1111l1ll_opy_ = bstack1l1ll1l1ll_opy_(bs_config)
        bstack1l1111lll1_opy_ = bstack1l1ll1l11l_opy_(bs_config)
        data = {
            bstack111_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭ᅪ"): bstack111_opy_ (u"ࠧ࡫ࡵࡲࡲࠬᅫ"),
            bstack111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧᅬ"): bs_config.get(bstack111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᅭ"), bstack111_opy_ (u"ࠪࠫᅮ")),
            bstack111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᅯ"): bs_config.get(bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᅰ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᅱ"): bs_config.get(bstack111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᅲ")),
            bstack111_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ᅳ"): bs_config.get(bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᅴ"), bstack111_opy_ (u"ࠪࠫᅵ")),
            bstack111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡢࡸ࡮ࡳࡥࠨᅶ"): datetime.datetime.now().isoformat(),
            bstack111_opy_ (u"ࠬࡺࡡࡨࡵࠪᅷ"): bstack1l1llll1ll_opy_(bs_config),
            bstack111_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩᅸ"): get_host_info(),
            bstack111_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨᅹ"): bstack11l1l1ll_opy_(),
            bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᅺ"): os.environ.get(bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᅻ")),
            bstack111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨᅼ"): os.environ.get(bstack111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩᅽ"), False),
            bstack111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧᅾ"): bstack1l1ll1ll11_opy_(),
            bstack111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᅿ"): {
                bstack111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧᆀ"): bstack11llll1111_opy_.get(bstack111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩᆁ"), bstack111_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩᆂ")),
                bstack111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᆃ"): bstack11llll1111_opy_.get(bstack111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᆄ")),
                bstack111_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᆅ"): bstack11llll1111_opy_.get(bstack111_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫᆆ"))
            }
        }
        config = {
            bstack111_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᆇ"): (bstack1l1111l1ll_opy_, bstack1l1111lll1_opy_),
            bstack111_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᆈ"): cls.default_headers()
        }
        response = bstack1l1l1111l_opy_(bstack111_opy_ (u"ࠩࡓࡓࡘ࡚ࠧᆉ"), cls.request_url(bstack111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵࠪᆊ")), data, config)
        if response.status_code != 200:
            os.environ[bstack111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᆋ")] = bstack111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᆌ")
            os.environ[bstack111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᆍ")] = bstack111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᆎ")
            os.environ[bstack111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᆏ")] = bstack111_opy_ (u"ࠤࡱࡹࡱࡲࠢᆐ")
            os.environ[bstack111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᆑ")] = bstack111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᆒ")
            bstack11lllll1ll_opy_ = response.json()
            if bstack11lllll1ll_opy_ and bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᆓ")]:
                error_message = bstack11lllll1ll_opy_[bstack111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᆔ")]
                if bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࡚ࡹࡱࡧࠪᆕ")] == bstack111_opy_ (u"ࠨࡇࡕࡖࡔࡘ࡟ࡊࡐ࡙ࡅࡑࡏࡄࡠࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘ࠭ᆖ"):
                    logger.error(error_message)
                elif bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬᆗ")] == bstack111_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠩᆘ"):
                    logger.info(error_message)
                elif bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠫࡪࡸࡲࡰࡴࡗࡽࡵ࡫ࠧᆙ")] == bstack111_opy_ (u"ࠬࡋࡒࡓࡑࡕࡣࡘࡊࡋࡠࡆࡈࡔࡗࡋࡃࡂࡖࡈࡈࠬᆚ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣᆛ"))
            return [None, None, None]
        logger.debug(bstack111_opy_ (u"ࠧࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫᆜ"))
        os.environ[bstack111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧᆝ")] = bstack111_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᆞ")
        bstack11lllll1ll_opy_ = response.json()
        if bstack11lllll1ll_opy_.get(bstack111_opy_ (u"ࠪ࡮ࡼࡺࠧᆟ")):
            os.environ[bstack111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᆠ")] = bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠬࡰࡷࡵࠩᆡ")]
            os.environ[bstack111_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪᆢ")] = json.dumps({
                bstack111_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩᆣ"): bstack1l1111l1ll_opy_,
                bstack111_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪᆤ"): bstack1l1111lll1_opy_
            })
        if bstack11lllll1ll_opy_.get(bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᆥ")):
            os.environ[bstack111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᆦ")] = bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᆧ")]
        if bstack11lllll1ll_opy_.get(bstack111_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᆨ")):
            os.environ[bstack111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᆩ")] = str(bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᆪ")])
        return [bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠨ࡬ࡺࡸࠬᆫ")], bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᆬ")], bstack11lllll1ll_opy_[bstack111_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᆭ")]]
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᆮ")] == bstack111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᆯ") or os.environ[bstack111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᆰ")] == bstack111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᆱ"):
            print(bstack111_opy_ (u"ࠨࡇ࡛ࡇࡊࡖࡔࡊࡑࡑࠤࡎࡔࠠࡴࡶࡲࡴࡇࡻࡩ࡭ࡦࡘࡴࡸࡺࡲࡦࡣࡰࠤࡗࡋࡑࡖࡇࡖࡘ࡚ࠥࡏࠡࡖࡈࡗ࡙ࠦࡏࡃࡕࡈࡖ࡛ࡇࡂࡊࡎࡌࡘ࡞ࠦ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩᆲ"))
            return {
                bstack111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᆳ"): bstack111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᆴ"),
                bstack111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᆵ"): bstack111_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪᆶ")
            }
        else:
            cls.bstack1l11lll11l_opy_.shutdown()
            data = {
                bstack111_opy_ (u"࠭ࡳࡵࡱࡳࡣࡹ࡯࡭ࡦࠩᆷ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack111_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᆸ"): cls.default_headers()
            }
            bstack1ll111l1l1_opy_ = bstack111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩᆹ").format(os.environ[bstack111_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣᆺ")])
            bstack11lll1llll_opy_ = cls.request_url(bstack1ll111l1l1_opy_)
            response = bstack1l1l1111l_opy_(bstack111_opy_ (u"ࠪࡔ࡚࡚ࠧᆻ"), bstack11lll1llll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥᆼ"))
    @classmethod
    def bstack1l11111111_opy_(cls):
        if cls.bstack1l11lll11l_opy_ is None:
            return
        cls.bstack1l11lll11l_opy_.shutdown()
    @classmethod
    def bstack11l111l1_opy_(cls):
        if cls.on():
            print(
                bstack111_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨᆽ").format(os.environ[bstack111_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧᆾ")]))
    @classmethod
    def bstack11llllll11_opy_(cls):
        if cls.bstack1l11lll11l_opy_ is not None:
            return
        cls.bstack1l11lll11l_opy_ = bstack1l11ll11l1_opy_(cls.bstack1l11111lll_opy_)
        cls.bstack1l11lll11l_opy_.start()
    @classmethod
    def bstack1l11111l1l_opy_(cls, bstack1l1111ll11_opy_, bstack1l1111111l_opy_=bstack111_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ᆿ")):
        if not cls.on():
            return
        bstack1111lll1_opy_ = bstack1l1111ll11_opy_[bstack111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᇀ")]
        bstack11lllll1l1_opy_ = {
            bstack111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᇁ"): bstack111_opy_ (u"ࠪࡘࡪࡹࡴࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧᇂ"),
            bstack111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᇃ"): bstack111_opy_ (u"࡚ࠬࡥࡴࡶࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧᇄ"),
            bstack111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᇅ"): bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙࡫ࡪࡲࡳࡩࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ᇆ"),
            bstack111_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᇇ"): bstack111_opy_ (u"ࠩࡏࡳ࡬ࡥࡕࡱ࡮ࡲࡥࡩ࠭ᇈ"),
            bstack111_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᇉ"): bstack111_opy_ (u"ࠫࡍࡵ࡯࡬ࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨᇊ"),
            bstack111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᇋ"): bstack111_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨᇌ"),
            bstack111_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᇍ"): bstack111_opy_ (u"ࠨࡅࡅࡘࡤ࡛ࡰ࡭ࡱࡤࡨࠬᇎ")
        }.get(bstack1111lll1_opy_)
        if bstack1l1111111l_opy_ == bstack111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᇏ"):
            cls.bstack11llllll11_opy_()
            cls.bstack1l11lll11l_opy_.add(bstack1l1111ll11_opy_)
        elif bstack1l1111111l_opy_ == bstack111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᇐ"):
            cls.bstack1l11111lll_opy_([bstack1l1111ll11_opy_], bstack1l1111111l_opy_)
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def bstack1l11111lll_opy_(cls, bstack1l1111ll11_opy_, bstack1l1111111l_opy_=bstack111_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᇑ")):
        config = {
            bstack111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᇒ"): cls.default_headers()
        }
        response = bstack1l1l1111l_opy_(bstack111_opy_ (u"࠭ࡐࡐࡕࡗࠫᇓ"), cls.request_url(bstack1l1111111l_opy_), bstack1l1111ll11_opy_, config)
        bstack11llll1l11_opy_ = response.json()
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def bstack1l1111l111_opy_(cls, bstack11llll1ll1_opy_):
        bstack1l1111ll1l_opy_ = []
        for log in bstack11llll1ll1_opy_:
            bstack11llllllll_opy_ = {
                bstack111_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᇔ"): bstack111_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪᇕ"),
                bstack111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᇖ"): log[bstack111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᇗ")],
                bstack111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᇘ"): log[bstack111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᇙ")],
                bstack111_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭ᇚ"): {},
                bstack111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᇛ"): log[bstack111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᇜ")],
            }
            if bstack111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᇝ") in log:
                bstack11llllllll_opy_[bstack111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᇞ")] = log[bstack111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᇟ")]
            elif bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᇠ") in log:
                bstack11llllllll_opy_[bstack111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᇡ")] = log[bstack111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᇢ")]
            bstack1l1111ll1l_opy_.append(bstack11llllllll_opy_)
        cls.bstack1l11111l1l_opy_({
            bstack111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᇣ"): bstack111_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᇤ"),
            bstack111_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᇥ"): bstack1l1111ll1l_opy_
        })
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def bstack1l11111ll1_opy_(cls, steps):
        bstack1l1111l1l1_opy_ = []
        for step in steps:
            bstack1l111111ll_opy_ = {
                bstack111_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᇦ"): bstack111_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨᇧ"),
                bstack111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᇨ"): step[bstack111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᇩ")],
                bstack111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᇪ"): step[bstack111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᇫ")],
                bstack111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᇬ"): step[bstack111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᇭ")],
                bstack111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᇮ"): step[bstack111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᇯ")]
            }
            if bstack111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᇰ") in step:
                bstack1l111111ll_opy_[bstack111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᇱ")] = step[bstack111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᇲ")]
            elif bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᇳ") in step:
                bstack1l111111ll_opy_[bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᇴ")] = step[bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᇵ")]
            bstack1l1111l1l1_opy_.append(bstack1l111111ll_opy_)
        cls.bstack1l11111l1l_opy_({
            bstack111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᇶ"): bstack111_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᇷ"),
            bstack111_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ᇸ"): bstack1l1111l1l1_opy_
        })
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def bstack1l1111l11l_opy_(cls, screenshot):
        cls.bstack1l11111l1l_opy_({
            bstack111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᇹ"): bstack111_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᇺ"),
            bstack111_opy_ (u"ࠫࡱࡵࡧࡴࠩᇻ"): [{
                bstack111_opy_ (u"ࠬࡱࡩ࡯ࡦࠪᇼ"): bstack111_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨᇽ"),
                bstack111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᇾ"): datetime.datetime.utcnow().isoformat() + bstack111_opy_ (u"ࠨ࡜ࠪᇿ"),
                bstack111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪሀ"): screenshot[bstack111_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩሁ")],
                bstack111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫሂ"): screenshot[bstack111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬሃ")]
            }]
        }, bstack1l1111111l_opy_=bstack111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫሄ"))
    @classmethod
    @bstack1ll1111ll1_opy_(class_method=True)
    def bstack1l1lll1l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11111l1l_opy_({
            bstack111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫህ"): bstack111_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬሆ"),
            bstack111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫሇ"): {
                bstack111_opy_ (u"ࠥࡹࡺ࡯ࡤࠣለ"): cls.current_test_uuid(),
                bstack111_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥሉ"): cls.bstack1l11111l11_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ሊ"), None) is None or os.environ[bstack111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧላ")] == bstack111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧሌ"):
            return False
        return True
    @classmethod
    def bstack1l111111l1_opy_(cls):
        return bstack1l1lll1111_opy_(cls.bs_config.get(bstack111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬል"), False))
    @staticmethod
    def request_url(url):
        return bstack111_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨሎ").format(bstack11lllllll1_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩሏ"): bstack111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧሐ"),
            bstack111_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨሑ"): bstack111_opy_ (u"࠭ࡴࡳࡷࡨࠫሒ")
        }
        if os.environ.get(bstack111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨሓ"), None):
            headers[bstack111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨሔ")] = bstack111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬሕ").format(os.environ[bstack111_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠦሖ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨሗ"), None)
    @staticmethod
    def bstack1l11111l11_opy_(driver):
        return {
            bstack1l1lll11ll_opy_(): bstack1l1ll11l11_opy_(driver)
        }
    @staticmethod
    def bstack11llll11ll_opy_(exception_info, report):
        return [{bstack111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨመ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1ll1111111_opy_(typename):
        if bstack111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤሙ") in typename:
            return bstack111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣሚ")
        return bstack111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤማ")
    @staticmethod
    def bstack11lllll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1111llll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11lllll11l_opy_(test, hook_name=None):
        bstack11llll1lll_opy_ = test.parent
        if hook_name in [bstack111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧሜ"), bstack111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫም"), bstack111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪሞ"), bstack111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧሟ")]:
            bstack11llll1lll_opy_ = test
        scope = []
        while bstack11llll1lll_opy_ is not None:
            scope.append(bstack11llll1lll_opy_.name)
            bstack11llll1lll_opy_ = bstack11llll1lll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11llll11l1_opy_(hook_type):
        if hook_type == bstack111_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦሠ"):
            return bstack111_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦሡ")
        elif hook_type == bstack111_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧሢ"):
            return bstack111_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤሣ")
    @staticmethod
    def bstack11llll111l_opy_(bstack111l1111l_opy_):
        try:
            if not bstack1111llll_opy_.on():
                return bstack111l1111l_opy_
            if os.environ.get(bstack111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣሤ"), None) == bstack111_opy_ (u"ࠦࡹࡸࡵࡦࠤሥ"):
                tests = os.environ.get(bstack111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤሦ"), None)
                if tests is None or tests == bstack111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦሧ"):
                    return bstack111l1111l_opy_
                bstack111l1111l_opy_ = tests.split(bstack111_opy_ (u"ࠧ࠭ࠩረ"))
                return bstack111l1111l_opy_
        except Exception as exc:
            print(bstack111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤሩ"), str(exc))
        return bstack111l1111l_opy_
    @classmethod
    def bstack11llll1l1l_opy_(cls, event: str, bstack1l1111ll11_opy_: bstack1l11l11111_opy_):
        bstack11llllll1l_opy_ = {
            bstack111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ሪ"): event,
            bstack1l1111ll11_opy_.bstack1l111ll11l_opy_(): bstack1l1111ll11_opy_.bstack1l111ll1l1_opy_(event)
        }
        bstack1111llll_opy_.bstack1l11111l1l_opy_(bstack11llllll1l_opy_)