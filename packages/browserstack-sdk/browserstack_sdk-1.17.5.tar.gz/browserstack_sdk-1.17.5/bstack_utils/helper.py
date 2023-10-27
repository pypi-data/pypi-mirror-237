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
import os
import re
import subprocess
import traceback
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack1ll111ll11_opy_, bstack11llll1ll_opy_, bstack1l111ll1l_opy_, bstack1lll111ll_opy_
from bstack_utils.messages import bstack111l1l1ll_opy_
from bstack_utils.proxy import bstack1lllll1ll_opy_
bstack1l11ll11l_opy_ = Config.get_instance()
def bstack1l1ll1l1ll_opy_(config):
    return config[bstack111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭໤")]
def bstack1l1ll1l11l_opy_(config):
    return config[bstack111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ໥")]
def bstack1l1ll11lll_opy_(obj):
    values = []
    bstack1l1ll1l1l1_opy_ = re.compile(bstack111_opy_ (u"ࡸࠢ࡟ࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤࡢࡤࠬࠦࠥ໦"), re.I)
    for key in obj.keys():
        if bstack1l1ll1l1l1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1l1llll1ll_opy_(config):
    tags = []
    tags.extend(bstack1l1ll11lll_opy_(os.environ))
    tags.extend(bstack1l1ll11lll_opy_(config))
    return tags
def bstack1ll11111ll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1ll111111l_opy_(bstack1l1lll11l1_opy_):
    if not bstack1l1lll11l1_opy_:
        return bstack111_opy_ (u"ࠧࠨ໧")
    return bstack111_opy_ (u"ࠣࡽࢀࠤ࠭ࢁࡽࠪࠤ໨").format(bstack1l1lll11l1_opy_.name, bstack1l1lll11l1_opy_.email)
def bstack1l1ll1ll11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1ll111l111_opy_ = repo.common_dir
        info = {
            bstack111_opy_ (u"ࠤࡶ࡬ࡦࠨ໩"): repo.head.commit.hexsha,
            bstack111_opy_ (u"ࠥࡷ࡭ࡵࡲࡵࡡࡶ࡬ࡦࠨ໪"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111_opy_ (u"ࠦࡧࡸࡡ࡯ࡥ࡫ࠦ໫"): repo.active_branch.name,
            bstack111_opy_ (u"ࠧࡺࡡࡨࠤ໬"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࠤ໭"): bstack1ll111111l_opy_(repo.head.commit.committer),
            bstack111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࡢࡨࡦࡺࡥࠣ໮"): repo.head.commit.committed_datetime.isoformat(),
            bstack111_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࠣ໯"): bstack1ll111111l_opy_(repo.head.commit.author),
            bstack111_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡡࡧࡥࡹ࡫ࠢ໰"): repo.head.commit.authored_datetime.isoformat(),
            bstack111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦ໱"): repo.head.commit.message,
            bstack111_opy_ (u"ࠦࡷࡵ࡯ࡵࠤ໲"): repo.git.rev_parse(bstack111_opy_ (u"ࠧ࠳࠭ࡴࡪࡲࡻ࠲ࡺ࡯ࡱ࡮ࡨࡺࡪࡲࠢ໳")),
            bstack111_opy_ (u"ࠨࡣࡰ࡯ࡰࡳࡳࡥࡧࡪࡶࡢࡨ࡮ࡸࠢ໴"): bstack1ll111l111_opy_,
            bstack111_opy_ (u"ࠢࡸࡱࡵ࡯ࡹࡸࡥࡦࡡࡪ࡭ࡹࡥࡤࡪࡴࠥ໵"): subprocess.check_output([bstack111_opy_ (u"ࠣࡩ࡬ࡸࠧ໶"), bstack111_opy_ (u"ࠤࡵࡩࡻ࠳ࡰࡢࡴࡶࡩࠧ໷"), bstack111_opy_ (u"ࠥ࠱࠲࡭ࡩࡵ࠯ࡦࡳࡲࡳ࡯࡯࠯ࡧ࡭ࡷࠨ໸")]).strip().decode(
                bstack111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ໹")),
            bstack111_opy_ (u"ࠧࡲࡡࡴࡶࡢࡸࡦ࡭ࠢ໺"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡹ࡟ࡴ࡫ࡱࡧࡪࡥ࡬ࡢࡵࡷࡣࡹࡧࡧࠣ໻"): repo.git.rev_list(
                bstack111_opy_ (u"ࠢࡼࡿ࠱࠲ࢀࢃࠢ໼").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1l1lllllll_opy_ = []
        for remote in remotes:
            bstack1ll1111l11_opy_ = {
                bstack111_opy_ (u"ࠣࡰࡤࡱࡪࠨ໽"): remote.name,
                bstack111_opy_ (u"ࠤࡸࡶࡱࠨ໾"): remote.url,
            }
            bstack1l1lllllll_opy_.append(bstack1ll1111l11_opy_)
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥࠣ໿"): bstack111_opy_ (u"ࠦ࡬࡯ࡴࠣༀ"),
            **info,
            bstack111_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡸࠨ༁"): bstack1l1lllllll_opy_
        }
    except Exception as err:
        print(bstack111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤ༂").format(err))
        return {}
def bstack11l1l1ll_opy_():
    env = os.environ
    if (bstack111_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧ༃") in env and len(env[bstack111_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ༄")]) > 0) or (
            bstack111_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣ༅") in env and len(env[bstack111_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ༆")]) > 0):
        return {
            bstack111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ༇"): bstack111_opy_ (u"ࠧࡐࡥ࡯࡭࡬ࡲࡸࠨ༈"),
            bstack111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ༉"): env.get(bstack111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ༊")),
            bstack111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ་"): env.get(bstack111_opy_ (u"ࠤࡍࡓࡇࡥࡎࡂࡏࡈࠦ༌")),
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ།"): env.get(bstack111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ༎"))
        }
    if env.get(bstack111_opy_ (u"ࠧࡉࡉࠣ༏")) == bstack111_opy_ (u"ࠨࡴࡳࡷࡨࠦ༐") and bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋࡃࡊࠤ༑"))):
        return {
            bstack111_opy_ (u"ࠣࡰࡤࡱࡪࠨ༒"): bstack111_opy_ (u"ࠤࡆ࡭ࡷࡩ࡬ࡦࡅࡌࠦ༓"),
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ༔"): env.get(bstack111_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ༕")),
            bstack111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ༖"): env.get(bstack111_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡊࡐࡄࠥ༗")),
            bstack111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ༘"): env.get(bstack111_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐ༙ࠦ"))
        }
    if env.get(bstack111_opy_ (u"ࠤࡆࡍࠧ༚")) == bstack111_opy_ (u"ࠥࡸࡷࡻࡥࠣ༛") and bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࠦ༜"))):
        return {
            bstack111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ༝"): bstack111_opy_ (u"ࠨࡔࡳࡣࡹ࡭ࡸࠦࡃࡊࠤ༞"),
            bstack111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ༟"): env.get(bstack111_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡘࡇࡅࡣ࡚ࡘࡌࠣ༠")),
            bstack111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ༡"): env.get(bstack111_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ༢")),
            bstack111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ༣"): env.get(bstack111_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ༤"))
        }
    if env.get(bstack111_opy_ (u"ࠨࡃࡊࠤ༥")) == bstack111_opy_ (u"ࠢࡵࡴࡸࡩࠧ༦") and env.get(bstack111_opy_ (u"ࠣࡅࡌࡣࡓࡇࡍࡆࠤ༧")) == bstack111_opy_ (u"ࠤࡦࡳࡩ࡫ࡳࡩ࡫ࡳࠦ༨"):
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥࠣ༩"): bstack111_opy_ (u"ࠦࡈࡵࡤࡦࡵ࡫࡭ࡵࠨ༪"),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ༫"): None,
            bstack111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ༬"): None,
            bstack111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ༭"): None
        }
    if env.get(bstack111_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇࡘࡁࡏࡅࡋࠦ༮")) and env.get(bstack111_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡉࡏࡎࡏࡌࡘࠧ༯")):
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥࠣ༰"): bstack111_opy_ (u"ࠦࡇ࡯ࡴࡣࡷࡦ࡯ࡪࡺࠢ༱"),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ༲"): env.get(bstack111_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡊࡍ࡙ࡥࡈࡕࡖࡓࡣࡔࡘࡉࡈࡋࡑࠦ༳")),
            bstack111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ༴"): None,
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸ༵ࠢ"): env.get(bstack111_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ༶"))
        }
    if env.get(bstack111_opy_ (u"ࠥࡇࡎࠨ༷")) == bstack111_opy_ (u"ࠦࡹࡸࡵࡦࠤ༸") and bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠧࡊࡒࡐࡐࡈ༹ࠦ"))):
        return {
            bstack111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ༺"): bstack111_opy_ (u"ࠢࡅࡴࡲࡲࡪࠨ༻"),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ༼"): env.get(bstack111_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡍࡋࡑࡏࠧ༽")),
            bstack111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ༾"): None,
            bstack111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ༿"): env.get(bstack111_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥཀ"))
        }
    if env.get(bstack111_opy_ (u"ࠨࡃࡊࠤཁ")) == bstack111_opy_ (u"ࠢࡵࡴࡸࡩࠧག") and bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࠦགྷ"))):
        return {
            bstack111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢང"): bstack111_opy_ (u"ࠥࡗࡪࡳࡡࡱࡪࡲࡶࡪࠨཅ"),
            bstack111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢཆ"): env.get(bstack111_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡑࡕࡋࡆࡔࡉ࡛ࡃࡗࡍࡔࡔ࡟ࡖࡔࡏࠦཇ")),
            bstack111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ཈"): env.get(bstack111_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧཉ")),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢཊ"): env.get(bstack111_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡌࡈࠧཋ"))
        }
    if env.get(bstack111_opy_ (u"ࠥࡇࡎࠨཌ")) == bstack111_opy_ (u"ࠦࡹࡸࡵࡦࠤཌྷ") and bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠧࡍࡉࡕࡎࡄࡆࡤࡉࡉࠣཎ"))):
        return {
            bstack111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦཏ"): bstack111_opy_ (u"ࠢࡈ࡫ࡷࡐࡦࡨࠢཐ"),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦད"): env.get(bstack111_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡘࡖࡑࠨདྷ")),
            bstack111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧན"): env.get(bstack111_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤཔ")),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦཕ"): env.get(bstack111_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡉࡅࠤབ"))
        }
    if env.get(bstack111_opy_ (u"ࠢࡄࡋࠥབྷ")) == bstack111_opy_ (u"ࠣࡶࡵࡹࡪࠨམ") and bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࠧཙ"))):
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥࠣཚ"): bstack111_opy_ (u"ࠦࡇࡻࡩ࡭ࡦ࡮࡭ࡹ࡫ࠢཛ"),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣཛྷ"): env.get(bstack111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧཝ")),
            bstack111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤཞ"): env.get(bstack111_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡑࡇࡂࡆࡎࠥཟ")) or env.get(bstack111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧའ")),
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤཡ"): env.get(bstack111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨར"))
        }
    if bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢལ"))):
        return {
            bstack111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦཤ"): bstack111_opy_ (u"ࠢࡗ࡫ࡶࡹࡦࡲࠠࡔࡶࡸࡨ࡮ࡵࠠࡕࡧࡤࡱ࡙ࠥࡥࡳࡸ࡬ࡧࡪࡹࠢཥ"),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦས"): bstack111_opy_ (u"ࠤࡾࢁࢀࢃࠢཧ").format(env.get(bstack111_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭ཨ")), env.get(bstack111_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࡋࡇࠫཀྵ"))),
            bstack111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢཪ"): env.get(bstack111_opy_ (u"ࠨࡓ࡚ࡕࡗࡉࡒࡥࡄࡆࡈࡌࡒࡎ࡚ࡉࡐࡐࡌࡈࠧཫ")),
            bstack111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨཬ"): env.get(bstack111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣ཭"))
        }
    if bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࠦ཮"))):
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥࠣ཯"): bstack111_opy_ (u"ࠦࡆࡶࡰࡷࡧࡼࡳࡷࠨ཰"),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ཱࠣ"): bstack111_opy_ (u"ࠨࡻࡾ࠱ࡳࡶࡴࡰࡥࡤࡶ࠲ࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁིࠧ").format(env.get(bstack111_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡘࡖࡑཱི࠭")), env.get(bstack111_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡅࡈࡉࡏࡖࡐࡗࡣࡓࡇࡍࡆུࠩ")), env.get(bstack111_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡕࡘࡏࡋࡇࡆࡘࡤ࡙ࡌࡖࡉཱུࠪ")), env.get(bstack111_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧྲྀ"))),
            bstack111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨཷ"): env.get(bstack111_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤླྀ")),
            bstack111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧཹ"): env.get(bstack111_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒེࠣ"))
        }
    if env.get(bstack111_opy_ (u"ࠣࡃ࡝࡙ࡗࡋ࡟ࡉࡖࡗࡔࡤ࡛ࡓࡆࡔࡢࡅࡌࡋࡎࡕࠤཻ")) and env.get(bstack111_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇོࠦ")):
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥཽࠣ"): bstack111_opy_ (u"ࠦࡆࢀࡵࡳࡧࠣࡇࡎࠨཾ"),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣཿ"): bstack111_opy_ (u"ࠨࡻࡾࡽࢀ࠳ࡤࡨࡵࡪ࡮ࡧ࠳ࡷ࡫ࡳࡶ࡮ࡷࡷࡄࡨࡵࡪ࡮ࡧࡍࡩࡃࡻࡾࠤྀ").format(env.get(bstack111_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋཱྀࠪ")), env.get(bstack111_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙࠭ྂ")), env.get(bstack111_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠩྃ"))),
            bstack111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ྄ࠧ"): env.get(bstack111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦ྅")),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ྆"): env.get(bstack111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ྇"))
        }
    if any([env.get(bstack111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧྈ")), env.get(bstack111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡗࡋࡓࡐࡎ࡙ࡉࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢྉ")), env.get(bstack111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨྊ"))]):
        return {
            bstack111_opy_ (u"ࠥࡲࡦࡳࡥࠣྋ"): bstack111_opy_ (u"ࠦࡆ࡝ࡓࠡࡅࡲࡨࡪࡈࡵࡪ࡮ࡧࠦྌ"),
            bstack111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣྍ"): env.get(bstack111_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡓ࡙ࡇࡒࡉࡄࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧྎ")),
            bstack111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤྏ"): env.get(bstack111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨྐ")),
            bstack111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣྑ"): env.get(bstack111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣྒ"))
        }
    if env.get(bstack111_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤྒྷ")):
        return {
            bstack111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥྔ"): bstack111_opy_ (u"ࠨࡂࡢ࡯ࡥࡳࡴࠨྕ"),
            bstack111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥྖ"): env.get(bstack111_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡒࡦࡵࡸࡰࡹࡹࡕࡳ࡮ࠥྗ")),
            bstack111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ྘"): env.get(bstack111_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡷ࡭ࡵࡲࡵࡌࡲࡦࡓࡧ࡭ࡦࠤྙ")),
            bstack111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥྚ"): env.get(bstack111_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥྛ"))
        }
    if env.get(bstack111_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘࠢྜ")) or env.get(bstack111_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤྜྷ")):
        return {
            bstack111_opy_ (u"ࠣࡰࡤࡱࡪࠨྞ"): bstack111_opy_ (u"ࠤ࡚ࡩࡷࡩ࡫ࡦࡴࠥྟ"),
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨྠ"): env.get(bstack111_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣྡ")),
            bstack111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢྡྷ"): bstack111_opy_ (u"ࠨࡍࡢ࡫ࡱࠤࡕ࡯ࡰࡦ࡮࡬ࡲࡪࠨྣ") if env.get(bstack111_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤྤ")) else None,
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢྥ"): env.get(bstack111_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡋࡎ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢྦ"))
        }
    if any([env.get(bstack111_opy_ (u"ࠥࡋࡈࡖ࡟ࡑࡔࡒࡎࡊࡉࡔࠣྦྷ")), env.get(bstack111_opy_ (u"ࠦࡌࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧྨ")), env.get(bstack111_opy_ (u"ࠧࡍࡏࡐࡉࡏࡉࡤࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧྩ"))]):
        return {
            bstack111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦྪ"): bstack111_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡄ࡮ࡲࡹࡩࠨྫ"),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦྫྷ"): None,
            bstack111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦྭ"): env.get(bstack111_opy_ (u"ࠥࡔࡗࡕࡊࡆࡅࡗࡣࡎࡊࠢྮ")),
            bstack111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥྯ"): env.get(bstack111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢྰ"))
        }
    if env.get(bstack111_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࠤྱ")):
        return {
            bstack111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧྲ"): bstack111_opy_ (u"ࠣࡕ࡫࡭ࡵࡶࡡࡣ࡮ࡨࠦླ"),
            bstack111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧྴ"): env.get(bstack111_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤྵ")),
            bstack111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨྶ"): bstack111_opy_ (u"ࠧࡐ࡯ࡣࠢࠦࡿࢂࠨྷ").format(env.get(bstack111_opy_ (u"࠭ࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠩྸ"))) if env.get(bstack111_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠥྐྵ")) else None,
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢྺ"): env.get(bstack111_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦྻ"))
        }
    if bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠥࡒࡊ࡚ࡌࡊࡈ࡜ࠦྼ"))):
        return {
            bstack111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ྽"): bstack111_opy_ (u"ࠧࡔࡥࡵ࡮࡬ࡪࡾࠨ྾"),
            bstack111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ྿"): env.get(bstack111_opy_ (u"ࠢࡅࡇࡓࡐࡔ࡟࡟ࡖࡔࡏࠦ࿀")),
            bstack111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ࿁"): env.get(bstack111_opy_ (u"ࠤࡖࡍ࡙ࡋ࡟ࡏࡃࡐࡉࠧ࿂")),
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿃"): env.get(bstack111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ࿄"))
        }
    if bstack1l1lll1111_opy_(env.get(bstack111_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡇࡃࡕࡋࡒࡒࡘࠨ࿅"))):
        return {
            bstack111_opy_ (u"ࠨ࡮ࡢ࡯ࡨ࿆ࠦ"): bstack111_opy_ (u"ࠢࡈ࡫ࡷࡌࡺࡨࠠࡂࡥࡷ࡭ࡴࡴࡳࠣ࿇"),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ࿈"): bstack111_opy_ (u"ࠤࡾࢁ࠴ࢁࡽ࠰ࡣࡦࡸ࡮ࡵ࡮ࡴ࠱ࡵࡹࡳࡹ࠯ࡼࡿࠥ࿉").format(env.get(bstack111_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡗࡊࡘࡖࡆࡔࡢ࡙ࡗࡒࠧ࿊")), env.get(bstack111_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗࡋࡐࡐࡕࡌࡘࡔࡘ࡙ࠨ࿋")), env.get(bstack111_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠬ࿌"))),
            bstack111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ࿍"): env.get(bstack111_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡘࡑࡕࡏࡋࡒࡏࡘࠤ࿎")),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ࿏"): env.get(bstack111_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠤ࿐"))
        }
    if env.get(bstack111_opy_ (u"ࠥࡇࡎࠨ࿑")) == bstack111_opy_ (u"ࠦࡹࡸࡵࡦࠤ࿒") and env.get(bstack111_opy_ (u"ࠧ࡜ࡅࡓࡅࡈࡐࠧ࿓")) == bstack111_opy_ (u"ࠨ࠱ࠣ࿔"):
        return {
            bstack111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ࿕"): bstack111_opy_ (u"ࠣࡘࡨࡶࡨ࡫࡬ࠣ࿖"),
            bstack111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ࿗"): bstack111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࡿࢂࠨ࿘").format(env.get(bstack111_opy_ (u"࡛ࠫࡋࡒࡄࡇࡏࡣ࡚ࡘࡌࠨ࿙"))),
            bstack111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ࿚"): None,
            bstack111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿛"): None,
        }
    if env.get(bstack111_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥ࿜")):
        return {
            bstack111_opy_ (u"ࠣࡰࡤࡱࡪࠨ࿝"): bstack111_opy_ (u"ࠤࡗࡩࡦࡳࡣࡪࡶࡼࠦ࿞"),
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ࿟"): None,
            bstack111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ࿠"): env.get(bstack111_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊࠨ࿡")),
            bstack111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿢"): env.get(bstack111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ࿣"))
        }
    if any([env.get(bstack111_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࠦ࿤")), env.get(bstack111_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡒࡍࠤ࿥")), env.get(bstack111_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡔࡇࡕࡒࡆࡓࡅࠣ࿦")), env.get(bstack111_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡕࡇࡄࡑࠧ࿧"))]):
        return {
            bstack111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ࿨"): bstack111_opy_ (u"ࠨࡃࡰࡰࡦࡳࡺࡸࡳࡦࠤ࿩"),
            bstack111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ࿪"): None,
            bstack111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ࿫"): env.get(bstack111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ࿬")) or None,
            bstack111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿭"): env.get(bstack111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ࿮"), 0)
        }
    if env.get(bstack111_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ࿯")):
        return {
            bstack111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ࿰"): bstack111_opy_ (u"ࠢࡈࡱࡆࡈࠧ࿱"),
            bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ࿲"): None,
            bstack111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ࿳"): env.get(bstack111_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ࿴")),
            bstack111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ࿵"): env.get(bstack111_opy_ (u"ࠧࡍࡏࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡇࡔ࡛ࡎࡕࡇࡕࠦ࿶"))
        }
    if env.get(bstack111_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ࿷")):
        return {
            bstack111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ࿸"): bstack111_opy_ (u"ࠣࡅࡲࡨࡪࡌࡲࡦࡵ࡫ࠦ࿹"),
            bstack111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ࿺"): env.get(bstack111_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ࿻")),
            bstack111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ࿼"): env.get(bstack111_opy_ (u"ࠧࡉࡆࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣ࿽")),
            bstack111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿾"): env.get(bstack111_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧ࿿"))
        }
    return {bstack111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢက"): None}
def get_host_info():
    uname = os.uname()
    return {
        bstack111_opy_ (u"ࠤ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠦခ"): uname.nodename,
        bstack111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧဂ"): uname.sysname,
        bstack111_opy_ (u"ࠦࡹࡿࡰࡦࠤဃ"): uname.machine,
        bstack111_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨင"): uname.version,
        bstack111_opy_ (u"ࠨࡡࡳࡥ࡫ࠦစ"): uname.machine
    }
def bstack1l1ll11l1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1l1lll11ll_opy_():
    if bstack1l11ll11l_opy_.get_property(bstack111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨဆ")):
        return bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧဇ")
    return bstack111_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠨဈ")
def bstack1l1ll11l11_opy_(driver):
    info = {
        bstack111_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩဉ"): driver.capabilities,
        bstack111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨည"): driver.session_id,
        bstack111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ဋ"): driver.capabilities.get(bstack111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫဌ"), None),
        bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဍ"): driver.capabilities.get(bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩဎ"), None),
        bstack111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࠫဏ"): driver.capabilities.get(bstack111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩတ"), None),
    }
    if bstack1l1lll11ll_opy_() == bstack111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪထ"):
        info[bstack111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ဒ")] = bstack111_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬဓ") if bstack111lllll_opy_() else bstack111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩန")
    return info
