from typing import Optional
from mcdreforged.api.all import *

psi = ServerInterface.psi()
MCDRConfig = psi.get_mcdr_config()
plgSelf = psi.get_self_metadata()
serverDir = MCDRConfig["working_directory"]

def tr(tr_key: str, return_str: Optional[bool] = True):
    if tr_key.startswith(f"{plgSelf.id}"):
        translation = psi.rtr(f"{tr_key}")
    else:
        # 使用此前缀代表非本插件的翻译键，则翻译时不会附加本插件的ID，避免错误。
        if tr_key.startswith("#"):
            translation = psi.rtr(tr_key.replace("#", ""))
        else:
            translation = psi.rtr(f"{plgSelf.id}.{tr_key}")
    if return_str:
        tr_to_str: str = str(translation)
        return tr_to_str
    else:
        return translation