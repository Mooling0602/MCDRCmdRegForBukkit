import os

from typing import Optional
from .utils import *

def extract_file():
    if os.path.exists(f"{serverDir}/plugins/Skript/scripts/"):
        with psi.open_bundled_file('resources/MCDR_Commands_general.sk') as file_handler:
            with open(f"{serverDir}/plugins/Skript/scripts/MCDR_Commands_general.sk", 'wb') as target_file:
                target_file.write(file_handler.read())

def load_general_sk_script(skip_check: Optional[bool] = False):
    if psi.is_server_startup() or skip_check:
        if os.path.exists(f"{serverDir}/plugins/Skript/config.sk"):
            psi.execute(f"sk reload MCDR_Commands_general.sk")
            psi.logger.info(tr("on_installed"))