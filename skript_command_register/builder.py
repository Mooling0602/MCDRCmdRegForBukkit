import json

raw_str = '''
{
    "data": [{
        "name": "!!calc",
        "type": "LITERAL",
        "children": [{
            "name": "item",
            "type": "LITERAL",
            "children": [{
                "name": "box/count",
                "type": "TEXT",
                "children": [{
                    "name": "stack",
                    "type": "INTEGER",
                    "children": [{
                        "name": "single",
                        "type": "INTEGER",
                        "children": []
                    }]
                }]
            }]
        }, {
            "name": "color",
            "type": "LITERAL",
            "children": [{
                "name": "red/#HEX",
                "type": "TEXT",
                "children": [{
                    "name": "green",
                    "type": "INTEGER",
                    "children": [{
                        "name": "blue",
                        "type": "INTEGER",
                        "children": []
                    }]
                }]
            }]
        }, {
            "name": "expression",
            "type": "GREEDY_TEXT",
            "children": []
        }]
    }, {
        "name": "!!kill",
        "type": "LITERAL",
        "children": []
    }]
}
'''

json_data = json.loads(raw_str)

with open('example_raw_data.json', 'r') as f:
    json_file = json.load(f)

def build_command(json_data, level=1):
    # 确保输入是列表
    if not isinstance(json_data, list):
        raise ValueError(f"Invalid input: Expected a list, got {type(json_data).__name__} at level {level}")

    command_data = {}

    for command in json_data:
        # 确保每个元素是字典
        if not isinstance(command, dict):
            raise ValueError(f"Invalid element: Expected a dict, got {type(command).__name__} at level {level}")

        cmd_name = command['name']

        # 仅处理 LITERAL 类型的节点
        if command['type'] == "LITERAL":
            command_data[cmd_name] = {}

            # 如果有子节点，递归处理
            if 'children' in command and command['children']:
                command_data[cmd_name] = build_command(command['children'], level + 1)
    
    return command_data


with open("output.json", "w", encoding="utf-8") as f:
    json.dump(build_command(json_data["data"]), f, indent=4, ensure_ascii=False)
