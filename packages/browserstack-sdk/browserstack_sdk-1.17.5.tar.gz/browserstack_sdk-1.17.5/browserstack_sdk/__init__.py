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
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from bstack_utils.constants import *
import time
import requests
def bstack11111l11l_opy_():
  global CONFIG
  headers = {
        bstack111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡵ"): bstack111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡶ"),
      }
  proxies = bstack1lllll1ll_opy_(CONFIG, bstack111lll111_opy_)
  try:
    response = requests.get(bstack111lll111_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1lllll_opy_ = response.json()[bstack111_opy_ (u"ࠫ࡭ࡻࡢࡴࠩࡷ")]
      logger.debug(bstack11l1llll1_opy_.format(response.json()))
      return bstack1l1lllll_opy_
    else:
      logger.debug(bstack1lllllll1l_opy_.format(bstack111_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦࡸ")))
  except Exception as e:
    logger.debug(bstack1lllllll1l_opy_.format(e))
def bstack11ll1111l_opy_(hub_url):
  global CONFIG
  url = bstack111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣࡹ")+  hub_url + bstack111_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢࡺ")
  headers = {
        bstack111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧࡻ"): bstack111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬࡼ"),
      }
  proxies = bstack1lllll1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11l111l1l_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11ll1ll11_opy_.format(hub_url, e))
def bstack1lll1111l1_opy_():
  try:
    global bstack1l1l1111_opy_
    bstack1l1lllll_opy_ = bstack11111l11l_opy_()
    bstack1lll11l1_opy_ = []
    results = []
    for bstack111lll1ll_opy_ in bstack1l1lllll_opy_:
      bstack1lll11l1_opy_.append(bstack1ll1l111l_opy_(target=bstack11ll1111l_opy_,args=(bstack111lll1ll_opy_,)))
    for t in bstack1lll11l1_opy_:
      t.start()
    for t in bstack1lll11l1_opy_:
      results.append(t.join())
    bstack1llllll1l1_opy_ = {}
    for item in results:
      hub_url = item[bstack111_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫࡽ")]
      latency = item[bstack111_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬࡾ")]
      bstack1llllll1l1_opy_[hub_url] = latency
    bstack111l1l1l1_opy_ = min(bstack1llllll1l1_opy_, key= lambda x: bstack1llllll1l1_opy_[x])
    bstack1l1l1111_opy_ = bstack111l1l1l1_opy_
    logger.debug(bstack1l1111ll_opy_.format(bstack111l1l1l1_opy_))
  except Exception as e:
    logger.debug(bstack111llll11_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils.config import Config
from bstack_utils.helper import bstack1l1l1111l_opy_, bstack11l111ll1_opy_, bstack111ll11ll_opy_, Notset, bstack1ll11l1l_opy_, \
  bstack1llll1ll11_opy_, bstack1lll111l_opy_, bstack1lll1llll_opy_, bstack11l1l1ll_opy_, bstack1l1lllll1_opy_
from bstack_utils.bstack1ll1l11lll_opy_ import bstack1111llll_opy_
from bstack_utils.proxy import bstack11llll1l1_opy_, bstack1lllll1ll_opy_, bstack1lll111111_opy_, bstack11llll11_opy_
from browserstack_sdk.bstack11ll1111_opy_ import *
from browserstack_sdk.bstack1ll11l1ll_opy_ import *
bstack111l11l1l_opy_ = bstack111_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬࡿ")
bstack1lll1ll11l_opy_ = bstack111_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬࢀ")
from ._version import __version__
bstack1111ll111_opy_ = None
CONFIG = {}
bstack1ll1llll1l_opy_ = {}
bstack1llllll1l_opy_ = {}
bstack1llll111_opy_ = None
bstack11l1l1ll1_opy_ = None
bstack1lll1111_opy_ = None
bstack1lll1l1111_opy_ = -1
bstack1ll1l1l11_opy_ = bstack1lll11l111_opy_
bstack1ll1llll_opy_ = 1
bstack1l11llll_opy_ = False
bstack1111l11ll_opy_ = False
bstack1lllllll11_opy_ = bstack111_opy_ (u"ࠧࠨࢁ")
bstack1ll111ll1_opy_ = bstack111_opy_ (u"ࠨࠩࢂ")
bstack1lllll1l1l_opy_ = False
bstack111l11l11_opy_ = True
bstack1l1l1lll_opy_ = bstack111_opy_ (u"ࠩࠪࢃ")
bstack1ll1l11l_opy_ = []
bstack1l1l1111_opy_ = bstack111_opy_ (u"ࠪࠫࢄ")
bstack1lll11l1l_opy_ = False
bstack1llll11111_opy_ = None
bstack1ll111l11_opy_ = None
bstack1l111l1l_opy_ = -1
bstack1l11111ll_opy_ = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠫࢃ࠭ࢅ")), bstack111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬࢆ"), bstack111_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫࢇ"))
bstack1l1111ll1_opy_ = []
bstack1l1ll11ll_opy_ = []
bstack1l1ll1l11_opy_ = False
bstack11l1l1lll_opy_ = False
bstack111l1llll_opy_ = None
bstack11l111l11_opy_ = None
bstack1ll1l111_opy_ = None
bstack1l1l1l1l1_opy_ = None
bstack1111l1l1_opy_ = None
bstack1llll1lll_opy_ = None
bstack1ll1ll1lll_opy_ = None
bstack111ll1ll_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack1l1111111_opy_ = None
bstack1lll1l11_opy_ = None
bstack1111l1lll_opy_ = None
bstack1l11l1l11_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack1ll1ll1l_opy_ = None
bstack1lll11llll_opy_ = None
bstack1111l1ll1_opy_ = None
bstack11111l11_opy_ = bstack111_opy_ (u"ࠢࠣ࢈")
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1ll1l1l11_opy_,
                    format=bstack111_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ࢉ"),
                    datefmt=bstack111_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫࢊ"),
                    stream=sys.stdout)
bstack1l11ll11l_opy_ = Config.get_instance()
def bstack1lll111ll1_opy_():
  global CONFIG
  global bstack1ll1l1l11_opy_
  if bstack111_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬࢋ") in CONFIG:
    bstack1ll1l1l11_opy_ = bstack11l1lllll_opy_[CONFIG[bstack111_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ࢌ")]]
    logging.getLogger().setLevel(bstack1ll1l1l11_opy_)
def bstack1l1llll1l_opy_():
  global CONFIG
  global bstack1l1ll1l11_opy_
  bstack11lll1l1_opy_ = bstack11l1l1l1_opy_(CONFIG)
  if (bstack111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࢍ") in bstack11lll1l1_opy_ and str(bstack11lll1l1_opy_[bstack111_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࢎ")]).lower() == bstack111_opy_ (u"ࠧࡵࡴࡸࡩࠬ࢏")):
    bstack1l1ll1l11_opy_ = True
def bstack11ll1l1l1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11111ll11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1lll1ll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ࢐") == args[i].lower() or bstack111_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ࢑") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1l1lll_opy_
      bstack1l1l1lll_opy_ += bstack111_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ࢒") + path
      return path
  return None
bstack1llll1l1_opy_ = re.compile(bstack111_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ࢓"))
def bstack111l1l11_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1llll1l1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111_opy_ (u"ࠧࠪࡻࠣ࢔") + group + bstack111_opy_ (u"ࠨࡽࠣ࢕"), os.environ.get(group))
  return value
def bstack1ll11l11_opy_():
  bstack111l111l1_opy_ = bstack1lll1ll1_opy_()
  if bstack111l111l1_opy_ and os.path.exists(os.path.abspath(bstack111l111l1_opy_)):
    fileName = bstack111l111l1_opy_
  if bstack111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢖") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࢗ")])) and not bstack111_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ࢘") in locals():
    fileName = os.environ[bstack111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")]
  if bstack111_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    bstack1llll1_opy_ = os.path.abspath(fileName)
  else:
    bstack1llll1_opy_ = bstack111_opy_ (u"࢛ࠬ࠭")
  bstack111111lll_opy_ = os.getcwd()
  bstack1l11lll11_opy_ = bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ࢜")
  bstack1l11111l1_opy_ = bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ࢝")
  while (not os.path.exists(bstack1llll1_opy_)) and bstack111111lll_opy_ != bstack111_opy_ (u"ࠣࠤ࢞"):
    bstack1llll1_opy_ = os.path.join(bstack111111lll_opy_, bstack1l11lll11_opy_)
    if not os.path.exists(bstack1llll1_opy_):
      bstack1llll1_opy_ = os.path.join(bstack111111lll_opy_, bstack1l11111l1_opy_)
    if bstack111111lll_opy_ != os.path.dirname(bstack111111lll_opy_):
      bstack111111lll_opy_ = os.path.dirname(bstack111111lll_opy_)
    else:
      bstack111111lll_opy_ = bstack111_opy_ (u"ࠤࠥ࢟")
  if not os.path.exists(bstack1llll1_opy_):
    bstack11l1l11l_opy_(
      bstack11111ll1_opy_.format(os.getcwd()))
  try:
    with open(bstack1llll1_opy_, bstack111_opy_ (u"ࠪࡶࠬࢠ")) as stream:
      yaml.add_implicit_resolver(bstack111_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧࢡ"), bstack1llll1l1_opy_)
      yaml.add_constructor(bstack111_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࢢ"), bstack111l1l11_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1llll1_opy_, bstack111_opy_ (u"࠭ࡲࠨࢣ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack11l1l11l_opy_(bstack11111111l_opy_.format(str(exc)))
def bstack11lll11l_opy_(config):
  bstack11l1ll1ll_opy_ = bstack11l1l1111_opy_(config)
  for option in list(bstack11l1ll1ll_opy_):
    if option.lower() in bstack1ll111111_opy_ and option != bstack1ll111111_opy_[option.lower()]:
      bstack11l1ll1ll_opy_[bstack1ll111111_opy_[option.lower()]] = bstack11l1ll1ll_opy_[option]
      del bstack11l1ll1ll_opy_[option]
  return config
def bstack1ll111l1l_opy_():
  global bstack1llllll1l_opy_
  for key, bstack11ll11111_opy_ in bstack1ll1l1ll1_opy_.items():
    if isinstance(bstack11ll11111_opy_, list):
      for var in bstack11ll11111_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1llllll1l_opy_[key] = os.environ[var]
          break
    elif bstack11ll11111_opy_ in os.environ and os.environ[bstack11ll11111_opy_] and str(os.environ[bstack11ll11111_opy_]).strip():
      bstack1llllll1l_opy_[key] = os.environ[bstack11ll11111_opy_]
  if bstack111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩࢤ") in os.environ:
    bstack1llllll1l_opy_[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢥ")] = {}
    bstack1llllll1l_opy_[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢦ")][bstack111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢧ")] = os.environ[bstack111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ")]
def bstack111l111ll_opy_():
  global bstack1ll1llll1l_opy_
  global bstack1l1l1lll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack111_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࢩ").lower() == val.lower():
      bstack1ll1llll1l_opy_[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")] = {}
      bstack1ll1llll1l_opy_[bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢫ")][bstack111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢬ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack11l1ll1l1_opy_ in bstack1l1lll1l_opy_.items():
    if isinstance(bstack11l1ll1l1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack11l1ll1l1_opy_:
          if idx < len(sys.argv) and bstack111_opy_ (u"ࠩ࠰࠱ࠬࢭ") + var.lower() == val.lower() and not key in bstack1ll1llll1l_opy_:
            bstack1ll1llll1l_opy_[key] = sys.argv[idx + 1]
            bstack1l1l1lll_opy_ += bstack111_opy_ (u"ࠪࠤ࠲࠳ࠧࢮ") + var + bstack111_opy_ (u"ࠫࠥ࠭ࢯ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack111_opy_ (u"ࠬ࠳࠭ࠨࢰ") + bstack11l1ll1l1_opy_.lower() == val.lower() and not key in bstack1ll1llll1l_opy_:
          bstack1ll1llll1l_opy_[key] = sys.argv[idx + 1]
          bstack1l1l1lll_opy_ += bstack111_opy_ (u"࠭ࠠ࠮࠯ࠪࢱ") + bstack11l1ll1l1_opy_ + bstack111_opy_ (u"ࠧࠡࠩࢲ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1l1l1l1ll_opy_(config):
  bstack1lll11ll1_opy_ = config.keys()
  for bstack1lll1lllll_opy_, bstack11111lll1_opy_ in bstack1l11l1l1_opy_.items():
    if bstack11111lll1_opy_ in bstack1lll11ll1_opy_:
      config[bstack1lll1lllll_opy_] = config[bstack11111lll1_opy_]
      del config[bstack11111lll1_opy_]
  for bstack1lll1lllll_opy_, bstack11111lll1_opy_ in bstack111llll1_opy_.items():
    if isinstance(bstack11111lll1_opy_, list):
      for bstack1l1l1llll_opy_ in bstack11111lll1_opy_:
        if bstack1l1l1llll_opy_ in bstack1lll11ll1_opy_:
          config[bstack1lll1lllll_opy_] = config[bstack1l1l1llll_opy_]
          del config[bstack1l1l1llll_opy_]
          break
    elif bstack11111lll1_opy_ in bstack1lll11ll1_opy_:
      config[bstack1lll1lllll_opy_] = config[bstack11111lll1_opy_]
      del config[bstack11111lll1_opy_]
  for bstack1l1l1llll_opy_ in list(config):
    for bstack1l1111l11_opy_ in bstack11lll1lll_opy_:
      if bstack1l1l1llll_opy_.lower() == bstack1l1111l11_opy_.lower() and bstack1l1l1llll_opy_ != bstack1l1111l11_opy_:
        config[bstack1l1111l11_opy_] = config[bstack1l1l1llll_opy_]
        del config[bstack1l1l1llll_opy_]
  bstack1l11llll1_opy_ = []
  if bstack111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫࢳ") in config:
    bstack1l11llll1_opy_ = config[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢴ")]
  for platform in bstack1l11llll1_opy_:
    for bstack1l1l1llll_opy_ in list(platform):
      for bstack1l1111l11_opy_ in bstack11lll1lll_opy_:
        if bstack1l1l1llll_opy_.lower() == bstack1l1111l11_opy_.lower() and bstack1l1l1llll_opy_ != bstack1l1111l11_opy_:
          platform[bstack1l1111l11_opy_] = platform[bstack1l1l1llll_opy_]
          del platform[bstack1l1l1llll_opy_]
  for bstack1lll1lllll_opy_, bstack11111lll1_opy_ in bstack111llll1_opy_.items():
    for platform in bstack1l11llll1_opy_:
      if isinstance(bstack11111lll1_opy_, list):
        for bstack1l1l1llll_opy_ in bstack11111lll1_opy_:
          if bstack1l1l1llll_opy_ in platform:
            platform[bstack1lll1lllll_opy_] = platform[bstack1l1l1llll_opy_]
            del platform[bstack1l1l1llll_opy_]
            break
      elif bstack11111lll1_opy_ in platform:
        platform[bstack1lll1lllll_opy_] = platform[bstack11111lll1_opy_]
        del platform[bstack11111lll1_opy_]
  for bstack11lllllll_opy_ in bstack1llllllll1_opy_:
    if bstack11lllllll_opy_ in config:
      if not bstack1llllllll1_opy_[bstack11lllllll_opy_] in config:
        config[bstack1llllllll1_opy_[bstack11lllllll_opy_]] = {}
      config[bstack1llllllll1_opy_[bstack11lllllll_opy_]].update(config[bstack11lllllll_opy_])
      del config[bstack11lllllll_opy_]
  for platform in bstack1l11llll1_opy_:
    for bstack11lllllll_opy_ in bstack1llllllll1_opy_:
      if bstack11lllllll_opy_ in list(platform):
        if not bstack1llllllll1_opy_[bstack11lllllll_opy_] in platform:
          platform[bstack1llllllll1_opy_[bstack11lllllll_opy_]] = {}
        platform[bstack1llllllll1_opy_[bstack11lllllll_opy_]].update(platform[bstack11lllllll_opy_])
        del platform[bstack11lllllll_opy_]
  config = bstack11lll11l_opy_(config)
  return config
def bstack1l1ll11l1_opy_(config):
  global bstack1ll111ll1_opy_
  if bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧࢵ") in config and str(config[bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࢶ")]).lower() != bstack111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫࢷ"):
    if not bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢸ") in config:
      config[bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢹ")] = {}
    if not bstack111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢺ") in config[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢻ")]:
      bstack1lllll111_opy_ = datetime.datetime.now()
      bstack1l1llll1_opy_ = bstack1lllll111_opy_.strftime(bstack111_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧࢼ"))
      hostname = socket.gethostname()
      bstack1ll1l1lll1_opy_ = bstack111_opy_ (u"ࠫࠬࢽ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧࢾ").format(bstack1l1llll1_opy_, hostname, bstack1ll1l1lll1_opy_)
      config[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢿ")][bstack111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣀ")] = identifier
    bstack1ll111ll1_opy_ = config[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣁ")][bstack111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣂ")]
  return config
def bstack111l11lll_opy_():
  bstack1lllll11l_opy_ =  bstack11l1l1ll_opy_()[bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩࣃ")]
  return bstack1lllll11l_opy_ if bstack1lllll11l_opy_ else -1
def bstack11111l1l_opy_(bstack1lllll11l_opy_):
  global CONFIG
  if not bstack111_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣄ") in CONFIG[bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣅ")]:
    return
  CONFIG[bstack111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")] = CONFIG[bstack111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣇ")].replace(
    bstack111_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣈ"),
    str(bstack1lllll11l_opy_)
  )
def bstack11ll111ll_opy_():
  global CONFIG
  if not bstack111_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨࣉ") in CONFIG[bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")]:
    return
  bstack1lllll111_opy_ = datetime.datetime.now()
  bstack1l1llll1_opy_ = bstack1lllll111_opy_.strftime(bstack111_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ࣋"))
  CONFIG[bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣌")] = CONFIG[bstack111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣍")].replace(
    bstack111_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭࣎"),
    bstack1l1llll1_opy_
  )
def bstack1l11l111l_opy_():
  global CONFIG
  if bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࣏ࠪ") in CONFIG and not bool(CONFIG[bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")]):
    del CONFIG[bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")]
    return
  if not bstack111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭") in CONFIG:
    CONFIG[bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ")] = bstack111_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩࣔ")
  if bstack111_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭ࣕ") in CONFIG[bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ")]:
    bstack11ll111ll_opy_()
    os.environ[bstack111_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ࣗ")] = CONFIG[bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣘ")]
  if not bstack111_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣙ") in CONFIG[bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]:
    return
  bstack1lllll11l_opy_ = bstack111_opy_ (u"࠭ࠧࣛ")
  bstack11l1l1l11_opy_ = bstack111l11lll_opy_()
  if bstack11l1l1l11_opy_ != -1:
    bstack1lllll11l_opy_ = bstack111_opy_ (u"ࠧࡄࡋࠣࠫࣜ") + str(bstack11l1l1l11_opy_)
  if bstack1lllll11l_opy_ == bstack111_opy_ (u"ࠨࠩࣝ"):
    bstack111llll1l_opy_ = bstack1ll1lll11_opy_(CONFIG[bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬࣞ")])
    if bstack111llll1l_opy_ != -1:
      bstack1lllll11l_opy_ = str(bstack111llll1l_opy_)
  if bstack1lllll11l_opy_:
    bstack11111l1l_opy_(bstack1lllll11l_opy_)
    os.environ[bstack111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧࣟ")] = CONFIG[bstack111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣠")]
def bstack1l1l111l1_opy_(bstack1111ll11_opy_, bstack1lll11lll_opy_, path):
  bstack1lllllll1_opy_ = {
    bstack111_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣡"): bstack1lll11lll_opy_
  }
  if os.path.exists(path):
    bstack11llll1l_opy_ = json.load(open(path, bstack111_opy_ (u"࠭ࡲࡣࠩ࣢")))
  else:
    bstack11llll1l_opy_ = {}
  bstack11llll1l_opy_[bstack1111ll11_opy_] = bstack1lllllll1_opy_
  with open(path, bstack111_opy_ (u"ࠢࡸࣣ࠭ࠥ")) as outfile:
    json.dump(bstack11llll1l_opy_, outfile)
def bstack1ll1lll11_opy_(bstack1111ll11_opy_):
  bstack1111ll11_opy_ = str(bstack1111ll11_opy_)
  bstack111111111_opy_ = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠨࢀࠪࣤ")), bstack111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩࣥ"))
  try:
    if not os.path.exists(bstack111111111_opy_):
      os.makedirs(bstack111111111_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠪࢂࣦࠬ")), bstack111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫࣧ"), bstack111_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧࣨ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111_opy_ (u"࠭ࡷࠨࣩ")):
        pass
      with open(file_path, bstack111_opy_ (u"ࠢࡸ࠭ࠥ࣪")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111_opy_ (u"ࠨࡴࠪ࣫")) as bstack1llll11l_opy_:
      bstack111lllll1_opy_ = json.load(bstack1llll11l_opy_)
    if bstack1111ll11_opy_ in bstack111lllll1_opy_:
      bstack111111ll_opy_ = bstack111lllll1_opy_[bstack1111ll11_opy_][bstack111_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣬")]
      bstack111ll11l_opy_ = int(bstack111111ll_opy_) + 1
      bstack1l1l111l1_opy_(bstack1111ll11_opy_, bstack111ll11l_opy_, file_path)
      return bstack111ll11l_opy_
    else:
      bstack1l1l111l1_opy_(bstack1111ll11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack111l1l1ll_opy_.format(str(e)))
    return -1
def bstack11l111ll_opy_(config):
  if not config[bstack111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ࣭ࠬ")] or not config[bstack111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿ࣮ࠧ")]:
    return True
  else:
    return False
