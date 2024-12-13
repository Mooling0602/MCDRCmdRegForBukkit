import os

from .utils import *
from .installer import extract_file, load_general_sk_script
from .builder import *
from mcdreforged.api.all import *
from minecraft_command_register import register # type: ignore

def on_load(server: PluginServerInterface, prev_module):
    server.logger.info(tr("on_load"))
    if not os.path.exists(f"{serverDir}/plugins/Skript/scripts/MCDR_Commands_general.sk"):
        extract_file()
    load_general_sk_script()
    sk_script_builder()


def on_server_startup(server: PluginServerInterface):
    load_general_sk_script(True)
    sk_script_builder()

@new_thread(plgSelf.id)   
def sk_script_builder():
    if psi.is_server_startup():
        json_data = register(psi)
        command_data = format_raw_data(json_data["data"])
        output_path = f"{serverDir}/plugins/Skript/scripts/MCDR_Commands_auto.sk"
        with open(output_path, "w", encoding="utf-8") as output_file:
            build_sk_script(command_data, output_file)
        load_auto_sk_script()
    
def load_auto_sk_script():
    psi.execute("sk reload MCDR_Commands_auto.sk")
    psi.logger.info(tr("mcdr_builtin_cmd"))
    psi.logger.info(tr("on_sk_reload"))
    psi.logger.info(tr("arg_wrong"))