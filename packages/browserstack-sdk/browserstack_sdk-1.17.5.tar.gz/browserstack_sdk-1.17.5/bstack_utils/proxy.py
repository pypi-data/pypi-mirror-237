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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1l1l1l1l11_opy_
def bstack1l1l11l11l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1l1l11lll1_opy_(bstack1l1l11ll1l_opy_, bstack1l1l11l111_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1l1l11ll1l_opy_):
        with open(bstack1l1l11ll1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1l1l11l11l_opy_(bstack1l1l11ll1l_opy_):
        pac = get_pac(url=bstack1l1l11ll1l_opy_)
    else:
        raise Exception(bstack111_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬႺ").format(bstack1l1l11ll1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢႻ"), 80))
        bstack1l1l11l1l1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1l1l11l1l1_opy_ = bstack111_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨႼ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1l1l11l111_opy_, bstack1l1l11l1l1_opy_)
    return proxy_url
def bstack11llll11_opy_(config):
    return bstack111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫႽ") in config or bstack111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭Ⴞ") in config
def bstack1lll111111_opy_(config):
    if not bstack11llll11_opy_(config):
        return
    if config.get(bstack111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭Ⴟ")):
        return config.get(bstack111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧჀ"))
    if config.get(bstack111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩჁ")):
        return config.get(bstack111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪჂ"))
def bstack1lllll1ll_opy_(config, bstack1l1l11l111_opy_):
    proxy = bstack1lll111111_opy_(config)
    proxies = {}
    if config.get(bstack111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪჃ")) or config.get(bstack111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬჄ")):
        if proxy.endswith(bstack111_opy_ (u"ࠩ࠱ࡴࡦࡩࠧჅ")):
            proxies = bstack11llll1l1_opy_(proxy, bstack1l1l11l111_opy_)
        else:
            proxies = {
                bstack111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩ჆"): proxy
            }
    return proxies
def bstack11llll1l1_opy_(bstack1l1l11ll1l_opy_, bstack1l1l11l111_opy_):
    proxies = {}
    global bstack1l1l11l1ll_opy_
    if bstack111_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧჇ") in globals():
        return bstack1l1l11l1ll_opy_
    try:
        proxy = bstack1l1l11lll1_opy_(bstack1l1l11ll1l_opy_, bstack1l1l11l111_opy_)
        if bstack111_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧ჈") in proxy:
            proxies = {}
        elif bstack111_opy_ (u"ࠨࡈࡕࡖࡓࠦ჉") in proxy or bstack111_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨ჊") in proxy or bstack111_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢ჋") in proxy:
            bstack1l1l11ll11_opy_ = proxy.split(bstack111_opy_ (u"ࠤࠣࠦ჌"))
            if bstack111_opy_ (u"ࠥ࠾࠴࠵ࠢჍ") in bstack111_opy_ (u"ࠦࠧ჎").join(bstack1l1l11ll11_opy_[1:]):
                proxies = {
                    bstack111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫ჏"): bstack111_opy_ (u"ࠨࠢა").join(bstack1l1l11ll11_opy_[1:])
                }
            else:
                proxies = {
                    bstack111_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ბ"): str(bstack1l1l11ll11_opy_[0]).lower() + bstack111_opy_ (u"ࠣ࠼࠲࠳ࠧგ") + bstack111_opy_ (u"ࠤࠥდ").join(bstack1l1l11ll11_opy_[1:])
                }
        elif bstack111_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤე") in proxy:
            bstack1l1l11ll11_opy_ = proxy.split(bstack111_opy_ (u"ࠦࠥࠨვ"))
            if bstack111_opy_ (u"ࠧࡀ࠯࠰ࠤზ") in bstack111_opy_ (u"ࠨࠢთ").join(bstack1l1l11ll11_opy_[1:]):
                proxies = {
                    bstack111_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ი"): bstack111_opy_ (u"ࠣࠤკ").join(bstack1l1l11ll11_opy_[1:])
                }
            else:
                proxies = {
                    bstack111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨლ"): bstack111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦმ") + bstack111_opy_ (u"ࠦࠧნ").join(bstack1l1l11ll11_opy_[1:])
                }
        else:
            proxies = {
                bstack111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫო"): proxy
            }
    except Exception as e:
        print(bstack111_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥპ"), bstack1l1l1l1l11_opy_.format(bstack1l1l11ll1l_opy_, str(e)))
    bstack1l1l11l1ll_opy_ = proxies
    return proxies