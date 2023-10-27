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
import atexit
import datetime
import inspect
import logging
import os
import sys
import threading
from uuid import uuid4
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l111ll11_opy_, bstack1l1l1l1ll_opy_, update, bstack111lll1l1_opy_,
                                       bstack1l1l11lll_opy_, bstack1ll1l1l1l_opy_, bstack1llll11ll1_opy_, bstack1ll1111l_opy_,
                                       bstack111ll111l_opy_, bstack1l1l1ll1l_opy_, bstack111l1ll1l_opy_, bstack1ll1l1111_opy_,
                                       bstack1lllll11_opy_)
from browserstack_sdk._version import __version__
from bstack_utils.capture import bstack1ll11l11l1_opy_
from bstack_utils.constants import bstack11l1lllll_opy_, bstack1lll11l111_opy_, bstack11ll11l1l_opy_, bstack1lll1l1ll1_opy_, \
    bstack1ll1ll1111_opy_
from bstack_utils.helper import bstack1l1ll11l1l_opy_, bstack1l1llll111_opy_, bstack1lllll111_opy_, bstack1l1llll1l1_opy_, \
    bstack1ll11111ll_opy_, bstack11111ll11_opy_, bstack1lll1ll111_opy_, bstack1l1lllll11_opy_, bstack1l1lllll1_opy_, Notset, \
    bstack1ll11l1l_opy_, bstack1l1ll1ll1l_opy_, bstack1l1ll1llll_opy_, Result, bstack1l1lllll1l_opy_, bstack1ll1111l1l_opy_, bstack1ll1111ll1_opy_
from bstack_utils.bstack1l1l1lll11_opy_ import bstack1l1l1l1l1l_opy_
from bstack_utils.messages import bstack1lll1111l_opy_, bstack11l11l11l_opy_, bstack11lll1l1l_opy_, bstack1111ll1l1_opy_, bstack11ll1l1l_opy_, \
    bstack1ll1ll1ll1_opy_, bstack11lll111l_opy_, bstack1lll11111l_opy_, bstack1llll1l1l_opy_, bstack1l1ll1l1_opy_, \
    bstack1111l111l_opy_, bstack11l111lll_opy_
from bstack_utils.proxy import bstack1lll111111_opy_, bstack11llll1l1_opy_
from bstack_utils.bstack1l1l111ll1_opy_ import bstack1l1l11111l_opy_, bstack1l1l1111ll_opy_, bstack1l11llllll_opy_, \
    bstack1l1l111l11_opy_, bstack1l11llll1l_opy_, bstack1l1l1111l1_opy_
from bstack_utils.bstack1l11l1ll1l_opy_ import bstack1l11l1llll_opy_
from bstack_utils.bstack1l11l11lll_opy_ import bstack1ll1llllll_opy_, bstack1l1l1l11_opy_, bstack1llll11lll_opy_
from bstack_utils.bstack1l111lll1l_opy_ import bstack1l11l1111l_opy_
from bstack_utils.bstack1ll1l11lll_opy_ import bstack1111llll_opy_
bstack111l1llll_opy_ = None
bstack11l111l11_opy_ = None
bstack1llll1lll_opy_ = None
bstack1ll1ll1lll_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack1l1111111_opy_ = None
bstack1lll1l11_opy_ = None
bstack1111l1lll_opy_ = None
bstack1l11l1l11_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack1ll1ll1l_opy_ = None
bstack1111l1ll1_opy_ = None
bstack1lllllll11_opy_ = bstack111_opy_ (u"ࠪࠫራ")
CONFIG = {}
bstack1lllll1l1l_opy_ = False
bstack1l1l1111_opy_ = bstack111_opy_ (u"ࠫࠬሬ")
bstack1ll111ll1_opy_ = bstack111_opy_ (u"ࠬ࠭ር")
bstack1l11llll_opy_ = False
bstack1ll1l11l_opy_ = []
bstack1ll1l1l11_opy_ = bstack1lll11l111_opy_
bstack11lll111ll_opy_ = bstack111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ሮ")
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1ll1l1l11_opy_,
                    format=bstack111_opy_ (u"ࠧ࡝ࡰࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬሯ"),
                    datefmt=bstack111_opy_ (u"ࠨࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪሰ"),
                    stream=sys.stdout)