def bstack111lllll_opy_():
    if bstack1l11ll11l_opy_.get_property(bstack111_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧပ")):
        return True
    if bstack1l1lll1111_opy_(os.environ.get(bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪဖ"), None)):
        return True
    return False
def bstack1l1l1111l_opy_(bstack1l1llll11l_opy_, url, data, config):
    headers = config.get(bstack111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫဗ"), None)
    proxies = bstack1lllll1ll_opy_(config, url)
    auth = config.get(bstack111_opy_ (u"ࠫࡦࡻࡴࡩࠩဘ"), None)
    response = requests.request(
            bstack1l1llll11l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1lll1ll1ll_opy_(bstack1llllll111_opy_, size):
    bstack1111l1111_opy_ = []
    while len(bstack1llllll111_opy_) > size:
        bstack1ll1lll1l_opy_ = bstack1llllll111_opy_[:size]
        bstack1111l1111_opy_.append(bstack1ll1lll1l_opy_)
        bstack1llllll111_opy_ = bstack1llllll111_opy_[size:]
    bstack1111l1111_opy_.append(bstack1llllll111_opy_)
    return bstack1111l1111_opy_
def bstack1l1lll1ll1_opy_(message, bstack1ll111l11l_opy_=False):
    os.write(1, bytes(message, bstack111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫမ")))
    os.write(1, bytes(bstack111_opy_ (u"࠭࡜࡯ࠩယ"), bstack111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ရ")))
    if bstack1ll111l11l_opy_:
        with open(bstack111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮ࡱ࠴࠵ࡾ࠳ࠧလ") + os.environ[bstack111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨဝ")] + bstack111_opy_ (u"ࠪ࠲ࡱࡵࡧࠨသ"), bstack111_opy_ (u"ࠫࡦ࠭ဟ")) as f:
            f.write(message + bstack111_opy_ (u"ࠬࡢ࡮ࠨဠ"))
def bstack1l1llll111_opy_():
    return os.environ[bstack111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩအ")].lower() == bstack111_opy_ (u"ࠧࡵࡴࡸࡩࠬဢ")
def bstack11l111ll1_opy_(bstack1ll111l1l1_opy_):
    return bstack111_opy_ (u"ࠨࡽࢀ࠳ࢀࢃࠧဣ").format(bstack1ll111ll11_opy_, bstack1ll111l1l1_opy_)
def bstack1lllll111_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack111_opy_ (u"ࠩ࡝ࠫဤ")
def bstack1l1ll1ll1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111_opy_ (u"ࠪ࡞ࠬဥ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111_opy_ (u"ࠫ࡟࠭ဦ")))).total_seconds() * 1000
def bstack1l1lllll1l_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack111_opy_ (u"ࠬࡠࠧဧ")
def bstack1l1llll1l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ဨ")
    else:
        return bstack111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧဩ")
def bstack1l1lll1111_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111_opy_ (u"ࠨࡶࡵࡹࡪ࠭ဪ")
def bstack1l1ll1l111_opy_(val):
    return val.__str__().lower() == bstack111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨါ")
def bstack1ll1111ll1_opy_(bstack1l1ll11ll1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1l1ll11ll1_opy_ as e:
                print(bstack111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥာ").format(func.__name__, bstack1l1ll11ll1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1l1lll111l_opy_(bstack1l1lll1lll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1l1lll1lll_opy_(cls, *args, **kwargs)
            except bstack1l1ll11ll1_opy_ as e:
                print(bstack111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦိ").format(bstack1l1lll1lll_opy_.__name__, bstack1l1ll11ll1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1l1lll111l_opy_
    else:
        return decorator
def bstack111ll11ll_opy_(bstack1ll11llll1_opy_):
    if bstack111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩီ") in bstack1ll11llll1_opy_ and bstack1l1ll1l111_opy_(bstack1ll11llll1_opy_[bstack111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪု")]):
        return False
    if bstack111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩူ") in bstack1ll11llll1_opy_ and bstack1l1ll1l111_opy_(bstack1ll11llll1_opy_[bstack111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪေ")]):
        return False
    return True
def bstack1l1lllll1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1lll1ll111_opy_(hub_url):
    if bstack11111ll11_opy_() <= version.parse(bstack111_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩဲ")):
        if hub_url != bstack111_opy_ (u"ࠪࠫဳ"):
            return bstack111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧဴ") + hub_url + bstack111_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤဵ")
        return bstack1l111ll1l_opy_
    if hub_url != bstack111_opy_ (u"࠭ࠧံ"):
        return bstack111_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ့") + hub_url + bstack111_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤး")
    return bstack1lll111ll_opy_
def bstack1l1lllll11_opy_():
    return isinstance(os.getenv(bstack111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨ္")), str)
def bstack1ll1llll11_opy_(url):
    return urlparse(url).hostname
def bstack1111ll1l_opy_(hostname):
    for bstack1111llll1_opy_ in bstack11llll1ll_opy_:
        regex = re.compile(bstack1111llll1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1l1lll1l1l_opy_(bstack1l1llllll1_opy_, file_name, logger):
    bstack111111111_opy_ = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠪࢂ်ࠬ")), bstack1l1llllll1_opy_)
    try:
        if not os.path.exists(bstack111111111_opy_):
            os.makedirs(bstack111111111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111_opy_ (u"ࠫࢃ࠭ျ")), bstack1l1llllll1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111_opy_ (u"ࠬࡽࠧြ")):
                pass
            with open(file_path, bstack111_opy_ (u"ࠨࡷࠬࠤွ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111l1l1ll_opy_.format(str(e)))
def bstack1ll1111lll_opy_(file_name, key, value, logger):
    file_path = bstack1l1lll1l1l_opy_(bstack111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧှ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11llll1l_opy_ = json.load(open(file_path, bstack111_opy_ (u"ࠨࡴࡥࠫဿ")))
        else:
            bstack11llll1l_opy_ = {}
        bstack11llll1l_opy_[key] = value
        with open(file_path, bstack111_opy_ (u"ࠤࡺ࠯ࠧ၀")) as outfile:
            json.dump(bstack11llll1l_opy_, outfile)
def bstack1llll1ll11_opy_(file_name, logger):
    file_path = bstack1l1lll1l1l_opy_(bstack111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ၁"), file_name, logger)
    bstack11llll1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111_opy_ (u"ࠫࡷ࠭၂")) as bstack1llll11l_opy_:
            bstack11llll1l_opy_ = json.load(bstack1llll11l_opy_)
    return bstack11llll1l_opy_
def bstack1lll111l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫࠺ࠡࠩ၃") + file_path + bstack111_opy_ (u"࠭ࠠࠨ၄") + str(e))
def bstack11111ll11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111_opy_ (u"ࠢ࠽ࡐࡒࡘࡘࡋࡔ࠿ࠤ၅")
def bstack1ll11l1l_opy_(config):
    if bstack111_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ၆") in config:
        del (config[bstack111_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ၇")])
        return False
    if bstack11111ll11_opy_() < version.parse(bstack111_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩ၈")):
        return False
    if bstack11111ll11_opy_() >= version.parse(bstack111_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪ၉")):
        return True
    if bstack111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ၊") in config and config[bstack111_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭။")] is False:
        return False
    else:
        return True
def bstack1lll1llll_opy_(args_list, bstack1l1lll1l11_opy_):
    index = -1
    for value in bstack1l1lll1l11_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll11111l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll11111l1_opy_ = bstack1ll11111l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ၌"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ၍"), exception=exception)
    def bstack1ll1111111_opy_(self):
        if self.result != bstack111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ၎"):
            return None
        if bstack111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨ၏") in self.exception_type:
            return bstack111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧၐ")
        return bstack111_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨၑ")
    def bstack1l1ll1lll1_opy_(self):
        if self.result != bstack111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ၒ"):
            return None
        if self.bstack1ll11111l1_opy_:
            return self.bstack1ll11111l1_opy_
        return bstack1l1ll1llll_opy_(self.exception)
def bstack1l1ll1llll_opy_(exc):
    return traceback.format_exception(exc)
def bstack1ll1111l1l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True