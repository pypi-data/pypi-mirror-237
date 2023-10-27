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
import sys
class bstack1ll11l11l1_opy_:
    def __init__(self, handler):
        self._1ll11l11ll_opy_ = sys.stdout.write
        self._1ll11l1l11_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack1ll11l1ll1_opy_
        sys.stdout.error = self.bstack1ll11l1l1l_opy_
    def bstack1ll11l1ll1_opy_(self, _str):
        self._1ll11l11ll_opy_(_str)
        if self.handler:
            self.handler({bstack111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫಠ"): bstack111_opy_ (u"࠭ࡉࡏࡈࡒࠫಡ"), bstack111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨಢ"): _str})
    def bstack1ll11l1l1l_opy_(self, _str):
        self._1ll11l1l11_opy_(_str)
        if self.handler:
            self.handler({bstack111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧಣ"): bstack111_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨತ"), bstack111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫಥ"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._1ll11l11ll_opy_
        sys.stderr.write = self._1ll11l1l11_opy_