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
class bstack1l11l1llll_opy_:
    def __init__(self, handler):
        self._1l11l1l1ll_opy_ = None
        self.handler = handler
        self._1l11l1ll11_opy_ = self.bstack1l11l1lll1_opy_()
        self.patch()
    def patch(self):
        self._1l11l1l1ll_opy_ = self._1l11l1ll11_opy_.execute
        self._1l11l1ll11_opy_.execute = self.bstack1l11ll1111_opy_()
    def bstack1l11ll1111_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            response = self._1l11l1l1ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(driver_command, response)
            return response
        return execute
    def reset(self):
        self._1l11l1ll11_opy_.execute = self._1l11l1l1ll_opy_
    @staticmethod
    def bstack1l11l1lll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver