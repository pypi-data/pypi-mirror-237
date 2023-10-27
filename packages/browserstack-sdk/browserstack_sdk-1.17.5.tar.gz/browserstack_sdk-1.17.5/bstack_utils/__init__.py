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