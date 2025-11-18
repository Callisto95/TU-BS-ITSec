import re
from argparse import ArgumentParser, Namespace
from enum import auto, Enum
from pathlib import Path


class InvalidKey(Exception):
    pass


class Mode(Enum):
    ENCRYPT = auto()
    DECRYPT = auto()


def main():
    args: Namespace = parse_args()
    
    mode: Mode = Mode.ENCRYPT if args.encrypt else Mode.DECRYPT
    key: str = args.encrypt if mode == Mode.ENCRYPT else args.decrypt
    
    exchange_map: dict[str, str] = create_exchange_map(key, mode)
    
    with open(args.file, "r") as input_:
        line: str = input_.readline().lower()
        line = re.sub("[^a-z]", "", line)
    
    # print(line)
    
    output: str = ""
    for char in line:
        output += exchange_map[char]
    
    print(output)


def parse_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("--out", type=Path, action="store", dest="output")
    parser.add_argument("file", type=Path, action="store", metavar="FILE")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", action="store", type=str, metavar="KEY")
    group.add_argument("--decrypt", action="store", type=str, metavar="KEY")
    
    args: Namespace = parser.parse_args()
    return args


def create_exchange_map(key: str, mode: Mode) -> dict[str, str]:
    if len(key) != 26:
        raise InvalidKey("length must be 26")
    
    exchange_map: dict[str, str] = { }
    
    used_letters: str = ""
    
    for index, char in enumerate(key):
        if char in used_letters:
            raise InvalidKey("letter has already been used")
        used_letters += char
        
        if mode == Mode.DECRYPT:
            exchange_map[char] = chr(ord('a') + index)
        else:
            exchange_map[chr(ord('a') + index)] = char
    
    return exchange_map


if __name__ == '__main__':
    main()
