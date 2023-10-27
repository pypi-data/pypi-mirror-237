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
import multiprocessing
import os
from browserstack_sdk.bstack1ll11l1ll_opy_ import *
from bstack_utils.helper import bstack1lll1ll1ll_opy_
from bstack_utils.messages import bstack11ll1l1l_opy_
from bstack_utils.constants import bstack1ll1ll1111_opy_
class bstack11ll1lll_opy_:
    def __init__(self, args, logger, bstack1ll11llll1_opy_, bstack1ll11lll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1ll11llll1_opy_ = bstack1ll11llll1_opy_
        self.bstack1ll11lll1l_opy_ = bstack1ll11lll1l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111l1111l_opy_ = []
        self.bstack1ll1l111l1_opy_ = None
        self.bstack1l11lllll_opy_ = []
        self.bstack1ll11lllll_opy_ = self.bstack1l1ll1l1l_opy_()
        self.bstack1l111l1l1_opy_ = -1
    def bstack1111l11l1_opy_(self, bstack1ll11ll111_opy_):
        self.parse_args()
        self.bstack1ll11l1lll_opy_()
        self.bstack1ll11ll1ll_opy_(bstack1ll11ll111_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack1ll11ll1l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l111l1l1_opy_ = -1
        if bstack111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ಍") in self.bstack1ll11llll1_opy_:
            self.bstack1l111l1l1_opy_ = self.bstack1ll11llll1_opy_[bstack111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨಎ")]
        try:
            bstack1ll11ll11l_opy_ = [bstack111_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫಏ"), bstack111_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭ಐ"), bstack111_opy_ (u"ࠫ࠲ࡶࠧ಑")]
            if self.bstack1l111l1l1_opy_ >= 0:
                bstack1ll11ll11l_opy_.extend([bstack111_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ಒ"), bstack111_opy_ (u"࠭࠭࡯ࠩಓ")])
            for arg in bstack1ll11ll11l_opy_:
                self.bstack1ll11ll1l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1ll11l1lll_opy_(self):
        bstack1ll1l111l1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1ll1l111l1_opy_ = bstack1ll1l111l1_opy_
        return bstack1ll1l111l1_opy_
    def bstack1l11ll111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack1ll1l1111l_opy_ = importlib.find_loader(bstack111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩಔ"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11ll1l1l_opy_)
    def bstack1ll11ll1ll_opy_(self, bstack1ll11ll111_opy_):
        if bstack1ll11ll111_opy_:
            self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಕ"))
            self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"ࠩࡗࡶࡺ࡫ࠧಖ"))
        self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"ࠪ࠱ࡵ࠭ಗ"))
        self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠩಘ"))
        self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧಙ"))
        self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ಚ"))
        if self.bstack1l111l1l1_opy_ > 1:
            self.bstack1ll1l111l1_opy_.append(bstack111_opy_ (u"ࠧ࠮ࡰࠪಛ"))
            self.bstack1ll1l111l1_opy_.append(str(self.bstack1l111l1l1_opy_))
    def bstack1ll1l11111_opy_(self):
        bstack1l11lllll_opy_ = []
        for spec in self.bstack111l1111l_opy_:
            bstack1lllll1ll1_opy_ = [spec]
            bstack1lllll1ll1_opy_ += self.bstack1ll1l111l1_opy_
            bstack1l11lllll_opy_.append(bstack1lllll1ll1_opy_)
        self.bstack1l11lllll_opy_ = bstack1l11lllll_opy_
        return bstack1l11lllll_opy_
    def bstack1l1ll1l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1ll11lllll_opy_ = True
            return True
        except Exception as e:
            self.bstack1ll11lllll_opy_ = False
        return self.bstack1ll11lllll_opy_
    def bstack1l1lll1ll_opy_(self, bstack1ll11lll11_opy_, bstack1111l11l1_opy_):
        bstack1111l11l1_opy_[bstack111_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨಜ")] = self.bstack1ll11llll1_opy_
        if bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಝ") in self.bstack1ll11llll1_opy_:
            bstack1llll1l1ll_opy_ = []
            manager = multiprocessing.Manager()
            bstack11l11l1ll_opy_ = manager.list()
            for index, platform in enumerate(self.bstack1ll11llll1_opy_[bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಞ")]):
                bstack1llll1l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack1ll11lll11_opy_,
                                                           args=(self.bstack1ll1l111l1_opy_, bstack1111l11l1_opy_)))
            i = 0
            for t in bstack1llll1l1ll_opy_:
                os.environ[bstack111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫಟ")] = str(i)
                i += 1
                t.start()
            for t in bstack1llll1l1ll_opy_:
                t.join()
            return bstack11l11l1ll_opy_