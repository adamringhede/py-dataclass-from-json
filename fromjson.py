import argparse
import json
import sys
from typing import Dict, List, Optional


def _infer_type(o) -> Optional[str]:
    if o is None:
        return "Optional[Any]"
    if isinstance(o, str):
        return 'str'
    if isinstance(o, bool):
        return 'bool'
    if isinstance(o, int):
        return 'int'
    if isinstance(o, float):
        return 'float'
    if isinstance(o, dict) and not o:
        return 'Dict'
    return None


def _create_class_name(key: str) -> str:
    return key.title().replace('_', '')


def _generate_from_dict(obj: Dict, name="Root", indent="    ") -> List[str]:
    out = [
        "@dataclass",
        f"class {name}():",
    ]
    for key, value in obj.items():
        # if it is a list, generate a new class with a name
        type = _infer_type(value)
        if type is None:
            if isinstance(value, list):
                if len(value) == 0:
                    type = "List[Any]"
                elif isinstance(value[0], dict):
                    inner_class_name = _create_class_name(key).rstrip('s')
                    out = _generate_from_dict(value[0], name=inner_class_name, indent=indent) + out
                    type = f"List[{inner_class_name}]"
                else:
                    type = f"List[{_infer_type(value[0])}]"
            elif isinstance(value, dict):
                inner_class_name = _create_class_name(key)
                out = _generate_from_dict(value, name=inner_class_name, indent=indent) + out
                type = inner_class_name

        out.append(indent + f"{key}: {type}")
    out.append("\n")
    return out


def generate(input: str, name="Root"):
    obj = json.loads(input)
    if isinstance(obj, dict):
        return "\n".join(_generate_from_dict(obj, name=name))
    return ''


def _run():
    parser = argparse.ArgumentParser()

    parser.add_argument('infile',
                        default=sys.stdin,
                        type=argparse.FileType('r'),
                        nargs='?')
    parser.add_argument('name', default='Root')

    args = parser.parse_args()
    data = args.infile.read()

    print(generate(data, name=args.name))

if __name__ == '__main__':
   _run()