store = {
    bstack111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ሱ"): []
}
def bstack1lll111ll1_opy_():
    global CONFIG
    global bstack1ll1l1l11_opy_
    if bstack111_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬሲ") in CONFIG:
        bstack1ll1l1l11_opy_ = bstack11l1lllll_opy_[CONFIG[bstack111_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ሳ")]]
        logging.getLogger().setLevel(bstack1ll1l1l11_opy_)
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11lll11l11_opy_ = {}
current_test_uuid = None
def bstack1l1l1l111_opy_(page, bstack1111l1l1l_opy_):
    try:
        page.evaluate(bstack111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨሴ"),
                      bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪስ") + json.dumps(
                          bstack1111l1l1l_opy_) + bstack111_opy_ (u"ࠢࡾࡿࠥሶ"))
    except Exception as e:
        print(bstack111_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨሷ"), e)
def bstack1ll11l111_opy_(page, message, level):
    try:
        page.evaluate(bstack111_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥሸ"), bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨሹ") + json.dumps(
            message) + bstack111_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧሺ") + json.dumps(level) + bstack111_opy_ (u"ࠬࢃࡽࠨሻ"))
    except Exception as e:
        print(bstack111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤሼ"), e)
def bstack1l1l11111_opy_(page, status, message=bstack111_opy_ (u"ࠢࠣሽ")):
    try:
        if (status == bstack111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣሾ")):
            page.evaluate(bstack111_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥሿ"),
                          bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠫቀ") + json.dumps(
                              bstack111_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࠨቁ") + str(message)) + bstack111_opy_ (u"ࠬ࠲ࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩቂ") + json.dumps(status) + bstack111_opy_ (u"ࠨࡽࡾࠤቃ"))
        else:
            page.evaluate(bstack111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣቄ"),
                          bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩቅ") + json.dumps(
                              status) + bstack111_opy_ (u"ࠤࢀࢁࠧቆ"))
    except Exception as e:
        print(bstack111_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢቇ"), e)
def pytest_configure(config):
    config.args = bstack1111llll_opy_.bstack11llll111l_opy_(config.args)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack11ll11llll_opy_ = item.config.getoption(bstack111_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ቈ"))
    plugins = item.config.getoption(bstack111_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨ቉"))
    report = outcome.get_result()
    bstack11ll1l111l_opy_(item, call, report)
    if bstack111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠦቊ") not in plugins or bstack1l1lllll1_opy_():
        return
    summary = []
    driver = getattr(item, bstack111_opy_ (u"ࠢࡠࡦࡵ࡭ࡻ࡫ࡲࠣቋ"), None)
    page = getattr(item, bstack111_opy_ (u"ࠣࡡࡳࡥ࡬࡫ࠢቌ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack11ll11ll11_opy_(item, report, summary, bstack11ll11llll_opy_)
    if (page is not None):
        bstack11ll1l1l1l_opy_(item, report, summary, bstack11ll11llll_opy_)
def bstack11ll11ll11_opy_(item, report, summary, bstack11ll11llll_opy_):
    if report.when in [bstack111_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣቍ"), bstack111_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ቎")]:
        return
    if not bstack1l1llll111_opy_():
        return
    try:
        if (str(bstack11ll11llll_opy_).lower() != bstack111_opy_ (u"ࠫࡹࡸࡵࡦࠩ቏")):
            item._driver.execute_script(
                bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪቐ") + json.dumps(
                    report.nodeid) + bstack111_opy_ (u"࠭ࡽࡾࠩቑ"))
    except Exception as e:
        summary.append(
            bstack111_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢቒ").format(e)
        )
    passed = report.passed or (report.failed and hasattr(report, bstack111_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥቓ")))
    bstack1llll11l11_opy_ = bstack111_opy_ (u"ࠤࠥቔ")
    if not passed:
        try:
            bstack1llll11l11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥቕ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1llll11l11_opy_))
    try:
        if passed:
            item._driver.execute_script(
                bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡪࡡࡵࡣࠥ࠾ࠥ࠭ቖ")
                + json.dumps(bstack111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠦࠨ቗"))
                + bstack111_opy_ (u"ࠨ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣቘ")
            )
        else:
            item._driver.execute_script(
                bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡧࡥࡹࡧࠢ࠻ࠢࠪ቙")
                + json.dumps(str(bstack1llll11l11_opy_))
                + bstack111_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥቚ")
            )
    except Exception as e:
        summary.append(bstack111_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡢࡰࡱࡳࡹࡧࡴࡦ࠼ࠣࡿ࠵ࢃࠢቛ").format(e))
def bstack11ll1l1l1l_opy_(item, report, summary, bstack11ll11llll_opy_):
    if report.when in [bstack111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤቜ"), bstack111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨቝ")]:
        return
    if (str(bstack11ll11llll_opy_).lower() != bstack111_opy_ (u"ࠬࡺࡲࡶࡧࠪ቞")):
        bstack1l1l1l111_opy_(item._page, report.nodeid)
    passed = report.passed or (report.failed and hasattr(report, bstack111_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ቟")))
    bstack1llll11l11_opy_ = bstack111_opy_ (u"ࠢࠣበ")
    if not passed:
        try:
            bstack1llll11l11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣቡ").format(e)
            )
    try:
        if passed:
            bstack1l1l11111_opy_(item._page, bstack111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤቢ"))
        else:
            if bstack1llll11l11_opy_:
                bstack1ll11l111_opy_(item._page, str(bstack1llll11l11_opy_), bstack111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤባ"))
                bstack1l1l11111_opy_(item._page, bstack111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦቤ"), str(bstack1llll11l11_opy_))
            else:
                bstack1l1l11111_opy_(item._page, bstack111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧብ"))
    except Exception as e:
        summary.append(bstack111_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡺࡶࡤࡢࡶࡨࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻ࠱ࡿࠥቦ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack111_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦቧ"), default=bstack111_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢቨ"), help=bstack111_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣቩ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111_opy_ (u"ࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧቪ"), action=bstack111_opy_ (u"ࠦࡸࡺ࡯ࡳࡧࠥቫ"), default=bstack111_opy_ (u"ࠧࡩࡨࡳࡱࡰࡩࠧቬ"),
                         help=bstack111_opy_ (u"ࠨࡄࡳ࡫ࡹࡩࡷࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷࠧቭ"))
def bstack11ll11ll1l_opy_(log):
    if not (log[bstack111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨቮ")] and log[bstack111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩቯ")].strip()):
        return
    active = bstack11lll111l1_opy_()
    log = {
        bstack111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨተ"): log[bstack111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩቱ")],
        bstack111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧቲ"): datetime.datetime.utcnow().isoformat() + bstack111_opy_ (u"ࠬࡠࠧታ"),
        bstack111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧቴ"): log[bstack111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨት")],
    }
    if active:
        if active[bstack111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ቶ")] == bstack111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧቷ"):
            log[bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪቸ")] = active[bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫቹ")]
        elif active[bstack111_opy_ (u"ࠬࡺࡹࡱࡧࠪቺ")] == bstack111_opy_ (u"࠭ࡴࡦࡵࡷࠫቻ"):
            log[bstack111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧቼ")] = active[bstack111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨች")]
    bstack1111llll_opy_.bstack1l1111l111_opy_([log])
def bstack11lll111l1_opy_():
    if len(store[bstack111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ቾ")]) > 0 and store[bstack111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧቿ")][-1]:
        return {
            bstack111_opy_ (u"ࠫࡹࡿࡰࡦࠩኀ"): bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪኁ"),
            bstack111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ኂ"): store[bstack111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫኃ")][-1]
        }
    if store.get(bstack111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬኄ"), None):
        return {
            bstack111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧኅ"): bstack111_opy_ (u"ࠪࡸࡪࡹࡴࠨኆ"),
            bstack111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫኇ"): store[bstack111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩኈ")]
        }
    return None
bstack11ll11l1l1_opy_ = bstack1ll11l11l1_opy_(bstack11ll11ll1l_opy_)
def pytest_runtest_call(item):
    try:
        if not bstack1111llll_opy_.on() or bstack11lll111ll_opy_ != bstack111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭኉"):
            return
        global current_test_uuid, bstack11ll11l1l1_opy_
        bstack11ll11l1l1_opy_.start()
        bstack11lll11ll1_opy_ = {
            bstack111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬኊ"): uuid4().__str__(),
            bstack111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬኋ"): datetime.datetime.utcnow().isoformat() + bstack111_opy_ (u"ࠩ࡝ࠫኌ")
        }
        current_test_uuid = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨኍ")]
        store[bstack111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ኎")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠬࡻࡵࡪࡦࠪ኏")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11lll11l11_opy_[item.nodeid] = {**_11lll11l11_opy_[item.nodeid], **bstack11lll11ll1_opy_}
        bstack11ll1lll11_opy_(item, _11lll11l11_opy_[item.nodeid], bstack111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧነ"))
    except Exception as err:
        print(bstack111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡤࡣ࡯ࡰ࠿ࠦࡻࡾࠩኑ"), str(err))
def pytest_runtest_setup(item):
    if bstack1l1lllll11_opy_():
        atexit.register(bstack1llll1l111_opy_)
    try:
        if not bstack1111llll_opy_.on():
            return
        bstack11ll11l1l1_opy_.start()
        uuid = uuid4().__str__()
        bstack11lll11ll1_opy_ = {
            bstack111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ኒ"): uuid,
            bstack111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ና"): datetime.datetime.utcnow().isoformat() + bstack111_opy_ (u"ࠪ࡞ࠬኔ"),
            bstack111_opy_ (u"ࠫࡹࡿࡰࡦࠩን"): bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪኖ"),
            bstack111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩኗ"): bstack111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬኘ"),
            bstack111_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫኙ"): bstack111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨኚ")
        }
        threading.current_thread().bstack11ll1l1lll_opy_ = uuid
        store[bstack111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧኛ")] = item
        store[bstack111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨኜ")] = [uuid]
        if not _11lll11l11_opy_.get(item.nodeid, None):
            _11lll11l11_opy_[item.nodeid] = {bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫኝ"): [], bstack111_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨኞ"): []}
        _11lll11l11_opy_[item.nodeid][bstack111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ኟ")].append(bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭አ")])
        _11lll11l11_opy_[item.nodeid + bstack111_opy_ (u"ࠩ࠰ࡷࡪࡺࡵࡱࠩኡ")] = bstack11lll11ll1_opy_
        bstack11ll1l1111_opy_(item, bstack11lll11ll1_opy_, bstack111_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫኢ"))
    except Exception as err:
        print(bstack111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧኣ"), str(err))
def pytest_runtest_teardown(item):
    try:
        if not bstack1111llll_opy_.on():
            return
        bstack11lll11ll1_opy_ = {
            bstack111_opy_ (u"ࠬࡻࡵࡪࡦࠪኤ"): uuid4().__str__(),
            bstack111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪእ"): datetime.datetime.utcnow().isoformat() + bstack111_opy_ (u"࡛ࠧࠩኦ"),
            bstack111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ኧ"): bstack111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧከ"),
            bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ኩ"): bstack111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨኪ"),
            bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨካ"): bstack111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨኬ")
        }
        _11lll11l11_opy_[item.nodeid + bstack111_opy_ (u"ࠧ࠮ࡶࡨࡥࡷࡪ࡯ࡸࡰࠪክ")] = bstack11lll11ll1_opy_
        bstack11ll1l1111_opy_(item, bstack11lll11ll1_opy_, bstack111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩኮ"))
    except Exception as err:
        print(bstack111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱ࠾ࠥࢁࡽࠨኯ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1111llll_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1l11llllll_opy_(fixturedef.argname):
        store[bstack111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩኰ")] = request.node
    elif bstack1l1l111l11_opy_(fixturedef.argname):
        store[bstack111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩ኱")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪኲ"): fixturedef.argname,
            bstack111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ኳ"): bstack1l1llll1l1_opy_(outcome),
            bstack111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩኴ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        bstack11lll1l11l_opy_ = store[bstack111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬኵ")]
        if not _11lll11l11_opy_.get(bstack11lll1l11l_opy_.nodeid, None):
            _11lll11l11_opy_[bstack11lll1l11l_opy_.nodeid] = {bstack111_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ኶"): []}
        _11lll11l11_opy_[bstack11lll1l11l_opy_.nodeid][bstack111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ኷")].append(fixture)
    except Exception as err:
        logger.debug(bstack111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧኸ"), str(err))
if bstack1l1lllll1_opy_() and bstack1111llll_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11lll11l11_opy_[request.node.nodeid][bstack111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨኹ")].bstack1l111llll1_opy_(id(step))
        except Exception as err:
            print(bstack111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶ࠺ࠡࡽࢀࠫኺ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11lll11l11_opy_[request.node.nodeid][bstack111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪኻ")].bstack1l11l111l1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬኼ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l111lll1l_opy_: bstack1l11l1111l_opy_ = _11lll11l11_opy_[request.node.nodeid][bstack111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬኽ")]
            bstack1l111lll1l_opy_.bstack1l11l111l1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧኾ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack11lll111ll_opy_
        try:
            if not bstack1111llll_opy_.on() or bstack11lll111ll_opy_ != bstack111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨ኿"):
                return
            global bstack11ll11l1l1_opy_
            bstack11ll11l1l1_opy_.start()
            if not _11lll11l11_opy_.get(request.node.nodeid, None):
                _11lll11l11_opy_[request.node.nodeid] = {}
            bstack1l111lll1l_opy_ = bstack1l11l1111l_opy_.bstack1l111l1lll_opy_(
                scenario, feature, request.node,
                name=bstack1l11llll1l_opy_(request.node, scenario),
                bstack1l111l111l_opy_=bstack1lllll111_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧዀ"),
                tags=bstack1l1l1111l1_opy_(feature, scenario)
            )
            _11lll11l11_opy_[request.node.nodeid][bstack111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ዁")] = bstack1l111lll1l_opy_
            bstack11ll1ll1ll_opy_(bstack1l111lll1l_opy_.uuid)
            bstack1111llll_opy_.bstack11llll1l1l_opy_(bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨዂ"), bstack1l111lll1l_opy_)
        except Exception as err:
            print(bstack111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪዃ"), str(err))
def bstack11ll1l1l11_opy_(bstack11lll1ll11_opy_):
    if bstack11lll1ll11_opy_ in store[bstack111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ዄ")]:
        store[bstack111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧዅ")].remove(bstack11lll1ll11_opy_)
def bstack11ll1ll1ll_opy_(bstack11ll1ll11l_opy_):
    store[bstack111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ዆")] = bstack11ll1ll11l_opy_
    threading.current_thread().current_test_uuid = bstack11ll1ll11l_opy_
@bstack1111llll_opy_.bstack11lllll111_opy_
def bstack11ll1l111l_opy_(item, call, report):
    global bstack11lll111ll_opy_
    try:
        if report.when == bstack111_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ዇"):
            bstack11ll11l1l1_opy_.reset()
        if report.when == bstack111_opy_ (u"࠭ࡣࡢ࡮࡯ࠫወ"):
            if bstack11lll111ll_opy_ == bstack111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧዉ"):
                _11lll11l11_opy_[item.nodeid][bstack111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ዊ")] = bstack1l1lllll1l_opy_(report.stop)
                bstack11ll1lll11_opy_(item, _11lll11l11_opy_[item.nodeid], bstack111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫዋ"), report, call)
                store[bstack111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧዌ")] = None
            elif bstack11lll111ll_opy_ == bstack111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣው"):
                bstack1l111lll1l_opy_ = _11lll11l11_opy_[item.nodeid][bstack111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨዎ")]
                bstack1l111lll1l_opy_.set(hooks=_11lll11l11_opy_[item.nodeid].get(bstack111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬዏ"), []))
                exception, bstack1ll11111l1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1ll11111l1_opy_ = [call.excinfo.exconly(), report.longreprtext]
                bstack1l111lll1l_opy_.stop(time=bstack1l1lllll1l_opy_(report.stop), result=Result(result=report.outcome, exception=exception, bstack1ll11111l1_opy_=bstack1ll11111l1_opy_))
                bstack1111llll_opy_.bstack11llll1l1l_opy_(bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩዐ"), _11lll11l11_opy_[item.nodeid][bstack111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫዑ")])
        elif report.when in [bstack111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨዒ"), bstack111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬዓ")]:
            bstack11ll1l11ll_opy_ = item.nodeid + bstack111_opy_ (u"ࠫ࠲࠭ዔ") + report.when
            if report.skipped:
                hook_type = bstack111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪዕ") if report.when == bstack111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬዖ") else bstack111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ዗")
                _11lll11l11_opy_[bstack11ll1l11ll_opy_] = {
                    bstack111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ዘ"): uuid4().__str__(),
                    bstack111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ዙ"): datetime.datetime.utcfromtimestamp(report.start).isoformat() + bstack111_opy_ (u"ࠪ࡞ࠬዚ"),
                    bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧዛ"): hook_type
                }
            _11lll11l11_opy_[bstack11ll1l11ll_opy_][bstack111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪዜ")] = datetime.datetime.utcfromtimestamp(report.stop).isoformat() + bstack111_opy_ (u"࡚࠭ࠨዝ")
            bstack11ll1l1l11_opy_(_11lll11l11_opy_[bstack11ll1l11ll_opy_][bstack111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬዞ")])
            bstack11ll1l1111_opy_(item, _11lll11l11_opy_[bstack11ll1l11ll_opy_], bstack111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪዟ"), report, call)
            if report.when == bstack111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨዠ"):
                if report.outcome == bstack111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪዡ"):
                    bstack11lll11ll1_opy_ = {
                        bstack111_opy_ (u"ࠫࡺࡻࡩࡥࠩዢ"): uuid4().__str__(),
                        bstack111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩዣ"): bstack1lllll111_opy_(),
                        bstack111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫዤ"): bstack1lllll111_opy_()
                    }
                    _11lll11l11_opy_[item.nodeid] = {**_11lll11l11_opy_[item.nodeid], **bstack11lll11ll1_opy_}
                    bstack11ll1lll11_opy_(item, _11lll11l11_opy_[item.nodeid], bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨዥ"))
                    bstack11ll1lll11_opy_(item, _11lll11l11_opy_[item.nodeid], bstack111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪዦ"), report, call)
    except Exception as err:
        print(bstack111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࢀࢃࠧዧ"), str(err))
def bstack11ll1lllll_opy_(test, bstack11lll11ll1_opy_, result=None, call=None, bstack1111lll1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l111lll1l_opy_ = {
        bstack111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨየ"): bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠫࡺࡻࡩࡥࠩዩ")],
        bstack111_opy_ (u"ࠬࡺࡹࡱࡧࠪዪ"): bstack111_opy_ (u"࠭ࡴࡦࡵࡷࠫያ"),
        bstack111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬዬ"): test.name,
        bstack111_opy_ (u"ࠨࡤࡲࡨࡾ࠭ይ"): {
            bstack111_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧዮ"): bstack111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪዯ"),
            bstack111_opy_ (u"ࠫࡨࡵࡤࡦࠩደ"): inspect.getsource(test.obj)
        },
        bstack111_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩዱ"): test.name,
        bstack111_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬዲ"): test.name,
        bstack111_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧዳ"): bstack1111llll_opy_.bstack11lllll11l_opy_(test),
        bstack111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫዴ"): file_path,
        bstack111_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫድ"): file_path,
        bstack111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪዶ"): bstack111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬዷ"),
        bstack111_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪዸ"): file_path,
        bstack111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪዹ"): bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫዺ")],
        bstack111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫዻ"): bstack111_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩዼ"),
        bstack111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭ዽ"): {
            bstack111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨዾ"): test.nodeid
        },
        bstack111_opy_ (u"ࠬࡺࡡࡨࡵࠪዿ"): bstack1ll11111ll_opy_(test.own_markers)
    }
    if bstack1111lll1_opy_ in [bstack111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧጀ"), bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩጁ")]:
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭ጂ")] = {
            bstack111_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫጃ"): bstack11lll11ll1_opy_.get(bstack111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬጄ"), [])
        }
    if bstack1111lll1_opy_ == bstack111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬጅ"):
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬጆ")] = bstack111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧጇ")
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ገ")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧጉ")]
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧጊ")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨጋ")]
    if result:
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫጌ")] = result.outcome
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ግ")] = result.duration * 1000
        bstack1l111lll1l_opy_[bstack111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫጎ")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬጏ")]
        if result.failed:
            bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧጐ")] = bstack1111llll_opy_.bstack1ll1111111_opy_(call.excinfo.typename)
            bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ጑")] = bstack1111llll_opy_.bstack11llll11ll_opy_(call.excinfo, result)
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩጒ")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪጓ")]
    if outcome:
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬጔ")] = bstack1l1llll1l1_opy_(outcome)
        bstack1l111lll1l_opy_[bstack111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧጕ")] = 0
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ጖")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭጗")]
        if bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩጘ")] == bstack111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪጙ"):
            bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪጚ")] = bstack111_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭ጛ")  # bstack11lll11111_opy_
            bstack1l111lll1l_opy_[bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧጜ")] = [{bstack111_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪጝ"): [bstack111_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬጞ")]}]
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨጟ")] = bstack11lll11ll1_opy_[bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩጠ")]
    return bstack1l111lll1l_opy_
