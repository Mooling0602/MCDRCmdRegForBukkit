import os

from .utils import *
from .installer import extract_file, load_general_sk_script
from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, prev_module):
    server.logger.info(tr("on_load"))
    if not os.path.exists("{serverDir}/plugins/Skript/scripts/MCDR_Commands_general.sk"):
        extract_file()
    load_general_sk_script()

def on_server_startup(server: PluginServerInterface):
    load_general_sk_script(True)
