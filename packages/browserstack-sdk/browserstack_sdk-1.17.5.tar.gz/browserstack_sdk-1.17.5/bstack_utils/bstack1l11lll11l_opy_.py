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
import threading
bstack1l11ll1ll1_opy_ = 1000
bstack1l11lll1l1_opy_ = 5
bstack1l11ll1lll_opy_ = 30
bstack1l11ll111l_opy_ = 2
class bstack1l11ll11l1_opy_:
    def __init__(self, handler, bstack1l11lll1ll_opy_=bstack1l11ll1ll1_opy_, bstack1l11llll11_opy_=bstack1l11lll1l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1l11lll1ll_opy_ = bstack1l11lll1ll_opy_
        self.bstack1l11llll11_opy_ = bstack1l11llll11_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack1l11ll1l1l_opy_()
    def bstack1l11ll1l1l_opy_(self):
        self.timer = threading.Timer(self.bstack1l11llll11_opy_, self.bstack1l11lll111_opy_)
        self.timer.start()
    def bstack1l11ll11ll_opy_(self):
        self.timer.cancel()
    def bstack1l11ll1l11_opy_(self):
        self.bstack1l11ll11ll_opy_()
        self.bstack1l11ll1l1l_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1l11lll1ll_opy_:
                t = threading.Thread(target=self.bstack1l11lll111_opy_)
                t.start()
                self.bstack1l11ll1l11_opy_()
    def bstack1l11lll111_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack1l11lll1ll_opy_]
        del self.queue[:self.bstack1l11lll1ll_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1l11ll11ll_opy_()
        while len(self.queue) > 0:
            self.bstack1l11lll111_opy_()