def bstack11lll1l111_opy_(test, bstack11lll11l1l_opy_, bstack1111lll1_opy_, result, call, outcome, bstack11lll1ll1l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧጡ")]
    hook_name = bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨጢ")]
    hook_data = {
        bstack111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫጣ"): bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬጤ")],
        bstack111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ጥ"): bstack111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧጦ"),
        bstack111_opy_ (u"ࠪࡲࡦࡳࡥࠨጧ"): bstack111_opy_ (u"ࠫࢀࢃࠧጨ").format(bstack1l1l11111l_opy_(hook_name)),
        bstack111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪጩ"): {
            bstack111_opy_ (u"࠭࡬ࡢࡰࡪࠫጪ"): bstack111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧጫ"),
            bstack111_opy_ (u"ࠨࡥࡲࡨࡪ࠭ጬ"): None
        },
        bstack111_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨጭ"): test.name,
        bstack111_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪጮ"): bstack1111llll_opy_.bstack11lllll11l_opy_(test, hook_name),
        bstack111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧጯ"): file_path,
        bstack111_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧጰ"): file_path,
        bstack111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ጱ"): bstack111_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨጲ"),
        bstack111_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ጳ"): file_path,
        bstack111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ጴ"): bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧጵ")],
        bstack111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧጶ"): bstack111_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧጷ") if bstack11lll111ll_opy_ == bstack111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪጸ") else bstack111_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧጹ"),
        bstack111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫጺ"): hook_type
    }
    bstack11ll11l1ll_opy_ = bstack11lll1111l_opy_(_11lll11l11_opy_.get(test.nodeid, None))
    if bstack11ll11l1ll_opy_:
        hook_data[bstack111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧጻ")] = bstack11ll11l1ll_opy_
    if result:
        hook_data[bstack111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪጼ")] = result.outcome
        hook_data[bstack111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬጽ")] = result.duration * 1000
        hook_data[bstack111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪጾ")] = bstack11lll11l1l_opy_[bstack111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫጿ")]
        if result.failed:
            hook_data[bstack111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ፀ")] = bstack1111llll_opy_.bstack1ll1111111_opy_(call.excinfo.typename)
            hook_data[bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩፁ")] = bstack1111llll_opy_.bstack11llll11ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩፂ")] = bstack1l1llll1l1_opy_(outcome)
        hook_data[bstack111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫፃ")] = 100
        hook_data[bstack111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩፄ")] = bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪፅ")]
        if hook_data[bstack111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ፆ")] == bstack111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧፇ"):
            hook_data[bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧፈ")] = bstack111_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪፉ")  # bstack11lll11111_opy_
            hook_data[bstack111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫፊ")] = [{bstack111_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧፋ"): [bstack111_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩፌ")]}]
    if bstack11lll1ll1l_opy_:
        hook_data[bstack111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ፍ")] = bstack11lll1ll1l_opy_.result
        hook_data[bstack111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨፎ")] = bstack1l1ll1ll1l_opy_(bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬፏ")], bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧፐ")])
        hook_data[bstack111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨፑ")] = bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩፒ")]
        if hook_data[bstack111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬፓ")] == bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ፔ"):
            hook_data[bstack111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ፕ")] = bstack1111llll_opy_.bstack1ll1111111_opy_(bstack11lll1ll1l_opy_.exception_type)
            hook_data[bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩፖ")] = [{bstack111_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬፗ"): bstack1l1ll1llll_opy_(bstack11lll1ll1l_opy_.exception)}]
    return hook_data
def bstack11ll1lll11_opy_(test, bstack11lll11ll1_opy_, bstack1111lll1_opy_, result=None, call=None, outcome=None):
    bstack1l111lll1l_opy_ = bstack11ll1lllll_opy_(test, bstack11lll11ll1_opy_, result, call, bstack1111lll1_opy_, outcome)
    driver = getattr(test, bstack111_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫፘ"), None)
    if bstack1111lll1_opy_ == bstack111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬፙ") and driver:
        bstack1l111lll1l_opy_[bstack111_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫፚ")] = bstack1111llll_opy_.bstack1l11111l11_opy_(driver)
    if bstack1111lll1_opy_ == bstack111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ፛"):
        bstack1111lll1_opy_ = bstack111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ፜")
    bstack11llllll1l_opy_ = {
        bstack111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ፝"): bstack1111lll1_opy_,
        bstack111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ፞"): bstack1l111lll1l_opy_
    }
    bstack1111llll_opy_.bstack1l11111l1l_opy_(bstack11llllll1l_opy_)
def bstack11ll1l1111_opy_(test, bstack11lll11ll1_opy_, bstack1111lll1_opy_, result=None, call=None, outcome=None, bstack11lll1ll1l_opy_=None):
    hook_data = bstack11lll1l111_opy_(test, bstack11lll11ll1_opy_, bstack1111lll1_opy_, result, call, outcome, bstack11lll1ll1l_opy_)
    bstack11llllll1l_opy_ = {
        bstack111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ፟"): bstack1111lll1_opy_,
        bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳ࠭፠"): hook_data
    }
    bstack1111llll_opy_.bstack1l11111l1l_opy_(bstack11llllll1l_opy_)
def bstack11lll1111l_opy_(bstack11lll11ll1_opy_):
    if not bstack11lll11ll1_opy_:
        return None
    if bstack11lll11ll1_opy_.get(bstack111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ፡"), None):
        return getattr(bstack11lll11ll1_opy_[bstack111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ።")], bstack111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ፣"), None)
    return bstack11lll11ll1_opy_.get(bstack111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭፤"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1111llll_opy_.on():
            return
        places = [bstack111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ፥"), bstack111_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ፦"), bstack111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭፧")]
        bstack11llll1ll1_opy_ = []
        for bstack11ll1ll1l1_opy_ in places:
            records = caplog.get_records(bstack11ll1ll1l1_opy_)
            bstack11ll1l11l1_opy_ = bstack111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ፨") if bstack11ll1ll1l1_opy_ == bstack111_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ፩") else bstack111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ፪")
            bstack11lll1l1l1_opy_ = request.node.nodeid + (bstack111_opy_ (u"ࠨࠩ፫") if bstack11ll1ll1l1_opy_ == bstack111_opy_ (u"ࠩࡦࡥࡱࡲࠧ፬") else bstack111_opy_ (u"ࠪ࠱ࠬ፭") + bstack11ll1ll1l1_opy_)
            bstack11ll1ll11l_opy_ = bstack11lll1111l_opy_(_11lll11l11_opy_.get(bstack11lll1l1l1_opy_, None))
            if not bstack11ll1ll11l_opy_:
                continue
            for record in records:
                if bstack1ll1111l1l_opy_(record.message):
                    continue
                bstack11llll1ll1_opy_.append({
                    bstack111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ፮"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack111_opy_ (u"ࠬࡠࠧ፯"),
                    bstack111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ፰"): record.levelname,
                    bstack111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ፱"): record.message,
                    bstack11ll1l11l1_opy_: bstack11ll1ll11l_opy_
                })
        if len(bstack11llll1ll1_opy_) > 0:
            bstack1111llll_opy_.bstack1l1111l111_opy_(bstack11llll1ll1_opy_)
    except Exception as err:
        print(bstack111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡦࡳࡳࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥ࠻ࠢࡾࢁࠬ፲"), str(err))
def bstack11ll1llll1_opy_(driver_command, response):
    if driver_command == bstack111_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭፳"):
        bstack1111llll_opy_.bstack1l1111l11l_opy_({
            bstack111_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩ፴"): response[bstack111_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪ፵")],
            bstack111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ፶"): store[bstack111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ፷")]
        })
def bstack1llll1l111_opy_():
    global bstack1ll1l11l_opy_
    bstack1111llll_opy_.bstack1l11111111_opy_()
    for driver in bstack1ll1l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1l1lll_opy_(self, *args, **kwargs):
    bstack1lllll1111_opy_ = bstack111l1llll_opy_(self, *args, **kwargs)
    bstack1111llll_opy_.bstack1l1lll1l1_opy_(self)
    return bstack1lllll1111_opy_
def bstack1lllll11ll_opy_(framework_name):
    global bstack1lllllll11_opy_
    global bstack1lll11l1l_opy_
    bstack1lllllll11_opy_ = framework_name
    logger.info(bstack11l111lll_opy_.format(bstack1lllllll11_opy_.split(bstack111_opy_ (u"ࠧ࠮ࠩ፸"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1l1llll111_opy_():
            Service.start = bstack1llll11ll1_opy_
            Service.stop = bstack1ll1111l_opy_
            webdriver.Remote.__init__ = bstack111ll1111_opy_
            webdriver.Remote.get = bstack11llll11l_opy_
            if not isinstance(os.getenv(bstack111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩ፹")), str):
                return
            WebDriver.close = bstack111ll111l_opy_
            WebDriver.quit = bstack1l11lll1l_opy_
        if not bstack1l1llll111_opy_() and bstack1111llll_opy_.on():
            webdriver.Remote.__init__ = bstack1ll1l1lll_opy_
        bstack1lll11l1l_opy_ = True
    except Exception as e:
        pass
    bstack11111l111_opy_()
    if os.environ.get(bstack111_opy_ (u"ࠩࡖࡉࡑࡋࡎࡊࡗࡐࡣࡔࡘ࡟ࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡎࡔࡓࡕࡃࡏࡐࡊࡊࠧ፺")):
        bstack1lll11l1l_opy_ = eval(os.environ.get(bstack111_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨ፻")))
    if not bstack1lll11l1l_opy_:
        bstack111l1ll1l_opy_(bstack111_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨ፼"), bstack1111l111l_opy_)
    if bstack1lll1l11l1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1lllll11l1_opy_
        except Exception as e:
            logger.error(bstack1ll1ll1ll1_opy_.format(str(e)))
    if bstack111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ፽") in str(framework_name).lower():
        if not bstack1l1llll111_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1l1l11lll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll1l1l1l_opy_
            Config.getoption = bstack111l1lll_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l111llll_opy_
        except Exception as e:
            pass
def bstack1l11lll1l_opy_(self):
    global bstack1lllllll11_opy_
    global bstack1llll111_opy_
    global bstack11l111l11_opy_
    try:
        if bstack111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭፾") in bstack1lllllll11_opy_ and self.session_id != None:
            bstack1llll1l1l1_opy_ = bstack111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ፿") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᎀ")
            bstack1l1ll1ll1_opy_ = bstack1ll1llllll_opy_(bstack111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᎁ"), bstack111_opy_ (u"ࠪࠫᎂ"), bstack1llll1l1l1_opy_, bstack111_opy_ (u"ࠫ࠱ࠦࠧᎃ").join(
                threading.current_thread().bstackTestErrorMessages), bstack111_opy_ (u"ࠬ࠭ᎄ"), bstack111_opy_ (u"࠭ࠧᎅ"))
            if self != None:
                self.execute_script(bstack1l1ll1ll1_opy_)
    except Exception as e:
        logger.debug(bstack111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣᎆ") + str(e))
    bstack11l111l11_opy_(self)
    self.session_id = None
def bstack111ll1111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1llll111_opy_
    global bstack1lll1111_opy_
    global bstack1l11llll_opy_
    global bstack1lllllll11_opy_
    global bstack111l1llll_opy_
    global bstack1ll1l11l_opy_
    global bstack1l1l1111_opy_
    global bstack1ll111ll1_opy_
    CONFIG[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᎇ")] = str(bstack1lllllll11_opy_) + str(__version__)
    command_executor = bstack1lll1ll111_opy_(bstack1l1l1111_opy_)
    logger.debug(bstack1111ll1l1_opy_.format(command_executor))
    proxy = bstack1lllll11_opy_(CONFIG, proxy)
    bstack1lll111l1l_opy_ = 0
    try:
        if bstack1l11llll_opy_ is True:
            bstack1lll111l1l_opy_ = int(os.environ.get(bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᎈ")))
    except:
        bstack1lll111l1l_opy_ = 0
    bstack1llll11l1_opy_ = bstack1l111ll11_opy_(CONFIG, bstack1lll111l1l_opy_)
    logger.debug(bstack1lll11111l_opy_.format(str(bstack1llll11l1_opy_)))
    if bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᎉ") in CONFIG and CONFIG[bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᎊ")]:
        bstack1llll11lll_opy_(bstack1llll11l1_opy_, bstack1ll111ll1_opy_)
    if desired_capabilities:
        bstack1l1l11l11_opy_ = bstack1l1l1l1ll_opy_(desired_capabilities)
        bstack1l1l11l11_opy_[bstack111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᎋ")] = bstack1ll11l1l_opy_(CONFIG)
        bstack1lll1l1l1l_opy_ = bstack1l111ll11_opy_(bstack1l1l11l11_opy_)
        if bstack1lll1l1l1l_opy_:
            bstack1llll11l1_opy_ = update(bstack1lll1l1l1l_opy_, bstack1llll11l1_opy_)
        desired_capabilities = None
    if options:
        bstack1l1l1ll1l_opy_(options, bstack1llll11l1_opy_)
    if not options:
        options = bstack111lll1l1_opy_(bstack1llll11l1_opy_)
    if proxy and bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ᎌ")):
        options.proxy(proxy)
    if options and bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᎍ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11111ll11_opy_() < version.parse(bstack111_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᎎ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1llll11l1_opy_)
    logger.info(bstack11lll1l1l_opy_)
    if bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩᎏ")):
        bstack111l1llll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ᎐")):
        bstack111l1llll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ᎑")):
        bstack111l1llll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack111l1llll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack11l111111_opy_ = bstack111_opy_ (u"ࠬ࠭᎒")
        if bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧ᎓")):
            bstack11l111111_opy_ = self.caps.get(bstack111_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ᎔"))
        else:
            bstack11l111111_opy_ = self.capabilities.get(bstack111_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ᎕"))
        if bstack11l111111_opy_:
            if bstack11111ll11_opy_() <= version.parse(bstack111_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ᎖")):
                self.command_executor._url = bstack111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ᎗") + bstack1l1l1111_opy_ + bstack111_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ᎘")
            else:
                self.command_executor._url = bstack111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ᎙") + bstack11l111111_opy_ + bstack111_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢ᎚")
            logger.debug(bstack11l11l11l_opy_.format(bstack11l111111_opy_))
        else:
            logger.debug(bstack1lll1111l_opy_.format(bstack111_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣ᎛")))
    except Exception as e:
        logger.debug(bstack1lll1111l_opy_.format(e))
    bstack1llll111_opy_ = self.session_id
    if bstack111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ᎜") in bstack1lllllll11_opy_:
        threading.current_thread().bstack11ll111l_opy_ = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        bstack1111llll_opy_.bstack1l1lll1l1_opy_(self)
    bstack1ll1l11l_opy_.append(self)
    if bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᎝") in CONFIG and bstack111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ᎞") in CONFIG[bstack111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ᎟")][bstack1lll111l1l_opy_]:
        bstack1lll1111_opy_ = CONFIG[bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᎠ")][bstack1lll111l1l_opy_][bstack111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᎡ")]
    logger.debug(bstack1l1ll1l1_opy_.format(bstack1llll111_opy_))
def bstack11llll11l_opy_(self, url):
    global bstack1111l1lll_opy_
    global CONFIG
    try:
        bstack1l1l1l11_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1llll1l1l_opy_.format(str(err)))
    try:
        bstack1111l1lll_opy_(self, url)
    except Exception as e:
        try:
            bstack111lll1l_opy_ = str(e)
            if any(err_msg in bstack111lll1l_opy_ for err_msg in bstack1lll1l1ll1_opy_):
                bstack1l1l1l11_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1llll1l1l_opy_.format(str(err)))
        raise e
def bstack11ll1ll1l_opy_(item, when):
    global bstack1ll1ll1l_opy_
    try:
        bstack1ll1ll1l_opy_(item, when)
    except Exception as e:
        pass
def bstack1l111llll_opy_(item, call, rep):
    global bstack1111l1ll1_opy_
    global bstack1ll1l11l_opy_
    name = bstack111_opy_ (u"ࠧࠨᎢ")
    try:
        if rep.when == bstack111_opy_ (u"ࠨࡥࡤࡰࡱ࠭Ꭳ"):
            bstack1llll111_opy_ = threading.current_thread().bstack11ll111l_opy_
            bstack11ll11llll_opy_ = item.config.getoption(bstack111_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᎤ"))
            try:
                if (str(bstack11ll11llll_opy_).lower() != bstack111_opy_ (u"ࠪࡸࡷࡻࡥࠨᎥ")):
                    name = str(rep.nodeid)
                    bstack1l1ll1ll1_opy_ = bstack1ll1llllll_opy_(bstack111_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᎦ"), name, bstack111_opy_ (u"ࠬ࠭Ꭷ"), bstack111_opy_ (u"࠭ࠧᎨ"), bstack111_opy_ (u"ࠧࠨᎩ"), bstack111_opy_ (u"ࠨࠩᎪ"))
                    for driver in bstack1ll1l11l_opy_:
                        if bstack1llll111_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll1ll1_opy_)
            except Exception as e:
                logger.debug(bstack111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩᎫ").format(str(e)))
            try:
                status = bstack111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᎬ") if rep.outcome.lower() == bstack111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᎭ") else bstack111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᎮ")
                reason = bstack111_opy_ (u"࠭ࠧᎯ")
                if (reason != bstack111_opy_ (u"ࠢࠣᎰ")):
                    try:
                        if (threading.current_thread().bstackTestErrorMessages == None):
                            threading.current_thread().bstackTestErrorMessages = []
                    except Exception as e:
                        threading.current_thread().bstackTestErrorMessages = []
                    threading.current_thread().bstackTestErrorMessages.append(str(reason))
                if status == bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᎱ"):
                    reason = rep.longrepr.reprcrash.message
                    if (not threading.current_thread().bstackTestErrorMessages):
                        threading.current_thread().bstackTestErrorMessages = []
                    threading.current_thread().bstackTestErrorMessages.append(reason)
                level = bstack111_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᎲ") if status == bstack111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᎳ") else bstack111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᎴ")
                data = name + bstack111_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧᎵ") if status == bstack111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ꮆ") else name + bstack111_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠢࠢࠪᎷ") + reason
                bstack1ll1111l1_opy_ = bstack1ll1llllll_opy_(bstack111_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪᎸ"), bstack111_opy_ (u"ࠩࠪᎹ"), bstack111_opy_ (u"ࠪࠫᎺ"), bstack111_opy_ (u"ࠫࠬᎻ"), level, data)
                for driver in bstack1ll1l11l_opy_:
                    if bstack1llll111_opy_ == driver.session_id:
                        driver.execute_script(bstack1ll1111l1_opy_)
            except Exception as e:
                logger.debug(bstack111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡦࡳࡳࡺࡥࡹࡶࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩᎼ").format(str(e)))
    except Exception as e:
        logger.debug(bstack111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡶࡸࡦࡺࡥࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼࡿࠪᎽ").format(str(e)))
    bstack1111l1ll1_opy_(item, call, rep)
notset = Notset()
def bstack111l1lll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l11ll1ll_opy_
    if str(name).lower() == bstack111_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧᎾ"):
        return bstack111_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢᎿ")
    else:
        return bstack1l11ll1ll_opy_(self, name, default, skip)
def bstack1lllll11l1_opy_(self):
    global CONFIG
    global bstack1l1111111_opy_
    try:
        proxy = bstack1lll111111_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111_opy_ (u"ࠩ࠱ࡴࡦࡩࠧᏀ")):
                proxies = bstack11llll1l1_opy_(proxy, bstack1lll1ll111_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll11l1l1_opy_ = proxies.popitem()
                    if bstack111_opy_ (u"ࠥ࠾࠴࠵ࠢᏁ") in bstack1ll11l1l1_opy_:
                        return bstack1ll11l1l1_opy_
                    else:
                        return bstack111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᏂ") + bstack1ll11l1l1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤᏃ").format(str(e)))
    return bstack1l1111111_opy_(self)
def bstack1lll1l11l1_opy_():
    return bstack111_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᏄ") in CONFIG or bstack111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᏅ") in CONFIG and bstack11111ll11_opy_() >= version.parse(
        bstack11ll11l1l_opy_)
def bstack1111l111_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1lll1111_opy_
    global bstack1l11llll_opy_
    global bstack1lllllll11_opy_
    CONFIG[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᏆ")] = str(bstack1lllllll11_opy_) + str(__version__)
    bstack1lll111l1l_opy_ = 0
    try:
        if bstack1l11llll_opy_ is True:
            bstack1lll111l1l_opy_ = int(os.environ.get(bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᏇ")))
    except:
        bstack1lll111l1l_opy_ = 0
    CONFIG[bstack111_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᏈ")] = True
    bstack1llll11l1_opy_ = bstack1l111ll11_opy_(CONFIG, bstack1lll111l1l_opy_)
    logger.debug(bstack1lll11111l_opy_.format(str(bstack1llll11l1_opy_)))
    if CONFIG[bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᏉ")]:
        bstack1llll11lll_opy_(bstack1llll11l1_opy_, bstack1ll111ll1_opy_)
    if bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᏊ") in CONFIG and bstack111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᏋ") in CONFIG[bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᏌ")][bstack1lll111l1l_opy_]:
        bstack1lll1111_opy_ = CONFIG[bstack111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᏍ")][bstack1lll111l1l_opy_][bstack111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᏎ")]
    import urllib
    import json
    bstack1lllll1lll_opy_ = bstack111_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬᏏ") + urllib.parse.quote(json.dumps(bstack1llll11l1_opy_))
    browser = self.connect(bstack1lllll1lll_opy_)
    return browser
def bstack11111l111_opy_():
    global bstack1lll11l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1111l111_opy_
        bstack1lll11l1l_opy_ = True
    except Exception as e:
        pass
def bstack11ll1lll1l_opy_():
    global CONFIG
    global bstack1lllll1l1l_opy_
    global bstack1l1l1111_opy_
    global bstack1ll111ll1_opy_
    global bstack1l11llll_opy_
    CONFIG = json.loads(os.environ.get(bstack111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪᏐ")))
    bstack1lllll1l1l_opy_ = eval(os.environ.get(bstack111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭Ꮡ")))
    bstack1l1l1111_opy_ = os.environ.get(bstack111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭Ꮢ"))
    bstack1ll1l1111_opy_(CONFIG, bstack1lllll1l1l_opy_)
    bstack1lll111ll1_opy_()
    global bstack111l1llll_opy_
    global bstack11l111l11_opy_
    global bstack1llll1lll_opy_
    global bstack1ll1ll1lll_opy_
    global bstack1l1l1ll1_opy_
    global bstack1l1l11ll1_opy_
    global bstack1lll1l11_opy_
    global bstack1111l1lll_opy_
    global bstack1l1111111_opy_
    global bstack1l11ll1ll_opy_
    global bstack1ll1ll1l_opy_
    global bstack1111l1ll1_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack111l1llll_opy_ = webdriver.Remote.__init__
        bstack11l111l11_opy_ = WebDriver.quit
        bstack1lll1l11_opy_ = WebDriver.close
        bstack1111l1lll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if bstack111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᏓ") in CONFIG or bstack111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᏔ") in CONFIG:
        if bstack11111ll11_opy_() < version.parse(bstack11ll11l1l_opy_):
            logger.error(bstack11lll111l_opy_.format(bstack11111ll11_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1l1111111_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack1ll1ll1ll1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l11ll1ll_opy_ = Config.getoption
        from _pytest import runner
        bstack1ll1ll1l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11ll1l1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1111l1ll1_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack111_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪᏕ"))
    bstack1ll111ll1_opy_ = CONFIG.get(bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᏖ"), {}).get(bstack111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭Ꮧ"))
    bstack1l11llll_opy_ = True
    bstack1lllll11ll_opy_(bstack1ll1ll1111_opy_)
if (bstack1l1lllll11_opy_()):
    bstack11ll1lll1l_opy_()
@bstack1ll1111ll1_opy_(class_method=False)
def bstack11ll1ll111_opy_(hook_name, event, bstack11ll11lll1_opy_=None):
    if hook_name not in [bstack111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭Ꮨ"), bstack111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᏙ"), bstack111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭Ꮪ"), bstack111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᏛ"), bstack111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᏜ"), bstack111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᏝ"), bstack111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᏞ"), bstack111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧᏟ")]:
        return
    node = store[bstack111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᏠ")]
    if hook_name in [bstack111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭Ꮱ"), bstack111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᏢ")]:
        node = store[bstack111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨᏣ")]
    elif hook_name in [bstack111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᏤ"), bstack111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᏥ")]:
        node = store[bstack111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪᏦ")]
    if event == bstack111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭Ꮷ"):
        hook_type = bstack1l1l1111ll_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11lll11l1l_opy_ = {
            bstack111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᏨ"): uuid,
            bstack111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᏩ"): bstack1lllll111_opy_(),
            bstack111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᏪ"): bstack111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᏫ"),
            bstack111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᏬ"): hook_type,
            bstack111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨᏭ"): hook_name
        }
        store[bstack111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᏮ")].append(uuid)
        bstack11lll1l1ll_opy_ = node.nodeid
        if hook_type == bstack111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᏯ"):
            if not _11lll11l11_opy_.get(bstack11lll1l1ll_opy_, None):
                _11lll11l11_opy_[bstack11lll1l1ll_opy_] = {bstack111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᏰ"): []}
            _11lll11l11_opy_[bstack11lll1l1ll_opy_][bstack111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᏱ")].append(bstack11lll11l1l_opy_[bstack111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᏲ")])
        _11lll11l11_opy_[bstack11lll1l1ll_opy_ + bstack111_opy_ (u"ࠫ࠲࠭Ᏻ") + hook_name] = bstack11lll11l1l_opy_
        bstack11ll1l1111_opy_(node, bstack11lll11l1l_opy_, bstack111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭Ᏼ"))
    elif event == bstack111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᏵ"):
        bstack11ll1l11ll_opy_ = node.nodeid + bstack111_opy_ (u"ࠧ࠮ࠩ᏶") + hook_name
        _11lll11l11_opy_[bstack11ll1l11ll_opy_][bstack111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᏷")] = bstack1lllll111_opy_()
        bstack11ll1l1l11_opy_(_11lll11l11_opy_[bstack11ll1l11ll_opy_][bstack111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᏸ")])
        bstack11ll1l1111_opy_(node, _11lll11l11_opy_[bstack11ll1l11ll_opy_], bstack111_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᏹ"), bstack11lll1ll1l_opy_=bstack11ll11lll1_opy_)
def bstack11lll11lll_opy_():
    global bstack11lll111ll_opy_
    if bstack1l1lllll1_opy_():
        bstack11lll111ll_opy_ = bstack111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᏺ")
    else:
        bstack11lll111ll_opy_ = bstack111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᏻ")
@bstack1111llll_opy_.bstack11lllll111_opy_
def bstack11ll1l1ll1_opy_():
    bstack11lll11lll_opy_()
    if bstack1l1ll11l1l_opy_():
        bstack1l11l1llll_opy_(bstack11ll1llll1_opy_)
    bstack1l1l1lll11_opy_ = bstack1l1l1l1l1l_opy_(bstack11ll1ll111_opy_)
bstack11ll1l1ll1_opy_()