def bstack1ll11lll1_opy_(config, index=0):
  global bstack1lllll1l1l_opy_
  bstack11ll1l111_opy_ = {}
  caps = bstack111l1ll11_opy_ + bstack1lll111l11_opy_
  if bstack1lllll1l1l_opy_:
    caps += bstack1l111lll1_opy_
  for key in config:
    if key in caps + [bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࣯")]:
      continue
    bstack11ll1l111_opy_[key] = config[key]
  if bstack111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࣰࠩ") in config:
    for bstack1111111l_opy_ in config[bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ")][index]:
      if bstack1111111l_opy_ in caps + [bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣲ࠭"), bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪࣳ")]:
        continue
      bstack11ll1l111_opy_[bstack1111111l_opy_] = config[bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ")][index][bstack1111111l_opy_]
  bstack11ll1l111_opy_[bstack111_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࣵ")] = socket.gethostname()
  if bstack111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࣶ࠭") in bstack11ll1l111_opy_:
    del (bstack11ll1l111_opy_[bstack111_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࣷ")])
  return bstack11ll1l111_opy_
def bstack1111lllll_opy_(config):
  global bstack1lllll1l1l_opy_
  bstack1ll11111_opy_ = {}
  caps = bstack1lll111l11_opy_
  if bstack1lllll1l1l_opy_:
    caps += bstack1l111lll1_opy_
  for key in caps:
    if key in config:
      bstack1ll11111_opy_[key] = config[key]
  return bstack1ll11111_opy_
def bstack1ll1l1l111_opy_(bstack11ll1l111_opy_, bstack1ll11111_opy_):
  bstack1ll11llll_opy_ = {}
  for key in bstack11ll1l111_opy_.keys():
    if key in bstack1l11l1l1_opy_:
      bstack1ll11llll_opy_[bstack1l11l1l1_opy_[key]] = bstack11ll1l111_opy_[key]
    else:
      bstack1ll11llll_opy_[key] = bstack11ll1l111_opy_[key]
  for key in bstack1ll11111_opy_:
    if key in bstack1l11l1l1_opy_:
      bstack1ll11llll_opy_[bstack1l11l1l1_opy_[key]] = bstack1ll11111_opy_[key]
    else:
      bstack1ll11llll_opy_[key] = bstack1ll11111_opy_[key]
  return bstack1ll11llll_opy_
def bstack1l111ll11_opy_(config, index=0):
  global bstack1lllll1l1l_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack1ll11111_opy_ = bstack1111lllll_opy_(config)
  bstack1lll1l111_opy_ = bstack1lll111l11_opy_
  bstack1lll1l111_opy_ += bstack1l111111l_opy_
  if bstack1lllll1l1l_opy_:
    bstack1lll1l111_opy_ += bstack1l111lll1_opy_
  if bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣸ") in config:
    if bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣹ࠭") in config[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࣺࠬ")][index]:
      caps[bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࣻ")] = config[bstack111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ")][index][bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ")]
    if bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧࣾ") in config[bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣿ")][index]:
      caps[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऀ")] = str(config[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬँ")][index][bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं")])
    bstack1lll11ll_opy_ = {}
    for bstack11l11l111_opy_ in bstack1lll1l111_opy_:
      if bstack11l11l111_opy_ in config[bstack111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index]:
        if bstack11l11l111_opy_ == bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧऄ"):
          try:
            bstack1lll11ll_opy_[bstack11l11l111_opy_] = str(config[bstack111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index][bstack11l11l111_opy_] * 1.0)
          except:
            bstack1lll11ll_opy_[bstack11l11l111_opy_] = str(config[bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪआ")][index][bstack11l11l111_opy_])
        else:
          bstack1lll11ll_opy_[bstack11l11l111_opy_] = config[bstack111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack11l11l111_opy_]
        del (config[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack11l11l111_opy_])
    bstack1ll11111_opy_ = update(bstack1ll11111_opy_, bstack1lll11ll_opy_)
  bstack11ll1l111_opy_ = bstack1ll11lll1_opy_(config, index)
  for bstack1l1l1llll_opy_ in bstack1lll111l11_opy_ + [bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨउ"), bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬऊ")]:
    if bstack1l1l1llll_opy_ in bstack11ll1l111_opy_:
      bstack1ll11111_opy_[bstack1l1l1llll_opy_] = bstack11ll1l111_opy_[bstack1l1l1llll_opy_]
      del (bstack11ll1l111_opy_[bstack1l1l1llll_opy_])
  if bstack1ll11l1l_opy_(config):
    bstack11ll1l111_opy_[bstack111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬऋ")] = True
    caps.update(bstack1ll11111_opy_)
    caps[bstack111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧऌ")] = bstack11ll1l111_opy_
  else:
    bstack11ll1l111_opy_[bstack111_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧऍ")] = False
    caps.update(bstack1ll1l1l111_opy_(bstack11ll1l111_opy_, bstack1ll11111_opy_))
    if bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ऎ") in caps:
      caps[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪए")] = caps[bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨऐ")]
      del (caps[bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऑ")])
    if bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऒ") in caps:
      caps[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨओ")] = caps[bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨऔ")]
      del (caps[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩक")])
  return caps
def bstack1lll1ll111_opy_():
  global bstack1l1l1111_opy_
  if bstack11111ll11_opy_() <= version.parse(bstack111_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩख")):
    if bstack1l1l1111_opy_ != bstack111_opy_ (u"ࠪࠫग"):
      return bstack111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧघ") + bstack1l1l1111_opy_ + bstack111_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤङ")
    return bstack1l111ll1l_opy_
  if bstack1l1l1111_opy_ != bstack111_opy_ (u"࠭ࠧच"):
    return bstack111_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤछ") + bstack1l1l1111_opy_ + bstack111_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤज")
  return bstack1lll111ll_opy_
def bstack1lll1l1ll_opy_(options):
  return hasattr(options, bstack111_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪझ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11ll1lll1_opy_(options, bstack11l11l1l1_opy_):
  for bstack11111l1l1_opy_ in bstack11l11l1l1_opy_:
    if bstack11111l1l1_opy_ in [bstack111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨञ"), bstack111_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨट")]:
      continue
    if bstack11111l1l1_opy_ in options._experimental_options:
      options._experimental_options[bstack11111l1l1_opy_] = update(options._experimental_options[bstack11111l1l1_opy_],
                                                         bstack11l11l1l1_opy_[bstack11111l1l1_opy_])
    else:
      options.add_experimental_option(bstack11111l1l1_opy_, bstack11l11l1l1_opy_[bstack11111l1l1_opy_])
  if bstack111_opy_ (u"ࠬࡧࡲࡨࡵࠪठ") in bstack11l11l1l1_opy_:
    for arg in bstack11l11l1l1_opy_[bstack111_opy_ (u"࠭ࡡࡳࡩࡶࠫड")]:
      options.add_argument(arg)
    del (bstack11l11l1l1_opy_[bstack111_opy_ (u"ࠧࡢࡴࡪࡷࠬढ")])
  if bstack111_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬण") in bstack11l11l1l1_opy_:
    for ext in bstack11l11l1l1_opy_[bstack111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭त")]:
      options.add_extension(ext)
    del (bstack11l11l1l1_opy_[bstack111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ")])
def bstack1l11l11l_opy_(options, bstack1l11ll11_opy_):
  if bstack111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪद") in bstack1l11ll11_opy_:
    for bstack11l11ll1l_opy_ in bstack1l11ll11_opy_[bstack111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫध")]:
      if bstack11l11ll1l_opy_ in options._preferences:
        options._preferences[bstack11l11ll1l_opy_] = update(options._preferences[bstack11l11ll1l_opy_], bstack1l11ll11_opy_[bstack111_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन")][bstack11l11ll1l_opy_])
      else:
        options.set_preference(bstack11l11ll1l_opy_, bstack1l11ll11_opy_[bstack111_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")][bstack11l11ll1l_opy_])
  if bstack111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭प") in bstack1l11ll11_opy_:
    for arg in bstack1l11ll11_opy_[bstack111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧफ")]:
      options.add_argument(arg)
def bstack111ll111_opy_(options, bstack1llllll1ll_opy_):
  if bstack111_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫब") in bstack1llllll1ll_opy_:
    options.use_webview(bool(bstack1llllll1ll_opy_[bstack111_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬभ")]))
  bstack11ll1lll1_opy_(options, bstack1llllll1ll_opy_)
def bstack111111l11_opy_(options, bstack11l11ll11_opy_):
  for bstack11l1ll11_opy_ in bstack11l11ll11_opy_:
    if bstack11l1ll11_opy_ in [bstack111_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩम"), bstack111_opy_ (u"࠭ࡡࡳࡩࡶࠫय")]:
      continue
    options.set_capability(bstack11l1ll11_opy_, bstack11l11ll11_opy_[bstack11l1ll11_opy_])
  if bstack111_opy_ (u"ࠧࡢࡴࡪࡷࠬर") in bstack11l11ll11_opy_:
    for arg in bstack11l11ll11_opy_[bstack111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ")]:
      options.add_argument(arg)
  if bstack111_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ल") in bstack11l11ll11_opy_:
    options.bstack1llll11l1l_opy_(bool(bstack11l11ll11_opy_[bstack111_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧळ")]))
def bstack1l1111l1l_opy_(options, bstack11ll11l11_opy_):
  for bstack1l1111lll_opy_ in bstack11ll11l11_opy_:
    if bstack1l1111lll_opy_ in [bstack111_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऴ"), bstack111_opy_ (u"ࠬࡧࡲࡨࡵࠪव")]:
      continue
    options._options[bstack1l1111lll_opy_] = bstack11ll11l11_opy_[bstack1l1111lll_opy_]
  if bstack111_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪश") in bstack11ll11l11_opy_:
    for bstack1lll11l1ll_opy_ in bstack11ll11l11_opy_[bstack111_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫष")]:
      options.bstack1lll11lll1_opy_(
        bstack1lll11l1ll_opy_, bstack11ll11l11_opy_[bstack111_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस")][bstack1lll11l1ll_opy_])
  if bstack111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧह") in bstack11ll11l11_opy_:
    for arg in bstack11ll11l11_opy_[bstack111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨऺ")]:
      options.add_argument(arg)
def bstack1l1l111ll_opy_(options, caps):
  if not hasattr(options, bstack111_opy_ (u"ࠫࡐࡋ࡙ࠨऻ")):
    return
  if options.KEY == bstack111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ़ࠪ") and options.KEY in caps:
    bstack11ll1lll1_opy_(options, caps[bstack111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫऽ")])
  elif options.KEY == bstack111_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬा") and options.KEY in caps:
    bstack1l11l11l_opy_(options, caps[bstack111_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ि")])
  elif options.KEY == bstack111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪी") and options.KEY in caps:
    bstack111111l11_opy_(options, caps[bstack111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫु")])
  elif options.KEY == bstack111_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬू") and options.KEY in caps:
    bstack111ll111_opy_(options, caps[bstack111_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ृ")])
  elif options.KEY == bstack111_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬॄ") and options.KEY in caps:
    bstack1l1111l1l_opy_(options, caps[bstack111_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ॅ")])
def bstack111lll1l1_opy_(caps):
  global bstack1lllll1l1l_opy_
  if isinstance(os.environ.get(bstack111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩॆ")), str):
    bstack1lllll1l1l_opy_ = eval(os.getenv(bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪे")))
  if bstack1lllll1l1l_opy_:
    if bstack11ll1l1l1_opy_() < version.parse(bstack111_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩै")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫॉ")
    if bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪॊ") in caps:
      browser = caps[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫो")]
    elif bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨौ") in caps:
      browser = caps[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳ्ࠩ")]
    browser = str(browser).lower()
    if browser == bstack111_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩॎ") or browser == bstack111_opy_ (u"ࠪ࡭ࡵࡧࡤࠨॏ"):
      browser = bstack111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫॐ")
    if browser == bstack111_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭॑"):
      browser = bstack111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ॒࠭")
    if browser not in [bstack111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ॓"), bstack111_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭॔"), bstack111_opy_ (u"ࠩ࡬ࡩࠬॕ"), bstack111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪॖ"), bstack111_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬॗ")]:
      return None
    try:
      package = bstack111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧक़").format(browser)
      name = bstack111_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧख़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1lll1l1ll_opy_(options):
        return None
      for bstack1l1l1llll_opy_ in caps.keys():
        options.set_capability(bstack1l1l1llll_opy_, caps[bstack1l1l1llll_opy_])
      bstack1l1l111ll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l1l1ll1l_opy_(options, bstack1llll11l1_opy_):
  if not bstack1lll1l1ll_opy_(options):
    return
  for bstack1l1l1llll_opy_ in bstack1llll11l1_opy_.keys():
    if bstack1l1l1llll_opy_ in bstack1l111111l_opy_:
      continue
    if bstack1l1l1llll_opy_ in options._caps and type(options._caps[bstack1l1l1llll_opy_]) in [dict, list]:
      options._caps[bstack1l1l1llll_opy_] = update(options._caps[bstack1l1l1llll_opy_], bstack1llll11l1_opy_[bstack1l1l1llll_opy_])
    else:
      options.set_capability(bstack1l1l1llll_opy_, bstack1llll11l1_opy_[bstack1l1l1llll_opy_])
  bstack1l1l111ll_opy_(options, bstack1llll11l1_opy_)
  if bstack111_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ग़") in options._caps:
    if options._caps[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ज़")] and options._caps[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧड़")].lower() != bstack111_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫढ़"):
      del options._caps[bstack111_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪफ़")]
def bstack1ll1l1llll_opy_(proxy_config):
  if bstack111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩय़") in proxy_config:
    proxy_config[bstack111_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨॠ")] = proxy_config[bstack111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॡ")]
    del (proxy_config[bstack111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬॢ")])
  if bstack111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬॣ") in proxy_config and proxy_config[bstack111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭।")].lower() != bstack111_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫ॥"):
    proxy_config[bstack111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ०")] = bstack111_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭१")
  if bstack111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬ२") in proxy_config:
    proxy_config[bstack111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ३")] = bstack111_opy_ (u"ࠩࡳࡥࡨ࠭४")
  return proxy_config
def bstack1lllll11_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ५") in config:
    return proxy
  config[bstack111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ६")] = bstack1ll1l1llll_opy_(config[bstack111_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७")])
  if proxy == None:
    proxy = Proxy(config[bstack111_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")])
  return proxy
def bstack1lllll11l1_opy_(self):
  global CONFIG
  global bstack1l1111111_opy_
  try:
    proxy = bstack1lll111111_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ९")):
        proxies = bstack11llll1l1_opy_(proxy, bstack1lll1ll111_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11l1l1_opy_ = proxies.popitem()
          if bstack111_opy_ (u"ࠣ࠼࠲࠳ࠧ॰") in bstack1ll11l1l1_opy_:
            return bstack1ll11l1l1_opy_
          else:
            return bstack111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥॱ") + bstack1ll11l1l1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢॲ").format(str(e)))
  return bstack1l1111111_opy_(self)
def bstack1lll1l11l1_opy_():
  global CONFIG
  return bstack11llll11_opy_(CONFIG) and bstack11111ll11_opy_() >= version.parse(bstack11ll11l1l_opy_)
def bstack11l1l1111_opy_(config):
  bstack11l1ll1ll_opy_ = {}
  if bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॳ") in config:
    bstack11l1ll1ll_opy_ = config[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩॴ")]
  if bstack111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॵ") in config:
    bstack11l1ll1ll_opy_ = config[bstack111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ॶ")]
  proxy = bstack1lll111111_opy_(config)
  if proxy:
    if proxy.endswith(bstack111_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ॷ")) and os.path.isfile(proxy):
      bstack11l1ll1ll_opy_[bstack111_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬॸ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111_opy_ (u"ࠪ࠲ࡵࡧࡣࠨॹ")):
        proxies = bstack1lllll1ll_opy_(config, bstack1lll1ll111_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11l1l1_opy_ = proxies.popitem()
          if bstack111_opy_ (u"ࠦ࠿࠵࠯ࠣॺ") in bstack1ll11l1l1_opy_:
            parsed_url = urlparse(bstack1ll11l1l1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111_opy_ (u"ࠧࡀ࠯࠰ࠤॻ") + bstack1ll11l1l1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l1ll1ll_opy_[bstack111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩॼ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l1ll1ll_opy_[bstack111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪॽ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l1ll1ll_opy_[bstack111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫॾ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l1ll1ll_opy_[bstack111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬॿ")] = str(parsed_url.password)
  return bstack11l1ll1ll_opy_
def bstack11l1l1l1_opy_(config):
  if bstack111_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨঀ") in config:
    return config[bstack111_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩঁ")]
  return {}
def bstack1llll11lll_opy_(caps):
  global bstack1ll111ll1_opy_
  if bstack111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ং") in caps:
    caps[bstack111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧঃ")][bstack111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭঄")] = True
    if bstack1ll111ll1_opy_:
      caps[bstack111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঅ")][bstack111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫআ")] = bstack1ll111ll1_opy_
  else:
    caps[bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨই")] = True
    if bstack1ll111ll1_opy_:
      caps[bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬঈ")] = bstack1ll111ll1_opy_
def bstack1l1111l1_opy_():
  global CONFIG
  if bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩউ") in CONFIG and CONFIG[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪঊ")]:
    bstack11l1ll1ll_opy_ = bstack11l1l1111_opy_(CONFIG)
    bstack11lll1ll1_opy_(CONFIG[bstack111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪঋ")], bstack11l1ll1ll_opy_)
def bstack11lll1ll1_opy_(key, bstack11l1ll1ll_opy_):
  global bstack1111ll111_opy_
  logger.info(bstack111ll1lll_opy_)
  try:
    bstack1111ll111_opy_ = Local()
    bstack1ll1lllll1_opy_ = {bstack111_opy_ (u"ࠨ࡭ࡨࡽࠬঌ"): key}
    bstack1ll1lllll1_opy_.update(bstack11l1ll1ll_opy_)
    logger.debug(bstack1l1l1l1l_opy_.format(str(bstack1ll1lllll1_opy_)))
    bstack1111ll111_opy_.start(**bstack1ll1lllll1_opy_)
    if bstack1111ll111_opy_.isRunning():
      logger.info(bstack1111ll1ll_opy_)
  except Exception as e:
    bstack11l1l11l_opy_(bstack11l1llll_opy_.format(str(e)))
def bstack11lllll11_opy_():
  global bstack1111ll111_opy_
  if bstack1111ll111_opy_.isRunning():
    logger.info(bstack1ll111ll_opy_)
    bstack1111ll111_opy_.stop()
  bstack1111ll111_opy_ = None
def bstack111ll1ll1_opy_(bstack11ll11lll_opy_=[]):
  global CONFIG
  bstack1ll1ll11l1_opy_ = []
  bstack11llllll1_opy_ = [bstack111_opy_ (u"ࠩࡲࡷࠬ঍"), bstack111_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭঎"), bstack111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨএ"), bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧঐ"), bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ঑"), bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ঒")]
  try:
    for err in bstack11ll11lll_opy_:
      bstack1ll1llll1_opy_ = {}
      for k in bstack11llllll1_opy_:
        val = CONFIG[bstack111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫও")][int(err[bstack111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨঔ")])].get(k)
        if val:
          bstack1ll1llll1_opy_[k] = val
      bstack1ll1llll1_opy_[bstack111_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩক")] = {
        err[bstack111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩখ")]: err[bstack111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫগ")]
      }
      bstack1ll1ll11l1_opy_.append(bstack1ll1llll1_opy_)
  except Exception as e:
    logger.debug(bstack111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨঘ") + str(e))
  finally:
    return bstack1ll1ll11l1_opy_
def bstack1llll1l111_opy_():
  global bstack11111l11_opy_
  global bstack1ll1l11l_opy_
  global bstack1l1111ll1_opy_
  if bstack11111l11_opy_:
    logger.warning(bstack1lll11ll1l_opy_.format(str(bstack11111l11_opy_)))
  else:
    try:
      bstack11llll1l_opy_ = bstack1llll1ll11_opy_(bstack111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ঙ"), logger)
      if bstack11llll1l_opy_.get(bstack111_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭চ")) and bstack11llll1l_opy_.get(bstack111_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧছ")).get(bstack111_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬজ")):
        logger.warning(bstack1lll11ll1l_opy_.format(str(bstack11llll1l_opy_[bstack111_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩঝ")][bstack111_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧঞ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1ll1l111ll_opy_)
  global bstack1111ll111_opy_
  if bstack1111ll111_opy_:
    bstack11lllll11_opy_()
  try:
    for driver in bstack1ll1l11l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1ll1lll1l1_opy_)
  bstack11ll11ll1_opy_()
  if len(bstack1l1111ll1_opy_) > 0:
    message = bstack111ll1ll1_opy_(bstack1l1111ll1_opy_)
    bstack11ll11ll1_opy_(message)
  else:
    bstack11ll11ll1_opy_()
  bstack1lll111l_opy_(bstack111l1l1l_opy_, logger)
def bstack11lll1ll_opy_(self, *args):
  logger.error(bstack1l1l1l11l_opy_)
  bstack1llll1l111_opy_()
  sys.exit(1)
def bstack11l1l11l_opy_(err):
  logger.critical(bstack11l11llll_opy_.format(str(err)))
  bstack11ll11ll1_opy_(bstack11l11llll_opy_.format(str(err)))
  atexit.unregister(bstack1llll1l111_opy_)
  sys.exit(1)
def bstack111l1ll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11ll11ll1_opy_(message)
  atexit.unregister(bstack1llll1l111_opy_)
  sys.exit(1)
def bstack1ll11ll1_opy_():
  global CONFIG
  global bstack1ll1llll1l_opy_
  global bstack1llllll1l_opy_
  global bstack111l11l11_opy_
  CONFIG = bstack1ll11l11_opy_()
  bstack1ll111l1l_opy_()
  bstack111l111ll_opy_()
  CONFIG = bstack1l1l1l1ll_opy_(CONFIG)
  update(CONFIG, bstack1llllll1l_opy_)
  update(CONFIG, bstack1ll1llll1l_opy_)
  CONFIG = bstack1l1ll11l1_opy_(CONFIG)
  bstack111l11l11_opy_ = bstack111ll11ll_opy_(CONFIG)
  bstack1l11ll11l_opy_.bstack1l1ll1ll_opy_(bstack111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧট"), bstack111l11l11_opy_)
  if (bstack111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪঠ") in CONFIG and bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫড") in bstack1ll1llll1l_opy_) or (
          bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬঢ") in CONFIG and bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ণ") not in bstack1llllll1l_opy_):
    if os.getenv(bstack111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨত")):
      CONFIG[bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧথ")] = os.getenv(bstack111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪদ"))
    else:
      bstack1l11l111l_opy_()
  elif (bstack111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪধ") not in CONFIG and bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪন") in CONFIG) or (
          bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ঩") in bstack1llllll1l_opy_ and bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭প") not in bstack1ll1llll1l_opy_):
    del (CONFIG[bstack111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ফ")])
  if bstack11l111ll_opy_(CONFIG):
    bstack11l1l11l_opy_(bstack11l1ll111_opy_)
  bstack111lll11_opy_()
  bstack1lll1l1l1_opy_()
  if bstack1lllll1l1l_opy_:
    CONFIG[bstack111_opy_ (u"ࠬࡧࡰࡱࠩব")] = bstack1l11l111_opy_(CONFIG)
    logger.info(bstack1l1ll11l_opy_.format(CONFIG[bstack111_opy_ (u"࠭ࡡࡱࡲࠪভ")]))
def bstack1ll1l1111_opy_(config, bstack111lllll_opy_):
  global CONFIG
  global bstack1lllll1l1l_opy_
  CONFIG = config
  bstack1lllll1l1l_opy_ = bstack111lllll_opy_
def bstack1lll1l1l1_opy_():
  global CONFIG
  global bstack1lllll1l1l_opy_
  if bstack111_opy_ (u"ࠧࡢࡲࡳࠫম") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack111lll11l_opy_)
    bstack1lllll1l1l_opy_ = True
    bstack1l11ll11l_opy_.bstack1l1ll1ll_opy_(bstack111_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧয"), True)
def bstack1l11l111_opy_(config):
  bstack1l1llll11_opy_ = bstack111_opy_ (u"ࠩࠪর")
  app = config[bstack111_opy_ (u"ࠪࡥࡵࡶࠧ঱")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1ll1ll1l1_opy_:
      if os.path.exists(app):
        bstack1l1llll11_opy_ = bstack11ll111l1_opy_(config, app)
      elif bstack1ll1lll11l_opy_(app):
        bstack1l1llll11_opy_ = app
      else:
        bstack11l1l11l_opy_(bstack1lll111lll_opy_.format(app))
    else:
      if bstack1ll1lll11l_opy_(app):
        bstack1l1llll11_opy_ = app
      elif os.path.exists(app):
        bstack1l1llll11_opy_ = bstack11ll111l1_opy_(app)
      else:
        bstack11l1l11l_opy_(bstack111l11ll_opy_)
  else:
    if len(app) > 2:
      bstack11l1l11l_opy_(bstack11l1lll1l_opy_)
    elif len(app) == 2:
      if bstack111_opy_ (u"ࠫࡵࡧࡴࡩࠩল") in app and bstack111_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ঳") in app:
        if os.path.exists(app[bstack111_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ঴")]):
          bstack1l1llll11_opy_ = bstack11ll111l1_opy_(config, app[bstack111_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ঵")], app[bstack111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫশ")])
        else:
          bstack11l1l11l_opy_(bstack1lll111lll_opy_.format(app))
      else:
        bstack11l1l11l_opy_(bstack11l1lll1l_opy_)
    else:
      for key in app:
        if key in bstack1l111l11_opy_:
          if key == bstack111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧষ"):
            if os.path.exists(app[key]):
              bstack1l1llll11_opy_ = bstack11ll111l1_opy_(config, app[key])
            else:
              bstack11l1l11l_opy_(bstack1lll111lll_opy_.format(app))
          else:
            bstack1l1llll11_opy_ = app[key]
        else:
          bstack11l1l11l_opy_(bstack1lll1lll1l_opy_)
  return bstack1l1llll11_opy_
def bstack1ll1lll11l_opy_(bstack1l1llll11_opy_):
  import re
  bstack111ll1l1l_opy_ = re.compile(bstack111_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥস"))
  bstack11l11l11_opy_ = re.compile(bstack111_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣহ"))
  if bstack111_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫ঺") in bstack1l1llll11_opy_ or re.fullmatch(bstack111ll1l1l_opy_, bstack1l1llll11_opy_) or re.fullmatch(bstack11l11l11_opy_, bstack1l1llll11_opy_):
    return True
  else:
    return False
def bstack11ll111l1_opy_(config, path, bstack1ll11111l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111_opy_ (u"࠭ࡲࡣࠩ঻")).read()).hexdigest()
  bstack11l11111_opy_ = bstack111ll1l11_opy_(md5_hash)
  bstack1l1llll11_opy_ = None
  if bstack11l11111_opy_:
    logger.info(bstack1l11l1lll_opy_.format(bstack11l11111_opy_, md5_hash))
    return bstack11l11111_opy_
  bstack1ll1ll1l1l_opy_ = MultipartEncoder(
    fields={
      bstack111_opy_ (u"ࠧࡧ࡫࡯ࡩ়ࠬ"): (os.path.basename(path), open(os.path.abspath(path), bstack111_opy_ (u"ࠨࡴࡥࠫঽ")), bstack111_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭া")),
      bstack111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ি"): bstack1ll11111l_opy_
    }
  )
  response = requests.post(bstack1ll1l11l11_opy_, data=bstack1ll1ll1l1l_opy_,
                           headers={bstack111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪী"): bstack1ll1ll1l1l_opy_.content_type},
                           auth=(config[bstack111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧু")], config[bstack111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩূ")]))
  try:
    res = json.loads(response.text)
    bstack1l1llll11_opy_ = res[bstack111_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨৃ")]
    logger.info(bstack1ll1111ll_opy_.format(bstack1l1llll11_opy_))
    bstack1llllll11_opy_(md5_hash, bstack1l1llll11_opy_)
  except ValueError as err:
    bstack11l1l11l_opy_(bstack1lll11ll11_opy_.format(str(err)))
  return bstack1l1llll11_opy_
def bstack111lll11_opy_():
  global CONFIG
  global bstack1ll1llll_opy_
  bstack1ll1ll1ll_opy_ = 0
  bstack1lllll1l1_opy_ = 1
  if bstack111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨৄ") in CONFIG:
    bstack1lllll1l1_opy_ = CONFIG[bstack111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ৅")]
  if bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆") in CONFIG:
    bstack1ll1ll1ll_opy_ = len(CONFIG[bstack111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧে")])
  bstack1ll1llll_opy_ = int(bstack1lllll1l1_opy_) * int(bstack1ll1ll1ll_opy_)
def bstack111ll1l11_opy_(md5_hash):
  bstack1lll11111_opy_ = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠬࢄࠧৈ")), bstack111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭৉"), bstack111_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ৊"))
  if os.path.exists(bstack1lll11111_opy_):
    bstack1l1ll1111_opy_ = json.load(open(bstack1lll11111_opy_, bstack111_opy_ (u"ࠨࡴࡥࠫো")))
    if md5_hash in bstack1l1ll1111_opy_:
      bstack1lll111l1_opy_ = bstack1l1ll1111_opy_[md5_hash]
      bstack11l1ll11l_opy_ = datetime.datetime.now()
      bstack111l1ll1_opy_ = datetime.datetime.strptime(bstack1lll111l1_opy_[bstack111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬৌ")], bstack111_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾্࡙ࠪࠧ"))
      if (bstack11l1ll11l_opy_ - bstack111l1ll1_opy_).days > 60:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1lll111l1_opy_[bstack111_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩৎ")]):
        return None
      return bstack1lll111l1_opy_[bstack111_opy_ (u"ࠬ࡯ࡤࠨ৏")]
  else:
    return None
def bstack1llllll11_opy_(md5_hash, bstack1l1llll11_opy_):
  bstack111111111_opy_ = os.path.join(os.path.expanduser(bstack111_opy_ (u"࠭ࡾࠨ৐")), bstack111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ৑"))
  if not os.path.exists(bstack111111111_opy_):
    os.makedirs(bstack111111111_opy_)
  bstack1lll11111_opy_ = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠨࢀࠪ৒")), bstack111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ৓"), bstack111_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫ৔"))
  bstack11l1l11ll_opy_ = {
    bstack111_opy_ (u"ࠫ࡮ࡪࠧ৕"): bstack1l1llll11_opy_,
    bstack111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ৖"): datetime.datetime.strftime(datetime.datetime.now(), bstack111_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪৗ")),
    bstack111_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ৘"): str(__version__)
  }
  if os.path.exists(bstack1lll11111_opy_):
    bstack1l1ll1111_opy_ = json.load(open(bstack1lll11111_opy_, bstack111_opy_ (u"ࠨࡴࡥࠫ৙")))
  else:
    bstack1l1ll1111_opy_ = {}
  bstack1l1ll1111_opy_[md5_hash] = bstack11l1l11ll_opy_
  with open(bstack1lll11111_opy_, bstack111_opy_ (u"ࠤࡺ࠯ࠧ৚")) as outfile:
    json.dump(bstack1l1ll1111_opy_, outfile)
def bstack1llll11ll1_opy_(self):
  return
def bstack1ll1111l_opy_(self):
  return
def bstack111ll111l_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1l11lll1l_opy_(self):
  global bstack1lllllll11_opy_
  global bstack1llll111_opy_
  global bstack11l111l11_opy_
  try:
    if bstack111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ৛") in bstack1lllllll11_opy_ and self.session_id != None:
      bstack1llll1l1l1_opy_ = bstack111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫড়") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬঢ়")
      bstack1l1ll1ll1_opy_ = bstack1ll1llllll_opy_(bstack111_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ৞"), bstack111_opy_ (u"ࠧࠨয়"), bstack1llll1l1l1_opy_, bstack111_opy_ (u"ࠨ࠮ࠣࠫৠ").join(
        threading.current_thread().bstackTestErrorMessages), bstack111_opy_ (u"ࠩࠪৡ"), bstack111_opy_ (u"ࠪࠫৢ"))
      if self != None:
        self.execute_script(bstack1l1ll1ll1_opy_)
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧৣ") + str(e))
  bstack11l111l11_opy_(self)
  self.session_id = None
def bstack1ll1l1lll_opy_(self, *args, **kwargs):
  bstack1lllll1111_opy_ = bstack111l1llll_opy_(self, *args, **kwargs)
  bstack1111llll_opy_.bstack1l1lll1l1_opy_(self)
  return bstack1lllll1111_opy_
def bstack111ll1111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1llll111_opy_
  global bstack1lll1l1111_opy_
  global bstack1lll1111_opy_
  global bstack1l11llll_opy_
  global bstack1111l11ll_opy_
  global bstack1lllllll11_opy_
  global bstack111l1llll_opy_
  global bstack1ll1l11l_opy_
  global bstack1l111l1l_opy_
  CONFIG[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ৤")] = str(bstack1lllllll11_opy_) + str(__version__)
  command_executor = bstack1lll1ll111_opy_()
  logger.debug(bstack1111ll1l1_opy_.format(command_executor))
  proxy = bstack1lllll11_opy_(CONFIG, proxy)
  bstack1lll111l1l_opy_ = 0 if bstack1lll1l1111_opy_ < 0 else bstack1lll1l1111_opy_
  try:
    if bstack1l11llll_opy_ is True:
      bstack1lll111l1l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1111l11ll_opy_ is True:
      bstack1lll111l1l_opy_ = int(threading.current_thread().name)
  except:
    bstack1lll111l1l_opy_ = 0
  bstack1llll11l1_opy_ = bstack1l111ll11_opy_(CONFIG, bstack1lll111l1l_opy_)
  logger.debug(bstack1lll11111l_opy_.format(str(bstack1llll11l1_opy_)))
  if bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ৥") in CONFIG and CONFIG[bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ০")]:
    bstack1llll11lll_opy_(bstack1llll11l1_opy_)
  if desired_capabilities:
    bstack1l1l11l11_opy_ = bstack1l1l1l1ll_opy_(desired_capabilities)
    bstack1l1l11l11_opy_[bstack111_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ১")] = bstack1ll11l1l_opy_(CONFIG)
    bstack1lll1l1l1l_opy_ = bstack1l111ll11_opy_(bstack1l1l11l11_opy_)
    if bstack1lll1l1l1l_opy_:
      bstack1llll11l1_opy_ = update(bstack1lll1l1l1l_opy_, bstack1llll11l1_opy_)
    desired_capabilities = None
  if options:
    bstack1l1l1ll1l_opy_(options, bstack1llll11l1_opy_)
  if not options:
    options = bstack111lll1l1_opy_(bstack1llll11l1_opy_)
  if proxy and bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ২")):
    options.proxy(proxy)
  if options and bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ৩")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11111ll11_opy_() < version.parse(bstack111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ৪")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1llll11l1_opy_)
  logger.info(bstack11lll1l1l_opy_)
  if bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ৫")):
    bstack111l1llll_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ৬")):
    bstack111l1llll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧ৭")):
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
    bstack11l111111_opy_ = bstack111_opy_ (u"ࠨࠩ৮")
    if bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪ৯")):
      bstack11l111111_opy_ = self.caps.get(bstack111_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥৰ"))
    else:
      bstack11l111111_opy_ = self.capabilities.get(bstack111_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦৱ"))
    if bstack11l111111_opy_:
      if bstack11111ll11_opy_() <= version.parse(bstack111_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ৲")):
        self.command_executor._url = bstack111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ৳") + bstack1l1l1111_opy_ + bstack111_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ৴")
      else:
        self.command_executor._url = bstack111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ৵") + bstack11l111111_opy_ + bstack111_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ৶")
      logger.debug(bstack11l11l11l_opy_.format(bstack11l111111_opy_))
    else:
      logger.debug(bstack1lll1111l_opy_.format(bstack111_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦ৷")))
  except Exception as e:
    logger.debug(bstack1lll1111l_opy_.format(e))
  if bstack111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ৸") in bstack1lllllll11_opy_:
    bstack11l1111ll_opy_(bstack1lll1l1111_opy_, bstack1l111l1l_opy_)
  bstack1llll111_opy_ = self.session_id
  if bstack111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ৹") in bstack1lllllll11_opy_ or bstack111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭৺") in bstack1lllllll11_opy_:
    threading.current_thread().bstack11ll111l_opy_ = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1111llll_opy_.bstack1l1lll1l1_opy_(self)
  bstack1ll1l11l_opy_.append(self)
  if bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৻") in CONFIG and bstack111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ৼ") in CONFIG[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৽")][bstack1lll111l1l_opy_]:
    bstack1lll1111_opy_ = CONFIG[bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৾")][bstack1lll111l1l_opy_][bstack111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ৿")]
  logger.debug(bstack1l1ll1l1_opy_.format(bstack1llll111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1lll1ll1l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lll11l1l_opy_
      if(bstack111_opy_ (u"ࠧ࡯࡮ࡥࡧࡻ࠲࡯ࡹࠢ਀") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111_opy_ (u"࠭ࡾࠨਁ")), bstack111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧਂ"), bstack111_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪਃ")), bstack111_opy_ (u"ࠩࡺࠫ਄")) as fp:
          fp.write(bstack111_opy_ (u"ࠥࠦਅ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨਆ")))):
          with open(args[1], bstack111_opy_ (u"ࠬࡸࠧਇ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111_opy_ (u"࠭ࡡࡴࡻࡱࡧࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡠࡰࡨࡻࡕࡧࡧࡦࠪࡦࡳࡳࡺࡥࡹࡶ࠯ࠤࡵࡧࡧࡦࠢࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠬਈ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack111l11l1l_opy_)
            lines.insert(1, bstack1lll1ll11l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤਉ")), bstack111_opy_ (u"ࠨࡹࠪਊ")) as bstack11l11lll1_opy_:
              bstack11l11lll1_opy_.writelines(lines)
        CONFIG[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ਋")] = str(bstack1lllllll11_opy_) + str(__version__)
        bstack1lll111l1l_opy_ = 0 if bstack1lll1l1111_opy_ < 0 else bstack1lll1l1111_opy_
        try:
          if bstack1l11llll_opy_ is True:
            bstack1lll111l1l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1111l11ll_opy_ is True:
            bstack1lll111l1l_opy_ = int(threading.current_thread().name)
        except:
          bstack1lll111l1l_opy_ = 0
        CONFIG[bstack111_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥ਌")] = False
        CONFIG[bstack111_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ਍")] = True
        bstack1llll11l1_opy_ = bstack1l111ll11_opy_(CONFIG, bstack1lll111l1l_opy_)
        logger.debug(bstack1lll11111l_opy_.format(str(bstack1llll11l1_opy_)))
        if CONFIG[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ਎")]:
          bstack1llll11lll_opy_(bstack1llll11l1_opy_)
        if bstack111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਏ") in CONFIG and bstack111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬਐ") in CONFIG[bstack111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ਑")][bstack1lll111l1l_opy_]:
          bstack1lll1111_opy_ = CONFIG[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ਒")][bstack1lll111l1l_opy_][bstack111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਓ")]
        args.append(os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠫࢃ࠭ਔ")), bstack111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬਕ"), bstack111_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨਖ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1llll11l1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤਗ"))
      bstack1lll11l1l_opy_ = True
      return bstack1l11l1l11_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1111l111_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1lll1l1111_opy_
    global bstack1lll1111_opy_
    global bstack1l11llll_opy_
    global bstack1111l11ll_opy_
    global bstack1lllllll11_opy_
    CONFIG[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪਘ")] = str(bstack1lllllll11_opy_) + str(__version__)
    bstack1lll111l1l_opy_ = 0 if bstack1lll1l1111_opy_ < 0 else bstack1lll1l1111_opy_
    try:
      if bstack1l11llll_opy_ is True:
        bstack1lll111l1l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1111l11ll_opy_ is True:
        bstack1lll111l1l_opy_ = int(threading.current_thread().name)
    except:
      bstack1lll111l1l_opy_ = 0
    CONFIG[bstack111_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣਙ")] = True
    bstack1llll11l1_opy_ = bstack1l111ll11_opy_(CONFIG, bstack1lll111l1l_opy_)
    logger.debug(bstack1lll11111l_opy_.format(str(bstack1llll11l1_opy_)))
    if CONFIG[bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਚ")]:
      bstack1llll11lll_opy_(bstack1llll11l1_opy_)
    if bstack111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧਛ") in CONFIG and bstack111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪਜ") in CONFIG[bstack111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਝ")][bstack1lll111l1l_opy_]:
      bstack1lll1111_opy_ = CONFIG[bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਞ")][bstack1lll111l1l_opy_][bstack111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ਟ")]
    import urllib
    import json
    bstack1lllll1lll_opy_ = bstack111_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫਠ") + urllib.parse.quote(json.dumps(bstack1llll11l1_opy_))
    browser = self.connect(bstack1lllll1lll_opy_)
    return browser
except Exception as e:
    pass
def bstack11111l111_opy_():
    global bstack1lll11l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1111l111_opy_
        bstack1lll11l1l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1lll1ll1l1_opy_
      bstack1lll11l1l_opy_ = True
    except Exception as e:
      pass
def bstack1l1l1l111_opy_(context, bstack1111l1l1l_opy_):
  try:
    context.page.evaluate(bstack111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦਡ"), bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨਢ")+ json.dumps(bstack1111l1l1l_opy_) + bstack111_opy_ (u"ࠧࢃࡽࠣਣ"))
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦਤ"), e)
def bstack1ll11l111_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣਥ"), bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ਦ") + json.dumps(message) + bstack111_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬਧ") + json.dumps(level) + bstack111_opy_ (u"ࠪࢁࢂ࠭ਨ"))
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢ਩"), e)
def bstack1l1l11111_opy_(context, status, message = bstack111_opy_ (u"ࠧࠨਪ")):
  try:
    if(status == bstack111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨਫ")):
      context.page.evaluate(bstack111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣਬ"), bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡳࡧࡤࡷࡴࡴࠢ࠻ࠩਭ") + json.dumps(bstack111_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࠦਮ") + str(message)) + bstack111_opy_ (u"ࠪ࠰ࠧࡹࡴࡢࡶࡸࡷࠧࡀࠧਯ") + json.dumps(status) + bstack111_opy_ (u"ࠦࢂࢃࠢਰ"))
    else:
      context.page.evaluate(bstack111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ਱"), bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡹࡴࡢࡶࡸࡷࠧࡀࠧਲ") + json.dumps(status) + bstack111_opy_ (u"ࠢࡾࡿࠥਲ਼"))
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡾࢁࠧ਴"), e)
def bstack11llll11l_opy_(self, url):
  global bstack1111l1lll_opy_
  try:
    bstack1l1l1l11_opy_(url)
  except Exception as err:
    logger.debug(bstack1llll1l1l_opy_.format(str(err)))
  try:
    bstack1111l1lll_opy_(self, url)
  except Exception as e:
    try:
      bstack111lll1l_opy_ = str(e)
      if any(err_msg in bstack111lll1l_opy_ for err_msg in bstack1lll1l1ll1_opy_):
        bstack1l1l1l11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1llll1l1l_opy_.format(str(err)))
    raise e
def bstack1111111ll_opy_(self):
  global bstack1ll111l11_opy_
  bstack1ll111l11_opy_ = self
  return
def bstack1ll1l11ll_opy_(self):
  global bstack1llll11111_opy_
  bstack1llll11111_opy_ = self
  return
def bstack11l1lll11_opy_(self, test):
  global CONFIG
  global bstack1llll11111_opy_
  global bstack1ll111l11_opy_
  global bstack1llll111_opy_
  global bstack11l1l1ll1_opy_
  global bstack1lll1111_opy_
  global bstack1ll1l111_opy_
  global bstack1l1l1l1l1_opy_
  global bstack1111l1l1_opy_
  global bstack1ll1l11l_opy_
  try:
    if not bstack1llll111_opy_:
      with open(os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠩࢁࠫਵ")), bstack111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪਸ਼"), bstack111_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭਷"))) as f:
        bstack111llllll_opy_ = json.loads(bstack111_opy_ (u"ࠧࢁࠢਸ") + f.read().strip() + bstack111_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨਹ") + bstack111_opy_ (u"ࠢࡾࠤ਺"))
        bstack1llll111_opy_ = bstack111llllll_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1ll1l11l_opy_:
    for driver in bstack1ll1l11l_opy_:
      if bstack1llll111_opy_ == driver.session_id:
        if test:
          bstack1llllllll_opy_ = str(test.data)
        if not bstack1l1ll1l11_opy_ and bstack1llllllll_opy_:
          bstack11111111_opy_ = {
            bstack111_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ਻"): bstack111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧ਼ࠪ"),
            bstack111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭਽"): {
              bstack111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩਾ"): bstack1llllllll_opy_
            }
          }
          bstack11l11111l_opy_ = bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪਿ").format(json.dumps(bstack11111111_opy_))
          driver.execute_script(bstack11l11111l_opy_)
        if bstack11l1l1ll1_opy_:
          bstack11l11l1l_opy_ = {
            bstack111_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ੀ"): bstack111_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩੁ"),
            bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫੂ"): {
              bstack111_opy_ (u"ࠩࡧࡥࡹࡧࠧ੃"): bstack1llllllll_opy_ + bstack111_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ੄"),
              bstack111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ੅"): bstack111_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ੆")
            }
          }
          bstack11111111_opy_ = {
            bstack111_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ੇ"): bstack111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪੈ"),
            bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ੉"): {
              bstack111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ੊"): bstack111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪੋ")
            }
          }
          if bstack11l1l1ll1_opy_.status == bstack111_opy_ (u"ࠫࡕࡇࡓࡔࠩੌ"):
            bstack1l1ll1lll_opy_ = bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿ੍ࠪ").format(json.dumps(bstack11l11l1l_opy_))
            driver.execute_script(bstack1l1ll1lll_opy_)
            bstack11l11111l_opy_ = bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ੎").format(json.dumps(bstack11111111_opy_))
            driver.execute_script(bstack11l11111l_opy_)
          elif bstack11l1l1ll1_opy_.status == bstack111_opy_ (u"ࠧࡇࡃࡌࡐࠬ੏"):
            reason = bstack111_opy_ (u"ࠣࠤ੐")
            bstack1lll1lll_opy_ = bstack1llllllll_opy_ + bstack111_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠪੑ")
            if bstack11l1l1ll1_opy_.message:
              reason = str(bstack11l1l1ll1_opy_.message)
              bstack1lll1lll_opy_ = bstack1lll1lll_opy_ + bstack111_opy_ (u"ࠪࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࠪ੒") + reason
            bstack11l11l1l_opy_[bstack111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ੓")] = {
              bstack111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ੔"): bstack111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ੕"),
              bstack111_opy_ (u"ࠧࡥࡣࡷࡥࠬ੖"): bstack1lll1lll_opy_
            }
            bstack11111111_opy_[bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ੗")] = {
              bstack111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ੘"): bstack111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪਖ਼"),
              bstack111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫਗ਼"): reason
            }
            bstack1l1ll1lll_opy_ = bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪਜ਼").format(json.dumps(bstack11l11l1l_opy_))
            driver.execute_script(bstack1l1ll1lll_opy_)
            bstack11l11111l_opy_ = bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫੜ").format(json.dumps(bstack11111111_opy_))
            driver.execute_script(bstack11l11111l_opy_)
  elif bstack1llll111_opy_:
    try:
      data = {}
      bstack1llllllll_opy_ = None
      if test:
        bstack1llllllll_opy_ = str(test.data)
      if not bstack1l1ll1l11_opy_ and bstack1llllllll_opy_:
        data[bstack111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ੝")] = bstack1llllllll_opy_
      if bstack11l1l1ll1_opy_:
        if bstack11l1l1ll1_opy_.status == bstack111_opy_ (u"ࠨࡒࡄࡗࡘ࠭ਫ਼"):
          data[bstack111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ੟")] = bstack111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ੠")
        elif bstack11l1l1ll1_opy_.status == bstack111_opy_ (u"ࠫࡋࡇࡉࡍࠩ੡"):
          data[bstack111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ੢")] = bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭੣")
          if bstack11l1l1ll1_opy_.message:
            data[bstack111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ੤")] = str(bstack11l1l1ll1_opy_.message)
      user = CONFIG[bstack111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ੥")]
      key = CONFIG[bstack111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ੦")]
      url = bstack111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨ੧").format(user, key, bstack1llll111_opy_)
      headers = {
        bstack111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ੨"): bstack111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ੩"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack11l1111l_opy_.format(str(e)))
  if bstack1llll11111_opy_:
    bstack1l1l1l1l1_opy_(bstack1llll11111_opy_)
  if bstack1ll111l11_opy_:
    bstack1111l1l1_opy_(bstack1ll111l11_opy_)
  bstack1ll1l111_opy_(self, test)
def bstack1l1l11ll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1llll1lll_opy_
  bstack1llll1lll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l1l1ll1_opy_
  bstack11l1l1ll1_opy_ = self._test
def bstack1l1l11l1_opy_():
  global bstack1l11111ll_opy_
  try:
    if os.path.exists(bstack1l11111ll_opy_):
      os.remove(bstack1l11111ll_opy_)
  except Exception as e:
    logger.debug(bstack111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩ੪") + str(e))
def bstack11111ll1l_opy_():
  global bstack1l11111ll_opy_
  bstack11llll1l_opy_ = {}
  try:
    if not os.path.isfile(bstack1l11111ll_opy_):
      with open(bstack1l11111ll_opy_, bstack111_opy_ (u"ࠧࡸࠩ੫")):
        pass
      with open(bstack1l11111ll_opy_, bstack111_opy_ (u"ࠣࡹ࠮ࠦ੬")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1l11111ll_opy_):
      bstack11llll1l_opy_ = json.load(open(bstack1l11111ll_opy_, bstack111_opy_ (u"ࠩࡵࡦࠬ੭")))
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬ੮") + str(e))
  finally:
    return bstack11llll1l_opy_
def bstack11l1111ll_opy_(platform_index, item_index):
  global bstack1l11111ll_opy_
  try:
    bstack11llll1l_opy_ = bstack11111ll1l_opy_()
    bstack11llll1l_opy_[item_index] = platform_index
    with open(bstack1l11111ll_opy_, bstack111_opy_ (u"ࠦࡼ࠱ࠢ੯")) as outfile:
      json.dump(bstack11llll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪੰ") + str(e))
def bstack1l11l1l1l_opy_(bstack1llll1111_opy_):
  global CONFIG
  bstack1l11111l_opy_ = bstack111_opy_ (u"࠭ࠧੱ")
  if not bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪੲ") in CONFIG:
    logger.info(bstack111_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬੳ"))
  try:
    platform = CONFIG[bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬੴ")][bstack1llll1111_opy_]
    if bstack111_opy_ (u"ࠪࡳࡸ࠭ੵ") in platform:
      bstack1l11111l_opy_ += str(platform[bstack111_opy_ (u"ࠫࡴࡹࠧ੶")]) + bstack111_opy_ (u"ࠬ࠲ࠠࠨ੷")
    if bstack111_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ੸") in platform:
      bstack1l11111l_opy_ += str(platform[bstack111_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ੹")]) + bstack111_opy_ (u"ࠨ࠮ࠣࠫ੺")
    if bstack111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭੻") in platform:
      bstack1l11111l_opy_ += str(platform[bstack111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧ੼")]) + bstack111_opy_ (u"ࠫ࠱ࠦࠧ੽")
    if bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ੾") in platform:
      bstack1l11111l_opy_ += str(platform[bstack111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ੿")]) + bstack111_opy_ (u"ࠧ࠭ࠢࠪ઀")
    if bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ઁ") in platform:
      bstack1l11111l_opy_ += str(platform[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧં")]) + bstack111_opy_ (u"ࠪ࠰ࠥ࠭ઃ")
    if bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ઄") in platform:
      bstack1l11111l_opy_ += str(platform[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭અ")]) + bstack111_opy_ (u"࠭ࠬࠡࠩઆ")
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠧઇ") + str(e))
  finally:
    if bstack1l11111l_opy_[len(bstack1l11111l_opy_) - 2:] == bstack111_opy_ (u"ࠨ࠮ࠣࠫઈ"):
      bstack1l11111l_opy_ = bstack1l11111l_opy_[:-2]
    return bstack1l11111l_opy_
def bstack11l1ll1l_opy_(path, bstack1l11111l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l1l1l1l_opy_ = ET.parse(path)
    bstack1lll1ll11_opy_ = bstack11l1l1l1l_opy_.getroot()
    bstack1llll1llll_opy_ = None
    for suite in bstack1lll1ll11_opy_.iter(bstack111_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨઉ")):
      if bstack111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪઊ") in suite.attrib:
        suite.attrib[bstack111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩઋ")] += bstack111_opy_ (u"ࠬࠦࠧઌ") + bstack1l11111l_opy_
        bstack1llll1llll_opy_ = suite
    bstack1ll1ll111_opy_ = None
    for robot in bstack1lll1ll11_opy_.iter(bstack111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬઍ")):
      bstack1ll1ll111_opy_ = robot
    bstack111l1l11l_opy_ = len(bstack1ll1ll111_opy_.findall(bstack111_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭઎")))
    if bstack111l1l11l_opy_ == 1:
      bstack1ll1ll111_opy_.remove(bstack1ll1ll111_opy_.findall(bstack111_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧએ"))[0])
      bstack11ll1l11_opy_ = ET.Element(bstack111_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨઐ"), attrib={bstack111_opy_ (u"ࠪࡲࡦࡳࡥࠨઑ"): bstack111_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫ઒"), bstack111_opy_ (u"ࠬ࡯ࡤࠨઓ"): bstack111_opy_ (u"࠭ࡳ࠱ࠩઔ")})
      bstack1ll1ll111_opy_.insert(1, bstack11ll1l11_opy_)
      bstack1111l1l11_opy_ = None
      for suite in bstack1ll1ll111_opy_.iter(bstack111_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ક")):
        bstack1111l1l11_opy_ = suite
      bstack1111l1l11_opy_.append(bstack1llll1llll_opy_)
      bstack1lll1l1lll_opy_ = None
      for status in bstack1llll1llll_opy_.iter(bstack111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨખ")):
        bstack1lll1l1lll_opy_ = status
      bstack1111l1l11_opy_.append(bstack1lll1l1lll_opy_)
    bstack11l1l1l1l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧગ") + str(e))
def bstack11lllll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1lll11llll_opy_
  global CONFIG
  if bstack111_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢઘ") in options:
    del options[bstack111_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣઙ")]
  bstack1lllllll1_opy_ = bstack11111ll1l_opy_()
  for bstack11111lll_opy_ in bstack1lllllll1_opy_.keys():
    path = os.path.join(os.getcwd(), bstack111_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬચ"), str(bstack11111lll_opy_), bstack111_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪછ"))
    bstack11l1ll1l_opy_(path, bstack1l11l1l1l_opy_(bstack1lllllll1_opy_[bstack11111lll_opy_]))
  bstack1l1l11l1_opy_()
  return bstack1lll11llll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111l11111_opy_(self, ff_profile_dir):
  global bstack1ll1ll1lll_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll1ll1lll_opy_(self, ff_profile_dir)
def bstack1lll1l1l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll111ll1_opy_
  bstack1llll1ll1l_opy_ = []
  if bstack111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪજ") in CONFIG:
    bstack1llll1ll1l_opy_ = CONFIG[bstack111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫઝ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥઞ")],
      pabot_args[bstack111_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦટ")],
      argfile,
      pabot_args.get(bstack111_opy_ (u"ࠦ࡭࡯ࡶࡦࠤઠ")),
      pabot_args[bstack111_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣડ")],
      platform[0],
      bstack1ll111ll1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨઢ")] or [(bstack111_opy_ (u"ࠢࠣણ"), None)]
    for platform in enumerate(bstack1llll1ll1l_opy_)
  ]
def bstack111ll11l1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll1lllll_opy_=bstack111_opy_ (u"ࠨࠩત")):
  global bstack1l1l1ll1_opy_
  self.platform_index = platform_index
  self.bstack1l111l111_opy_ = bstack1ll1lllll_opy_
  bstack1l1l1ll1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l11l11ll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1l11ll1_opy_
  global bstack1l1l1lll_opy_
  if not bstack111_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫથ") in item.options:
    item.options[bstack111_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬદ")] = []
  for v in item.options[bstack111_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ધ")]:
    if bstack111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫન") in v:
      item.options[bstack111_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ઩")].remove(v)
    if bstack111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧપ") in v:
      item.options[bstack111_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪફ")].remove(v)
  item.options[bstack111_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫબ")].insert(0, bstack111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙࠼ࡾࢁࠬભ").format(item.platform_index))
  item.options[bstack111_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭મ")].insert(0, bstack111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓ࠼ࡾࢁࠬય").format(item.bstack1l111l111_opy_))
  if bstack1l1l1lll_opy_:
    item.options[bstack111_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨર")].insert(0, bstack111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙࠺ࡼࡿࠪ઱").format(bstack1l1l1lll_opy_))
  return bstack1l1l11ll1_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1l1l11l1l_opy_(command, item_index):
  global bstack1l1l1lll_opy_
  if bstack1l1l1lll_opy_:
    command[0] = command[0].replace(bstack111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧલ"), bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭ળ") + str(
      item_index) + bstack111_opy_ (u"ࠪࠤࠬ઴") + bstack1l1l1lll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪવ"),
                                    bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩશ") + str(item_index), 1)
def bstack11ll1l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111ll1ll_opy_
  bstack1l1l11l1l_opy_(command, item_index)
  return bstack111ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack111111l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111ll1ll_opy_
  bstack1l1l11l1l_opy_(command, item_index)
  return bstack111ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1lll1111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111ll1ll_opy_
  bstack1l1l11l1l_opy_(command, item_index)
  return bstack111ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1llll1l11_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll1ll11_opy_
  bstack11lllll1l_opy_ = bstack1ll1ll11_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack111_opy_ (u"࠭ࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡡࡤࡶࡷ࠭ષ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111_opy_ (u"ࠧࡦࡺࡦࡣࡹࡸࡡࡤࡧࡥࡥࡨࡱ࡟ࡢࡴࡵࠫસ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11lllll1l_opy_
def bstack1ll1lll1ll_opy_(self, name, context, *args):
  global bstack1l1lll11_opy_
  if name == bstack111_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠩહ"):
    bstack1l1lll11_opy_(self, name, context, *args)
    try:
      if not bstack1l1ll1l11_opy_:
        bstack1llll1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1ll11ll_opy_(bstack111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ઺")) else context.browser
        bstack1111l1l1l_opy_ = str(self.feature.name)
        bstack1l1l1l111_opy_(context, bstack1111l1l1l_opy_)
        bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨ઻") + json.dumps(bstack1111l1l1l_opy_) + bstack111_opy_ (u"ࠫࢂࢃ઼ࠧ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack111_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬઽ").format(str(e)))
  elif name == bstack111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨા"):
    bstack1l1lll11_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack111_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩિ")):
        self.driver_before_scenario = True
      if (not bstack1l1ll1l11_opy_):
        scenario_name = args[0].name
        feature_name = bstack1111l1l1l_opy_ = str(self.feature.name)
        bstack1111l1l1l_opy_ = feature_name + bstack111_opy_ (u"ࠨࠢ࠰ࠤࠬી") + scenario_name
        bstack1llll1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1ll11ll_opy_(bstack111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨુ")) else context.browser
        if self.driver_before_scenario:
          bstack1l1l1l111_opy_(context, bstack1111l1l1l_opy_)
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨૂ") + json.dumps(bstack1111l1l1l_opy_) + bstack111_opy_ (u"ࠫࢂࢃࠧૃ"))
    except Exception as e:
      logger.debug(bstack111_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭ૄ").format(str(e)))
  elif name == bstack111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧૅ"):
    try:
      bstack1lll11l1l1_opy_ = args[0].status.name
      bstack1llll1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭૆") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1lll11l1l1_opy_).lower() == bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨે"):
        bstack1llll11l11_opy_ = bstack111_opy_ (u"ࠩࠪૈ")
        bstack1lll1llll1_opy_ = bstack111_opy_ (u"ࠪࠫૉ")
        bstack1ll1l11l1l_opy_ = bstack111_opy_ (u"ࠫࠬ૊")
        try:
          import traceback
          bstack1llll11l11_opy_ = self.exception.__class__.__name__
          bstack1l1lll111_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1lll1llll1_opy_ = bstack111_opy_ (u"ࠬࠦࠧો").join(bstack1l1lll111_opy_)
          bstack1ll1l11l1l_opy_ = bstack1l1lll111_opy_[-1]
        except Exception as e:
          logger.debug(bstack11l11lll_opy_.format(str(e)))
        bstack1llll11l11_opy_ += bstack1ll1l11l1l_opy_
        bstack1ll11l111_opy_(context, json.dumps(str(args[0].name) + bstack111_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧૌ") + str(bstack1lll1llll1_opy_)),
                            bstack111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ્"))
        if self.driver_before_scenario:
          bstack1l1l11111_opy_(context, bstack111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ૎"), bstack1llll11l11_opy_)
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ૏") + json.dumps(str(args[0].name) + bstack111_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤૐ") + str(bstack1lll1llll1_opy_)) + bstack111_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫ૑"))
        if self.driver_before_scenario:
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡸࡺࡡࡵࡷࡶࠦ࠿ࠨࡦࡢ࡫࡯ࡩࡩࠨࠬࠡࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠤࠬ૒") + json.dumps(bstack111_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ૓") + str(bstack1llll11l11_opy_)) + bstack111_opy_ (u"ࠧࡾࡿࠪ૔"))
      else:
        bstack1ll11l111_opy_(context, bstack111_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤ૕"), bstack111_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ૖"))
        if self.driver_before_scenario:
          bstack1l1l11111_opy_(context, bstack111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ૗"))
        bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ૘") + json.dumps(str(args[0].name) + bstack111_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ૙")) + bstack111_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ૚"))
        if self.driver_before_scenario:
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠣࡲࡤࡷࡸ࡫ࡤࠣࡿࢀࠫ૛"))
    except Exception as e:
      logger.debug(bstack111_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪ૜").format(str(e)))
  elif name == bstack111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩ૝"):
    try:
      bstack1llll1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1ll11ll_opy_(bstack111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ૞")) else context.browser
      if context.failed is True:
        bstack11lll11ll_opy_ = []
        bstack1llll11ll_opy_ = []
        bstack1lllllllll_opy_ = []
        bstack11ll1llll_opy_ = bstack111_opy_ (u"ࠫࠬ૟")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack11lll11ll_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l1lll111_opy_ = traceback.format_tb(exc_tb)
            bstack1lll1l1l11_opy_ = bstack111_opy_ (u"ࠬࠦࠧૠ").join(bstack1l1lll111_opy_)
            bstack1llll11ll_opy_.append(bstack1lll1l1l11_opy_)
            bstack1lllllllll_opy_.append(bstack1l1lll111_opy_[-1])
        except Exception as e:
          logger.debug(bstack11l11lll_opy_.format(str(e)))
        bstack1llll11l11_opy_ = bstack111_opy_ (u"࠭ࠧૡ")
        for i in range(len(bstack11lll11ll_opy_)):
          bstack1llll11l11_opy_ += bstack11lll11ll_opy_[i] + bstack1lllllllll_opy_[i] + bstack111_opy_ (u"ࠧ࡝ࡰࠪૢ")
        bstack11ll1llll_opy_ = bstack111_opy_ (u"ࠨࠢࠪૣ").join(bstack1llll11ll_opy_)
        if not self.driver_before_scenario:
          bstack1ll11l111_opy_(context, bstack11ll1llll_opy_, bstack111_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ૤"))
          bstack1l1l11111_opy_(context, bstack111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ૥"), bstack1llll11l11_opy_)
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ૦") + json.dumps(bstack11ll1llll_opy_) + bstack111_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬ૧"))
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡹࡴࡢࡶࡸࡷࠧࡀࠢࡧࡣ࡬ࡰࡪࡪࠢ࠭ࠢࠥࡶࡪࡧࡳࡰࡰࠥ࠾ࠥ࠭૨") + json.dumps(bstack111_opy_ (u"ࠢࡔࡱࡰࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢ࡟ࡲࠧ૩") + str(bstack1llll11l11_opy_)) + bstack111_opy_ (u"ࠨࡿࢀࠫ૪"))
      else:
        if not self.driver_before_scenario:
          bstack1ll11l111_opy_(context, bstack111_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧ૫") + str(self.feature.name) + bstack111_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧ૬"), bstack111_opy_ (u"ࠦ࡮ࡴࡦࡰࠤ૭"))
          bstack1l1l11111_opy_(context, bstack111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ૮"))
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ૯") + json.dumps(bstack111_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥ૰") + str(self.feature.name) + bstack111_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥ૱")) + bstack111_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ૲"))
          bstack1llll1ll_opy_.execute_script(bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦࡵࡧࡳࡴࡧࡧࠦࢂࢃࠧ૳"))
    except Exception as e:
      logger.debug(bstack111_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭૴").format(str(e)))
  else:
    bstack1l1lll11_opy_(self, name, context, *args)
  if name in [bstack111_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬ૵"), bstack111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ૶")]:
    bstack1l1lll11_opy_(self, name, context, *args)
    if (name == bstack111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ૷") and self.driver_before_scenario) or (
            name == bstack111_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨ૸") and not self.driver_before_scenario):
      try:
        bstack1llll1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1ll11ll_opy_(bstack111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨૹ")) else context.browser
        bstack1llll1ll_opy_.quit()
      except Exception:
        pass
def bstack1l1l11lll_opy_(config, startdir):
  return bstack111_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣૺ").format(bstack111_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥૻ"))
notset = Notset()
def bstack111l1lll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l11ll1ll_opy_
  if str(name).lower() == bstack111_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬૼ"):
    return bstack111_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧ૽")
  else:
    return bstack1l11ll1ll_opy_(self, name, default, skip)
def bstack11ll1ll1l_opy_(item, when):
  global bstack1ll1ll1l_opy_
  try:
    bstack1ll1ll1l_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll1l1l1l_opy_():
  return
def bstack1ll1llllll_opy_(type, name, status, reason, bstack1111lll11_opy_, bstack1l11ll1l1_opy_):
  bstack11111111_opy_ = {
    bstack111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ૾"): type,
    bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ૿"): {}
  }
  if type == bstack111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ଀"):
    bstack11111111_opy_[bstack111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ଁ")][bstack111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪଂ")] = bstack1111lll11_opy_
    bstack11111111_opy_[bstack111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨଃ")][bstack111_opy_ (u"࠭ࡤࡢࡶࡤࠫ଄")] = json.dumps(str(bstack1l11ll1l1_opy_))
  if type == bstack111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨଅ"):
    bstack11111111_opy_[bstack111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫଆ")][bstack111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧଇ")] = name
  if type == bstack111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ଈ"):
    bstack11111111_opy_[bstack111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧଉ")][bstack111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬଊ")] = status
    if status == bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ଋ"):
      bstack11111111_opy_[bstack111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪଌ")][bstack111_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ଍")] = json.dumps(str(reason))
  bstack11l11111l_opy_ = bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ଎").format(json.dumps(bstack11111111_opy_))
  return bstack11l11111l_opy_
def bstack1l111llll_opy_(item, call, rep):
  global bstack1111l1ll1_opy_
  global bstack1ll1l11l_opy_
  global bstack1l1ll1l11_opy_
  name = bstack111_opy_ (u"ࠪࠫଏ")
  try:
    if rep.when == bstack111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩଐ"):
      bstack1llll111_opy_ = threading.current_thread().bstack11ll111l_opy_
      try:
        if not bstack1l1ll1l11_opy_:
          name = str(rep.nodeid)
          bstack1l1ll1ll1_opy_ = bstack1ll1llllll_opy_(bstack111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭଑"), name, bstack111_opy_ (u"࠭ࠧ଒"), bstack111_opy_ (u"ࠧࠨଓ"), bstack111_opy_ (u"ࠨࠩଔ"), bstack111_opy_ (u"ࠩࠪକ"))
          for driver in bstack1ll1l11l_opy_:
            if bstack1llll111_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll1ll1_opy_)
      except Exception as e:
        logger.debug(bstack111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪଖ").format(str(e)))
      try:
        status = bstack111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫଗ") if rep.outcome.lower() == bstack111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬଘ") else bstack111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ଙ")
        reason = bstack111_opy_ (u"ࠧࠨଚ")
        if (reason != bstack111_opy_ (u"ࠣࠤଛ")):
          try:
            if (threading.current_thread().bstackTestErrorMessages == None):
              threading.current_thread().bstackTestErrorMessages = []
          except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
          threading.current_thread().bstackTestErrorMessages.append(str(reason))
        if status == bstack111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩଜ"):
          reason = rep.longrepr.reprcrash.message
          if (not threading.current_thread().bstackTestErrorMessages):
            threading.current_thread().bstackTestErrorMessages = []
          threading.current_thread().bstackTestErrorMessages.append(reason)
        level = bstack111_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨଝ") if status == bstack111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫଞ") else bstack111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫଟ")
        data = name + bstack111_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨଠ") if status == bstack111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧଡ") else name + bstack111_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫଢ") + reason
        bstack1ll1111l1_opy_ = bstack1ll1llllll_opy_(bstack111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫଣ"), bstack111_opy_ (u"ࠪࠫତ"), bstack111_opy_ (u"ࠫࠬଥ"), bstack111_opy_ (u"ࠬ࠭ଦ"), level, data)
        for driver in bstack1ll1l11l_opy_:
          if bstack1llll111_opy_ == driver.session_id:
            driver.execute_script(bstack1ll1111l1_opy_)
      except Exception as e:
        logger.debug(bstack111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪଧ").format(str(e)))
  except Exception as e:
    logger.debug(bstack111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫନ").format(str(e)))
  bstack1111l1ll1_opy_(item, call, rep)
def bstack1lllll11ll_opy_(framework_name):
  global bstack1lllllll11_opy_
  global bstack1lll11l1l_opy_
  global bstack11l1l1lll_opy_
  bstack1lllllll11_opy_ = framework_name
  logger.info(bstack11l111lll_opy_.format(bstack1lllllll11_opy_.split(bstack111_opy_ (u"ࠨ࠯ࠪ଩"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack111l11l11_opy_:
      Service.start = bstack1llll11ll1_opy_
      Service.stop = bstack1ll1111l_opy_
      webdriver.Remote.get = bstack11llll11l_opy_
      WebDriver.close = bstack111ll111l_opy_
      WebDriver.quit = bstack1l11lll1l_opy_
      webdriver.Remote.__init__ = bstack111ll1111_opy_
    if not bstack111l11l11_opy_ and bstack1111llll_opy_.on():
      webdriver.Remote.__init__ = bstack1ll1l1lll_opy_
    bstack1lll11l1l_opy_ = True
  except Exception as e:
    pass
  bstack11111l111_opy_()
  if not bstack1lll11l1l_opy_:
    bstack111l1ll1l_opy_(bstack111_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦପ"), bstack1111l111l_opy_)
  if bstack1lll1l11l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1lllll11l1_opy_
    except Exception as e:
      logger.error(bstack1ll1ll1ll1_opy_.format(str(e)))
  if (bstack111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩଫ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111l11111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1ll1l11ll_opy_
      except Exception as e:
        logger.warn(bstack1ll111l1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1111111ll_opy_
      except Exception as e:
        logger.debug(bstack1l1l111l_opy_ + str(e))
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1ll111l1_opy_)
    Output.end_test = bstack11l1lll11_opy_
    TestStatus.__init__ = bstack1l1l11ll_opy_
    QueueItem.__init__ = bstack111ll11l1_opy_
    pabot._create_items = bstack1lll1l1l_opy_
    try:
      from pabot import __version__ as bstack1lll1lll1_opy_
      if version.parse(bstack1lll1lll1_opy_) >= version.parse(bstack111_opy_ (u"ࠫ࠷࠴࠱࠶࠰࠳ࠫବ")):
        pabot._run = bstack1lll1111ll_opy_
      elif version.parse(bstack1lll1lll1_opy_) >= version.parse(bstack111_opy_ (u"ࠬ࠸࠮࠲࠵࠱࠴ࠬଭ")):
        pabot._run = bstack111111l1l_opy_
      else:
        pabot._run = bstack11ll1l11l_opy_
    except Exception as e:
      pabot._run = bstack11ll1l11l_opy_
    pabot._create_command_for_execution = bstack1l11l11ll_opy_
    pabot._report_results = bstack11lllll1_opy_
  if bstack111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ମ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1l11l11l1_opy_)
    Runner.run_hook = bstack1ll1lll1ll_opy_
    Step.run = bstack1llll1l11_opy_
  if bstack111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧଯ") in str(framework_name).lower():
    if not bstack111l11l11_opy_:
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
def bstack11lll111_opy_():
  global CONFIG
  if bstack111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨର") in CONFIG and int(CONFIG[bstack111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ଱")]) > 1:
    logger.warn(bstack111l1111_opy_)
def bstack1l1lll11l_opy_(arg, bstack1111l11l1_opy_):
  global CONFIG
  global bstack1l1l1111_opy_
  global bstack1lllll1l1l_opy_
  global bstack111l11l11_opy_
  global bstack1l11ll11l_opy_
  bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪଲ")
  if bstack1111l11l1_opy_ and isinstance(bstack1111l11l1_opy_, str):
    bstack1111l11l1_opy_ = eval(bstack1111l11l1_opy_)
  CONFIG = bstack1111l11l1_opy_[bstack111_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫଳ")]
  bstack1l1l1111_opy_ = bstack1111l11l1_opy_[bstack111_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭଴")]
  bstack1lllll1l1l_opy_ = bstack1111l11l1_opy_[bstack111_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨଵ")]
  bstack111l11l11_opy_ = bstack1111l11l1_opy_[bstack111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪଶ")]
  bstack1l11ll11l_opy_.bstack1l1ll1ll_opy_(bstack111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩଷ"), bstack111l11l11_opy_)
  os.environ[bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫସ")] = bstack1lllll1l11_opy_
  os.environ[bstack111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩହ")] = json.dumps(CONFIG)
  os.environ[bstack111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ଺")] = bstack1l1l1111_opy_
  os.environ[bstack111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭଻")] = str(bstack1lllll1l1l_opy_)
  os.environ[bstack111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒ଼ࠬ")] = str(True)
  if bstack1lll1llll_opy_(arg, [bstack111_opy_ (u"ࠧ࠮ࡰࠪଽ"), bstack111_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩା")]) != -1:
    os.environ[bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪି")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack111l11l1_opy_)
    return
  bstack11lll11l1_opy_()
  global bstack1ll1llll_opy_
  global bstack1lll1l1111_opy_
  global bstack1ll111ll1_opy_
  global bstack1l1l1lll_opy_
  global bstack1l1ll11ll_opy_
  global bstack11l1l1lll_opy_
  global bstack1l11llll_opy_
  arg.append(bstack111_opy_ (u"ࠥ࠱࡜ࠨୀ"))
  arg.append(bstack111_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾ࡒࡵࡤࡶ࡮ࡨࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡭ࡱࡱࡵࡸࡪࡪ࠺ࡱࡻࡷࡩࡸࡺ࠮ࡑࡻࡷࡩࡸࡺࡗࡢࡴࡱ࡭ࡳ࡭ࠢୁ"))
  arg.append(bstack111_opy_ (u"ࠧ࠳ࡗࠣୂ"))
  arg.append(bstack111_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡔࡩࡧࠣ࡬ࡴࡵ࡫ࡪ࡯ࡳࡰࠧୃ"))
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
  if bstack11llll11_opy_(CONFIG):
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
    logger.debug(bstack111_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨୄ"))
  bstack1ll111ll1_opy_ = CONFIG.get(bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୅"), {}).get(bstack111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ୆"))
  bstack1l11llll_opy_ = True
  bstack1lllll11ll_opy_(bstack1ll1ll1111_opy_)
  os.environ[bstack111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫେ")] = CONFIG[bstack111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ୈ")]
  os.environ[bstack111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨ୉")] = CONFIG[bstack111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ୊")]
  os.environ[bstack111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪୋ")] = bstack111l11l11_opy_.__str__()
  from _pytest.config import main as bstack1ll1ll1l11_opy_
  bstack1ll1ll1l11_opy_(arg)
def bstack1l111ll1_opy_(arg):
  bstack1lllll11ll_opy_(bstack1l1l1lll1_opy_)
  from behave.__main__ import main as bstack1l11ll1l_opy_
  bstack1l11ll1l_opy_(arg)
def bstack1ll1l1l11l_opy_():
  logger.info(bstack111111ll1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧୌ"), help=bstack111_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡴࡴࡦࡪࡩ୍ࠪ"))
  parser.add_argument(bstack111_opy_ (u"ࠪ࠱ࡺ࠭୎"), bstack111_opy_ (u"ࠫ࠲࠳ࡵࡴࡧࡵࡲࡦࡳࡥࠨ୏"), help=bstack111_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫ୐"))
  parser.add_argument(bstack111_opy_ (u"࠭࠭࡬ࠩ୑"), bstack111_opy_ (u"ࠧ࠮࠯࡮ࡩࡾ࠭୒"), help=bstack111_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠩ୓"))
  parser.add_argument(bstack111_opy_ (u"ࠩ࠰ࡪࠬ୔"), bstack111_opy_ (u"ࠪ࠱࠲࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ୕"), help=bstack111_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪୖ"))
  bstack1ll1ll11l_opy_ = parser.parse_args()
  try:
    bstack1ll1l1l1l1_opy_ = bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡮ࡦࡴ࡬ࡧ࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩୗ")
    if bstack1ll1ll11l_opy_.framework and bstack1ll1ll11l_opy_.framework not in (bstack111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭୘"), bstack111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ୙")):
      bstack1ll1l1l1l1_opy_ = bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧ୚")
    bstack1l1l1ll11_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1l1l1l1_opy_)
    bstack1111lll1l_opy_ = open(bstack1l1l1ll11_opy_, bstack111_opy_ (u"ࠩࡵࠫ୛"))
    bstack1l11l1ll1_opy_ = bstack1111lll1l_opy_.read()
    bstack1111lll1l_opy_.close()
    if bstack1ll1ll11l_opy_.username:
      bstack1l11l1ll1_opy_ = bstack1l11l1ll1_opy_.replace(bstack111_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪଡ଼"), bstack1ll1ll11l_opy_.username)
    if bstack1ll1ll11l_opy_.key:
      bstack1l11l1ll1_opy_ = bstack1l11l1ll1_opy_.replace(bstack111_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ଢ଼"), bstack1ll1ll11l_opy_.key)
    if bstack1ll1ll11l_opy_.framework:
      bstack1l11l1ll1_opy_ = bstack1l11l1ll1_opy_.replace(bstack111_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭୞"), bstack1ll1ll11l_opy_.framework)
    file_name = bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩୟ")
    file_path = os.path.abspath(file_name)
    bstack1l111l1ll_opy_ = open(file_path, bstack111_opy_ (u"ࠧࡸࠩୠ"))
    bstack1l111l1ll_opy_.write(bstack1l11l1ll1_opy_)
    bstack1l111l1ll_opy_.close()
    logger.info(bstack1llll111l_opy_)
    try:
      os.environ[bstack111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪୡ")] = bstack1ll1ll11l_opy_.framework if bstack1ll1ll11l_opy_.framework != None else bstack111_opy_ (u"ࠤࠥୢ")
      config = yaml.safe_load(bstack1l11l1ll1_opy_)
      config[bstack111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪୣ")] = bstack111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡸ࡫ࡴࡶࡲࠪ୤")
      bstack1l111lll_opy_(bstack111111l1_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll11ll11_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1lll11l11_opy_.format(str(e)))
def bstack1l111lll_opy_(bstack1111lll1_opy_, config, bstack1ll1l1l1ll_opy_={}):
  global bstack111l11l11_opy_
  if not config:
    return
  bstack1111111l1_opy_ = bstack1111l1ll_opy_ if not bstack111l11l11_opy_ else (
    bstack1l1ll111l_opy_ if bstack111_opy_ (u"ࠬࡧࡰࡱࠩ୥") in config else bstack11111l1ll_opy_)
  data = {
    bstack111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ୦"): config[bstack111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ୧")],
    bstack111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ୨"): config[bstack111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ୩")],
    bstack111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ୪"): bstack1111lll1_opy_,
    bstack111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ୫"): {
      bstack111_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ୬"): str(config[bstack111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭୭")]) if bstack111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ୮") in config else bstack111_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ୯"),
      bstack111_opy_ (u"ࠩࡵࡩ࡫࡫ࡲࡳࡧࡵࠫ୰"): bstack1ll1l1ll11_opy_(os.getenv(bstack111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠧୱ"), bstack111_opy_ (u"ࠦࠧ୲"))),
      bstack111_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ୳"): bstack111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭୴"),
      bstack111_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨ୵"): bstack1111111l1_opy_,
      bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ୶"): config[bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ୷")] if config[bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭୸")] else bstack111_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ୹"),
      bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ୺"): str(config[bstack111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ୻")]) if bstack111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୼") in config else bstack111_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ୽"),
      bstack111_opy_ (u"ࠩࡲࡷࠬ୾"): sys.platform,
      bstack111_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ୿"): socket.gethostname()
    }
  }
  update(data[bstack111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ஀")], bstack1ll1l1l1ll_opy_)
  try:
    response = bstack1l1l1111l_opy_(bstack111_opy_ (u"ࠬࡖࡏࡔࡖࠪ஁"), bstack11l111ll1_opy_(bstack111l1l111_opy_), data, {
      bstack111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫஂ"): (config[bstack111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩஃ")], config[bstack111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ஄")])
    })
    if response:
      logger.debug(bstack1ll11ll1l_opy_.format(bstack1111lll1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11l11ll1_opy_.format(str(e)))
def bstack1ll1l1ll11_opy_(framework):
  return bstack111_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨஅ").format(str(framework), __version__) if framework else bstack111_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦஆ").format(
    __version__)
def bstack11lll11l1_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack1ll11ll1_opy_()
    logger.debug(bstack1ll1l1ll_opy_.format(str(CONFIG)))
    bstack1lll111ll1_opy_()
    bstack1l1llll1l_opy_()
  except Exception as e:
    logger.error(bstack111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣஇ") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l1111l1_opy_
  atexit.register(bstack1llll1l111_opy_)
  signal.signal(signal.SIGINT, bstack11lll1ll_opy_)
  signal.signal(signal.SIGTERM, bstack11lll1ll_opy_)
def bstack11l1111l1_opy_(exctype, value, traceback):
  global bstack1ll1l11l_opy_
  try:
    for driver in bstack1ll1l11l_opy_:
      driver.execute_script(
        bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡸࡺࡡࡵࡷࡶࠦ࠿ࠨࡦࡢ࡫࡯ࡩࡩࠨࠬࠡࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠤࠬஈ") + json.dumps(
          bstack111_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤஉ") + str(value)) + bstack111_opy_ (u"ࠧࡾࡿࠪஊ"))
  except Exception:
    pass
  bstack11ll11ll1_opy_(value)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11ll11ll1_opy_(message=bstack111_opy_ (u"ࠨࠩ஋")):
  global CONFIG
  try:
    if message:
      bstack1ll1l1l1ll_opy_ = {
        bstack111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ஌"): str(message)
      }
      bstack1l111lll_opy_(bstack1ll1l11ll1_opy_, CONFIG, bstack1ll1l1l1ll_opy_)
    else:
      bstack1l111lll_opy_(bstack1ll1l11ll1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1lll11l11l_opy_.format(str(e)))
def bstack1lll1ll1ll_opy_(bstack1llllll111_opy_, size):
  bstack1111l1111_opy_ = []
  while len(bstack1llllll111_opy_) > size:
    bstack1ll1lll1l_opy_ = bstack1llllll111_opy_[:size]
    bstack1111l1111_opy_.append(bstack1ll1lll1l_opy_)
    bstack1llllll111_opy_ = bstack1llllll111_opy_[size:]
  bstack1111l1111_opy_.append(bstack1llllll111_opy_)
  return bstack1111l1111_opy_
def bstack1ll111lll_opy_(args):
  if bstack111_opy_ (u"ࠪ࠱ࡲ࠭஍") in args and bstack111_opy_ (u"ࠫࡵࡪࡢࠨஎ") in args:
    return True
  return False
def run_on_browserstack(bstack1llll1l11l_opy_=None, bstack11l1l111_opy_=None, bstack11l1l111l_opy_=False):
  global CONFIG
  global bstack1l1l1111_opy_
  global bstack1lllll1l1l_opy_
  bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠬ࠭ஏ")
  bstack1lll111l_opy_(bstack111l1l1l_opy_, logger)
  if bstack1llll1l11l_opy_ and isinstance(bstack1llll1l11l_opy_, str):
    bstack1llll1l11l_opy_ = eval(bstack1llll1l11l_opy_)
  if bstack1llll1l11l_opy_:
    CONFIG = bstack1llll1l11l_opy_[bstack111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ஐ")]
    bstack1l1l1111_opy_ = bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ஑")]
    bstack1lllll1l1l_opy_ = bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪஒ")]
    bstack1l11ll11l_opy_.bstack1l1ll1ll_opy_(bstack111_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫஓ"), bstack1lllll1l1l_opy_)
    bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪஔ")
  if not bstack11l1l111l_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack111l11l1_opy_)
      return
    if sys.argv[1] == bstack111_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧக") or sys.argv[1] == bstack111_opy_ (u"ࠬ࠳ࡶࠨ஖"):
      logger.info(bstack111_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭஗").format(__version__))
      return
    if sys.argv[1] == bstack111_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭஘"):
      bstack1ll1l1l11l_opy_()
      return
  args = sys.argv
  bstack11lll11l1_opy_()
  global bstack1ll1llll_opy_
  global bstack1l11llll_opy_
  global bstack1111l11ll_opy_
  global bstack1lll1l1111_opy_
  global bstack1ll111ll1_opy_
  global bstack1l1l1lll_opy_
  global bstack1l1111ll1_opy_
  global bstack1l1ll11ll_opy_
  global bstack11l1l1lll_opy_
  if not bstack1lllll1l11_opy_:
    if args[1] == bstack111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨங") or args[1] == bstack111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪச"):
      bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ஛")
      args = args[2:]
    elif args[1] == bstack111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪஜ"):
      bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ஝")
      args = args[2:]
    elif args[1] == bstack111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬஞ"):
      bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ட")
      args = args[2:]
    elif args[1] == bstack111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ஠"):
      bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ஡")
      args = args[2:]
    elif args[1] == bstack111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ஢"):
      bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫண")
      args = args[2:]
    elif args[1] == bstack111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬத"):
      bstack1lllll1l11_opy_ = bstack111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭஥")
      args = args[2:]
    else:
      if not bstack111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ஦") in CONFIG or str(CONFIG[bstack111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ஧")]).lower() in [bstack111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩந"), bstack111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫன")]:
        bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫப")
        args = args[1:]
      elif str(CONFIG[bstack111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ஫")]).lower() == bstack111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ஬"):
        bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭஭")
        args = args[1:]
      elif str(CONFIG[bstack111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫம")]).lower() == bstack111_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨய"):
        bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩர")
        args = args[1:]
      elif str(CONFIG[bstack111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧற")]).lower() == bstack111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬல"):
        bstack1lllll1l11_opy_ = bstack111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ள")
        args = args[1:]
      elif str(CONFIG[bstack111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪழ")]).lower() == bstack111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨவ"):
        bstack1lllll1l11_opy_ = bstack111_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩஶ")
        args = args[1:]
      else:
        os.environ[bstack111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬஷ")] = bstack1lllll1l11_opy_
        bstack11l1l11l_opy_(bstack1llll111l1_opy_)
  global bstack1l11l1l11_opy_
  if bstack1llll1l11l_opy_:
    try:
      os.environ[bstack111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ஸ")] = bstack1lllll1l11_opy_
      bstack1l111lll_opy_(bstack11lll1l11_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1lll11l11l_opy_.format(str(e)))
  global bstack111l1llll_opy_
  global bstack11l111l11_opy_
  global bstack1ll1l111_opy_
  global bstack1111l1l1_opy_
  global bstack1l1l1l1l1_opy_
  global bstack1llll1lll_opy_
  global bstack1ll1ll1lll_opy_
  global bstack111ll1ll_opy_
  global bstack1l1l1ll1_opy_
  global bstack1l1l11ll1_opy_
  global bstack1lll1l11_opy_
  global bstack1l1lll11_opy_
  global bstack1ll1ll11_opy_
  global bstack1111l1lll_opy_
  global bstack1l1111111_opy_
  global bstack1l11ll1ll_opy_
  global bstack1ll1ll1l_opy_
  global bstack1lll11llll_opy_
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
  try:
    import Browser
    from subprocess import Popen
    bstack1l11l1l11_opy_ = Popen.__init__
  except Exception as e:
    pass
  if bstack11llll11_opy_(CONFIG):
    if bstack11111ll11_opy_() < version.parse(bstack11ll11l1l_opy_):
      logger.error(bstack11lll111l_opy_.format(bstack11111ll11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1l1111111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1ll1ll1_opy_.format(str(e)))
  if bstack1lllll1l11_opy_ != bstack111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬஹ") or (bstack1lllll1l11_opy_ == bstack111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭஺") and not bstack1llll1l11l_opy_):
    bstack1lll1111l1_opy_()
  if (bstack1lllll1l11_opy_ in [bstack111_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭஻"), bstack111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ஼"), bstack111_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ஽")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111l11111_opy_
        bstack1l1l1l1l1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll111l1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1111l1l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1l1l111l_opy_ + str(e))
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1ll111l1_opy_)
    if bstack1lllll1l11_opy_ != bstack111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫா"):
      bstack1l1l11l1_opy_()
    bstack1ll1l111_opy_ = Output.end_test
    bstack1llll1lll_opy_ = TestStatus.__init__
    bstack111ll1ll_opy_ = pabot._run
    bstack1l1l1ll1_opy_ = QueueItem.__init__
    bstack1l1l11ll1_opy_ = pabot._create_command_for_execution
    bstack1lll11llll_opy_ = pabot._report_results
  if bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫி"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1l11l11l1_opy_)
    bstack1l1lll11_opy_ = Runner.run_hook
    bstack1ll1ll11_opy_ = Step.run
  if bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬீ"):
    try:
      bstack1111llll_opy_.launch(CONFIG, {
        bstack111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧு"): bstack111_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩூ") if bstack1l1lllll1_opy_() else bstack111_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ௃"),
        bstack111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭௄"): bstack11ll1lll_opy_.version(),
        bstack111_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ௅"): __version__
      })
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
      logger.debug(bstack111_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬெ"))
  if bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬே"):
    bstack1l11llll_opy_ = True
    if bstack1llll1l11l_opy_ and bstack11l1l111l_opy_:
      bstack1ll111ll1_opy_ = CONFIG.get(bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪை"), {}).get(bstack111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௉"))
      bstack1lllll11ll_opy_(bstack1llll1ll1_opy_)
    elif bstack1llll1l11l_opy_:
      bstack1ll111ll1_opy_ = CONFIG.get(bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬொ"), {}).get(bstack111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫோ"))
      global bstack1ll1l11l_opy_
      try:
        if bstack1ll111lll_opy_(bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ௌ")]) and multiprocessing.current_process().name == bstack111_opy_ (u"ࠫ࠵்࠭"):
          bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௎")].remove(bstack111_opy_ (u"࠭࠭࡮ࠩ௏"))
          bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪௐ")].remove(bstack111_opy_ (u"ࠨࡲࡧࡦࠬ௑"))
          bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ௒")] = bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௓")][0]
          with open(bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௔")], bstack111_opy_ (u"ࠬࡸࠧ௕")) as f:
            bstack11ll11ll_opy_ = f.read()
          bstack1l111l11l_opy_ = bstack111_opy_ (u"ࠨࠢࠣࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡤ࡬ࠢ࡬ࡱࡵࡵࡲࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡀࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࠪࡾࢁ࠮ࡁࠠࡧࡴࡲࡱࠥࡶࡤࡣࠢ࡬ࡱࡵࡵࡲࡵࠢࡓࡨࡧࡁࠠࡰࡩࡢࡨࡧࠦ࠽ࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱ࠻ࠋࡦࡨࡪࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠩࡵࡨࡰ࡫࠲ࠠࡢࡴࡪ࠰ࠥࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠡ࠿ࠣ࠴࠮ࡀࠊࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࡦࡸࡧࠡ࠿ࠣࡷࡹࡸࠨࡪࡰࡷࠬࡦࡸࡧࠪ࠭࠴࠴࠮ࠐࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࡱࡣࡶࡷࠏࠦࠠࡰࡩࡢࡨࡧ࠮ࡳࡦ࡮ࡩ࠰ࡦࡸࡧ࠭ࡶࡨࡱࡵࡵࡲࡢࡴࡼ࠭ࠏࡖࡤࡣ࠰ࡧࡳࡤࡨࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮ࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥ௖").format(str(bstack1llll1l11l_opy_))
          bstack1llll111ll_opy_ = bstack1l111l11l_opy_ + bstack11ll11ll_opy_
          bstack1ll1l1ll1l_opy_ = bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪௗ")] + bstack111_opy_ (u"ࠨࡡࡥࡷࡹࡧࡣ࡬ࡡࡷࡩࡲࡶ࠮ࡱࡻࠪ௘")
          with open(bstack1ll1l1ll1l_opy_, bstack111_opy_ (u"ࠩࡺࠫ௙")):
            pass
          with open(bstack1ll1l1ll1l_opy_, bstack111_opy_ (u"ࠥࡻ࠰ࠨ௚")) as f:
            f.write(bstack1llll111ll_opy_)
          import subprocess
          bstack1lll1lll11_opy_ = subprocess.run([bstack111_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦ௛"), bstack1ll1l1ll1l_opy_])
          if os.path.exists(bstack1ll1l1ll1l_opy_):
            os.unlink(bstack1ll1l1ll1l_opy_)
          os._exit(bstack1lll1lll11_opy_.returncode)
        else:
          if bstack1ll111lll_opy_(bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௜")]):
            bstack1llll1l11l_opy_[bstack111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௝")].remove(bstack111_opy_ (u"ࠧ࠮࡯ࠪ௞"))
            bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ௟")].remove(bstack111_opy_ (u"ࠩࡳࡨࡧ࠭௠"))
            bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௡")] = bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௢")][0]
          bstack1lllll11ll_opy_(bstack1llll1ll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௣")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨ௤")] = bstack111_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩ௥")
          mod_globals[bstack111_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪ௦")] = os.path.abspath(bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ௧")])
          exec(open(bstack1llll1l11l_opy_[bstack111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௨")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111_opy_ (u"ࠫࡈࡧࡵࡨࡪࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠫ௩").format(str(e)))
          for driver in bstack1ll1l11l_opy_:
            bstack11l1l111_opy_.append({
              bstack111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ௪"): bstack1llll1l11l_opy_[bstack111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௫")],
              bstack111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭௬"): str(e),
              bstack111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ௭"): multiprocessing.current_process().name
            })
            driver.execute_script(
              bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠥࡪࡦ࡯࡬ࡦࡦࠥ࠰ࠥࠨࡲࡦࡣࡶࡳࡳࠨ࠺ࠡࠩ௮") + json.dumps(
                bstack111_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨ௯") + str(e)) + bstack111_opy_ (u"ࠫࢂࢃࠧ௰"))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1ll1l11l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      bstack1l1111l1_opy_()
      bstack11lll111_opy_()
      bstack1111l11l1_opy_ = {
        bstack111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௱"): args[0],
        bstack111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭௲"): CONFIG,
        bstack111_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ௳"): bstack1l1l1111_opy_,
        bstack111_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ௴"): bstack1lllll1l1l_opy_
      }
      if bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ௵") in CONFIG:
        bstack1llll1l1ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack11l11l1ll_opy_ = manager.list()
        if bstack1ll111lll_opy_(args):
          for index, platform in enumerate(CONFIG[bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭௶")]):
            if index == 0:
              bstack1111l11l1_opy_[bstack111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௷")] = args
            bstack1llll1l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1111l11l1_opy_, bstack11l11l1ll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௸")]):
            bstack1llll1l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1111l11l1_opy_, bstack11l11l1ll_opy_)))
        for t in bstack1llll1l1ll_opy_:
          t.start()
        for t in bstack1llll1l1ll_opy_:
          t.join()
        bstack1l1111ll1_opy_ = list(bstack11l11l1ll_opy_)
      else:
        if bstack1ll111lll_opy_(args):
          bstack1111l11l1_opy_[bstack111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௹")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1111l11l1_opy_,))
          test.start()
          test.join()
        else:
          bstack1lllll11ll_opy_(bstack1llll1ll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ௺")] = bstack111_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ௻")
          mod_globals[bstack111_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ௼")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ௽") or bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ௾"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1ll111l1_opy_)
    bstack1l1111l1_opy_()
    bstack1lllll11ll_opy_(bstack1llll1lll1_opy_)
    if bstack111_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ௿") in args:
      i = args.index(bstack111_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫఀ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1ll1llll_opy_))
    args.insert(0, str(bstack111_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఁ")))
    pabot.main(args)
  elif bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩం"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1ll111l1_opy_)
    for a in args:
      if bstack111_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨః") in a:
        bstack1lll1l1111_opy_ = int(a.split(bstack111_opy_ (u"ࠪ࠾ࠬఄ"))[1])
      if bstack111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨఅ") in a:
        bstack1ll111ll1_opy_ = str(a.split(bstack111_opy_ (u"ࠬࡀࠧఆ"))[1])
      if bstack111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ఇ") in a:
        bstack1l1l1lll_opy_ = str(a.split(bstack111_opy_ (u"ࠧ࠻ࠩఈ"))[1])
    bstack1lll1ll1l_opy_ = None
    if bstack111_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧఉ") in args:
      i = args.index(bstack111_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨఊ"))
      args.pop(i)
      bstack1lll1ll1l_opy_ = args.pop(i)
    if bstack1lll1ll1l_opy_ is not None:
      global bstack1l111l1l_opy_
      bstack1l111l1l_opy_ = bstack1lll1ll1l_opy_
    bstack1lllll11ll_opy_(bstack1llll1lll1_opy_)
    run_cli(args)
  elif bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪఋ"):
    bstack1l11l1ll_opy_ = bstack11ll1lll_opy_(args, logger, CONFIG, bstack111l11l11_opy_)
    bstack1l11l1ll_opy_.bstack1l11ll111_opy_()
    bstack1l1111l1_opy_()
    bstack1111l11ll_opy_ = True
    bstack11l1l1lll_opy_ = bstack1l11l1ll_opy_.bstack1l1ll1l1l_opy_()
    bstack1l11l1ll_opy_.bstack1111l11l1_opy_(bstack1l1ll1l11_opy_)
    bstack1l1ll11ll_opy_ = bstack1l11l1ll_opy_.bstack1l1lll1ll_opy_(bstack1l1lll11l_opy_, {
      bstack111_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬఌ"): bstack1l1l1111_opy_,
      bstack111_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ఍"): bstack1lllll1l1l_opy_,
      bstack111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩఎ"): bstack111l11l11_opy_
    })
  elif bstack1lllll1l11_opy_ == bstack111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧఏ"):
    try:
      from behave.__main__ import main as bstack1l11ll1l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack111l1ll1l_opy_(e, bstack1l11l11l1_opy_)
    bstack1l1111l1_opy_()
    bstack1111l11ll_opy_ = True
    bstack1l111l1l1_opy_ = 1
    if bstack111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨఐ") in CONFIG:
      bstack1l111l1l1_opy_ = CONFIG[bstack111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ఑")]
    bstack1ll1lll111_opy_ = int(bstack1l111l1l1_opy_) * int(len(CONFIG[bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఒ")]))
    config = Configuration(args)
    bstack1llllll11l_opy_ = config.paths
    if len(bstack1llllll11l_opy_) == 0:
      import glob
      pattern = bstack111_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪఓ")
      bstack111l11ll1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack111l11ll1_opy_)
      config = Configuration(args)
      bstack1llllll11l_opy_ = config.paths
    bstack111l1111l_opy_ = [os.path.normpath(item) for item in bstack1llllll11l_opy_]
    bstack1ll1l1l1_opy_ = [os.path.normpath(item) for item in args]
    bstack11lll1111_opy_ = [item for item in bstack1ll1l1l1_opy_ if item not in bstack111l1111l_opy_]
    import platform as pf
    if pf.system().lower() == bstack111_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭ఔ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111l1111l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11ll1ll1_opy_)))
                    for bstack11ll1ll1_opy_ in bstack111l1111l_opy_]
    bstack1l11lllll_opy_ = []
    for spec in bstack111l1111l_opy_:
      bstack1lllll1ll1_opy_ = []
      bstack1lllll1ll1_opy_ += bstack11lll1111_opy_
      bstack1lllll1ll1_opy_.append(spec)
      bstack1l11lllll_opy_.append(bstack1lllll1ll1_opy_)
    execution_items = []
    for bstack1lllll1ll1_opy_ in bstack1l11lllll_opy_:
      for index, _ in enumerate(CONFIG[bstack111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩక")]):
        item = {}
        item[bstack111_opy_ (u"ࠧࡢࡴࡪࠫఖ")] = bstack111_opy_ (u"ࠨࠢࠪగ").join(bstack1lllll1ll1_opy_)
        item[bstack111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨఘ")] = index
        execution_items.append(item)
    bstack1llll1111l_opy_ = bstack1lll1ll1ll_opy_(execution_items, bstack1ll1lll111_opy_)
    for execution_item in bstack1llll1111l_opy_:
      bstack1llll1l1ll_opy_ = []
      for item in execution_item:
        bstack1llll1l1ll_opy_.append(bstack1ll1l111l_opy_(name=str(item[bstack111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩఙ")]),
                                             target=bstack1l111ll1_opy_,
                                             args=(item[bstack111_opy_ (u"ࠫࡦࡸࡧࠨచ")],)))
      for t in bstack1llll1l1ll_opy_:
        t.start()
      for t in bstack1llll1l1ll_opy_:
        t.join()
  else:
    bstack11l1l11l_opy_(bstack1llll111l1_opy_)
  if not bstack1llll1l11l_opy_:
    bstack11ll11l1_opy_()
def browserstack_initialize(bstack11llllll_opy_=None):
  run_on_browserstack(bstack11llllll_opy_, None, True)
def bstack11ll11l1_opy_():
  bstack1111llll_opy_.stop()
  bstack1111llll_opy_.bstack11l111l1_opy_()
  [bstack111l111l_opy_, bstack1ll1ll111l_opy_] = bstack1lll1l11ll_opy_()
  if bstack111l111l_opy_ is not None and bstack111l11lll_opy_() != -1:
    sessions = bstack11llll111_opy_(bstack111l111l_opy_)
    bstack1ll1lll1_opy_(sessions, bstack1ll1ll111l_opy_)
def bstack1l1llllll_opy_(bstack111l1lll1_opy_):
  if bstack111l1lll1_opy_:
    return bstack111l1lll1_opy_.capitalize()
  else:
    return bstack111l1lll1_opy_
def bstack1lll1l111l_opy_(bstack1ll11lll_opy_):
  if bstack111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪఛ") in bstack1ll11lll_opy_ and bstack1ll11lll_opy_[bstack111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫజ")] != bstack111_opy_ (u"ࠧࠨఝ"):
    return bstack1ll11lll_opy_[bstack111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ఞ")]
  else:
    bstack1llllllll_opy_ = bstack111_opy_ (u"ࠤࠥట")
    if bstack111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪఠ") in bstack1ll11lll_opy_ and bstack1ll11lll_opy_[bstack111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫడ")] != None:
      bstack1llllllll_opy_ += bstack1ll11lll_opy_[bstack111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬఢ")] + bstack111_opy_ (u"ࠨࠬࠡࠤణ")
      if bstack1ll11lll_opy_[bstack111_opy_ (u"ࠧࡰࡵࠪత")] == bstack111_opy_ (u"ࠣ࡫ࡲࡷࠧథ"):
        bstack1llllllll_opy_ += bstack111_opy_ (u"ࠤ࡬ࡓࡘࠦࠢద")
      bstack1llllllll_opy_ += (bstack1ll11lll_opy_[bstack111_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧధ")] or bstack111_opy_ (u"ࠫࠬన"))
      return bstack1llllllll_opy_
    else:
      bstack1llllllll_opy_ += bstack1l1llllll_opy_(bstack1ll11lll_opy_[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭఩")]) + bstack111_opy_ (u"ࠨࠠࠣప") + (
              bstack1ll11lll_opy_[bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩఫ")] or bstack111_opy_ (u"ࠨࠩబ")) + bstack111_opy_ (u"ࠤ࠯ࠤࠧభ")
      if bstack1ll11lll_opy_[bstack111_opy_ (u"ࠪࡳࡸ࠭మ")] == bstack111_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧయ"):
        bstack1llllllll_opy_ += bstack111_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥర")
      bstack1llllllll_opy_ += bstack1ll11lll_opy_[bstack111_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪఱ")] or bstack111_opy_ (u"ࠧࠨల")
      return bstack1llllllll_opy_
def bstack1lllll111l_opy_(bstack1ll1l11l1_opy_):
  if bstack1ll1l11l1_opy_ == bstack111_opy_ (u"ࠣࡦࡲࡲࡪࠨళ"):
    return bstack111_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬఴ")
  elif bstack1ll1l11l1_opy_ == bstack111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥవ"):
    return bstack111_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧశ")
  elif bstack1ll1l11l1_opy_ == bstack111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧష"):
    return bstack111_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭స")
  elif bstack1ll1l11l1_opy_ == bstack111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨహ"):
    return bstack111_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ఺")
  elif bstack1ll1l11l1_opy_ == bstack111_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥ఻"):
    return bstack111_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ఼")
  elif bstack1ll1l11l1_opy_ == bstack111_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧఽ"):
    return bstack111_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ా")
  else:
    return bstack111_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪి") + bstack1l1llllll_opy_(
      bstack1ll1l11l1_opy_) + bstack111_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ీ")
def bstack1111l11l_opy_(session):
  return bstack111_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨు").format(
    session[bstack111_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ూ")], bstack1lll1l111l_opy_(session), bstack1lllll111l_opy_(session[bstack111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩృ")]),
    bstack1lllll111l_opy_(session[bstack111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫౄ")]),
    bstack1l1llllll_opy_(session[bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭౅")] or session[bstack111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ె")] or bstack111_opy_ (u"ࠧࠨే")) + bstack111_opy_ (u"ࠣࠢࠥై") + (session[bstack111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ౉")] or bstack111_opy_ (u"ࠪࠫొ")),
    session[bstack111_opy_ (u"ࠫࡴࡹࠧో")] + bstack111_opy_ (u"ࠧࠦࠢౌ") + session[bstack111_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰ్ࠪ")], session[bstack111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ౎")] or bstack111_opy_ (u"ࠨࠩ౏"),
    session[bstack111_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭౐")] if session[bstack111_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧ౑")] else bstack111_opy_ (u"ࠫࠬ౒"))
def bstack1ll1lll1_opy_(sessions, bstack1ll1ll111l_opy_):
  try:
    bstack11l1l11l1_opy_ = bstack111_opy_ (u"ࠧࠨ౓")
    if not os.path.exists(bstack1lll1l11l_opy_):
      os.mkdir(bstack1lll1l11l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫ౔")), bstack111_opy_ (u"ࠧࡳౕࠩ")) as f:
      bstack11l1l11l1_opy_ = f.read()
    bstack11l1l11l1_opy_ = bstack11l1l11l1_opy_.replace(bstack111_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁౖࠬ"), str(len(sessions)))
    bstack11l1l11l1_opy_ = bstack11l1l11l1_opy_.replace(bstack111_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩ౗"), bstack1ll1ll111l_opy_)
    bstack11l1l11l1_opy_ = bstack11l1l11l1_opy_.replace(bstack111_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫౘ"),
                                              sessions[0].get(bstack111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨౙ")) if sessions[0] else bstack111_opy_ (u"ࠬ࠭ౚ"))
    with open(os.path.join(bstack1lll1l11l_opy_, bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪ౛")), bstack111_opy_ (u"ࠧࡸࠩ౜")) as stream:
      stream.write(bstack11l1l11l1_opy_.split(bstack111_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬౝ"))[0])
      for session in sessions:
        stream.write(bstack1111l11l_opy_(session))
      stream.write(bstack11l1l11l1_opy_.split(bstack111_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭౞"))[1])
    logger.info(bstack111_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭౟").format(bstack1lll1l11l_opy_));
  except Exception as e:
    logger.debug(bstack1l11lll1_opy_.format(str(e)))
def bstack11llll111_opy_(bstack111l111l_opy_):
  global CONFIG
  try:
    host = bstack111_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧౠ") if bstack111_opy_ (u"ࠬࡧࡰࡱࠩౡ") in CONFIG else bstack111_opy_ (u"࠭ࡡࡱ࡫ࠪౢ")
    user = CONFIG[bstack111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩౣ")]
    key = CONFIG[bstack111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ౤")]
    bstack1ll11l11l_opy_ = bstack111_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ౥") if bstack111_opy_ (u"ࠪࡥࡵࡶࠧ౦") in CONFIG else bstack111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭౧")
    url = bstack111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪ౨").format(user, key, host, bstack1ll11l11l_opy_,
                                                                                bstack111l111l_opy_)
    headers = {
      bstack111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬ౩"): bstack111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ౪"),
    }
    proxies = bstack1lllll1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭౫")], response.json()))
  except Exception as e:
    logger.debug(bstack1l1ll111_opy_.format(str(e)))
def bstack1lll1l11ll_opy_():
  global CONFIG
  try:
    if bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ౬") in CONFIG:
      host = bstack111_opy_ (u"ࠪࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠭౭") if bstack111_opy_ (u"ࠫࡦࡶࡰࠨ౮") in CONFIG else bstack111_opy_ (u"ࠬࡧࡰࡪࠩ౯")
      user = CONFIG[bstack111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ౰")]
      key = CONFIG[bstack111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ౱")]
      bstack1ll11l11l_opy_ = bstack111_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ౲") if bstack111_opy_ (u"ࠩࡤࡴࡵ࠭౳") in CONFIG else bstack111_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ౴")
      url = bstack111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࢀࢃ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠴ࡪࡴࡱࡱࠫ౵").format(user, key, host, bstack1ll11l11l_opy_)
      headers = {
        bstack111_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ౶"): bstack111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ౷"),
      }
      if bstack111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ౸") in CONFIG:
        params = {bstack111_opy_ (u"ࠨࡰࡤࡱࡪ࠭౹"): CONFIG[bstack111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ౺")], bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭౻"): CONFIG[bstack111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭౼")]}
      else:
        params = {bstack111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ౽"): CONFIG[bstack111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ౾")]}
      proxies = bstack1lllll1ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack11l1lll1_opy_ = response.json()[0][bstack111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡧࡻࡩ࡭ࡦࠪ౿")]
        if bstack11l1lll1_opy_:
          bstack1ll1ll111l_opy_ = bstack11l1lll1_opy_[bstack111_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬಀ")].split(bstack111_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤ࠯ࡥࡹ࡮ࡲࡤࠨಁ"))[0] + bstack111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵ࠲ࠫಂ") + bstack11l1lll1_opy_[
            bstack111_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧಃ")]
          logger.info(bstack1l111111_opy_.format(bstack1ll1ll111l_opy_))
          bstack11111llll_opy_ = CONFIG[bstack111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ಄")]
          if bstack111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨಅ") in CONFIG:
            bstack11111llll_opy_ += bstack111_opy_ (u"ࠧࠡࠩಆ") + CONFIG[bstack111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪಇ")]
          if bstack11111llll_opy_ != bstack11l1lll1_opy_[bstack111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧಈ")]:
            logger.debug(bstack1l11l1111_opy_.format(bstack11l1lll1_opy_[bstack111_opy_ (u"ࠪࡲࡦࡳࡥࠨಉ")], bstack11111llll_opy_))
          return [bstack11l1lll1_opy_[bstack111_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧಊ")], bstack1ll1ll111l_opy_]
    else:
      logger.warn(bstack11ll1l1ll_opy_)
  except Exception as e:
    logger.debug(bstack1111ll11l_opy_.format(str(e)))
  return [None, None]
def bstack1l1l1l11_opy_(url, bstack111ll1l1_opy_=False):
  global CONFIG
  global bstack11111l11_opy_
  if not bstack11111l11_opy_:
    hostname = bstack1ll1llll11_opy_(url)
    is_private = bstack1111ll1l_opy_(hostname)
    if (bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩಋ") in CONFIG and not CONFIG[bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಌ")]) and (is_private or bstack111ll1l1_opy_):
      bstack11111l11_opy_ = hostname
def bstack1ll1llll11_opy_(url):
  return urlparse(url).hostname
def bstack1111ll1l_opy_(hostname):
  for bstack1111llll1_opy_ in bstack11llll1ll_opy_:
    regex = re.compile(bstack1111llll1_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1ll1ll11ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False