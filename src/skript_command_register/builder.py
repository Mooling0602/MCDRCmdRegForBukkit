def format_raw_data(json_data, level=1):
    if not isinstance(json_data, list):
        raise ValueError(f"Invalid input: Expected a list, got {type(json_data).__name__} at level {level}")

    command_data = {}

    for command in json_data:
        if not isinstance(command, dict):
            raise ValueError(f"Invalid element: Expected a dict, got {type(command).__name__} at level {level}")

        cmd_name = command['name']

        if command['type'] == "LITERAL":
            command_data[cmd_name] = {}

            if 'children' in command and command['children']:
                command_data[cmd_name] = format_raw_data(command['children'], level + 1)
    
    return command_data

def build_sk_script(dict_data, output_file, level=0, parent=None):
    global root_commands
    same_level_keys = []
    register_commands = None
    tab_complete = None
    for key, value in dict_data.items():
        if key != "!!MCDR":
            if level > 0:
                same_level_keys.append(f"{key}")
            else:
                register_commands = f'''command /{key}:
    trigger:
        send "<%player%> %full command%" to the console

'''
                output_file.write(register_commands)
            if same_level_keys:
                if parent != "!!MCDR":
                    command_intervals = '"' + '" and "'.join(same_level_keys) + '"'
                    tab_complete = f'''
on tab complete:
    event-string is "/{parent}"
    set tab completions for position {level} to {command_intervals}

'''

    if tab_complete is not None:
        output_file.write(tab_complete)  

    for key, value in dict_data.items():
        if isinstance(value, dict):
            if parent != "!!MCDR" or parent is None:
                if level == 0:
                    build_sk_script(value, output_file, level=level + 1, parent=key)
                else:
                    build_sk_script(value, output_file, level=level + 1, parent=parent)