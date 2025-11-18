import re
import string
from argparse import ArgumentParser, Namespace
from enum import auto, Enum
from pathlib import Path


class Mode(Enum):
    ENCRYPT = auto()
    DECRYPT = auto()


def read_file(file: Path) -> str:
    with open(file, "r") as input_:
        line: str = input_.readline().lower()
        line = re.sub("[^a-z]", "", line)
    
    return line


def parse_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("--out", type=Path, action="store", dest="output")
    parser.add_argument("file", type=Path, action="store", metavar="FILE")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", action="store", type=str, metavar="KEY")
    group.add_argument("--decrypt", action="store", type=str, metavar="KEY")
    
    args: Namespace = parser.parse_args()
    return args


def to_index(char: str) -> int:
    return ord(char) - ord('a')


def from_index(char: int) -> str:
    return chr(ord('a') + char)


def main() -> None:
    args: Namespace = parse_args()
    
    text: str = read_file(args.file)
    
    mode: Mode = Mode.ENCRYPT if args.encrypt else Mode.DECRYPT
    key: str = args.encrypt if mode == Mode.ENCRYPT else args.decrypt
    
    def apply(index: int) -> str:
        match mode:
            case Mode.ENCRYPT:
                return from_index((to_index(text[index]) + to_index(key[index % len(key)])) % 26)
            case Mode.DECRYPT:
                return from_index((to_index(text[index]) - to_index(key[index % len(key)])) % 26)
    
    output: str = "".join([apply(index) for index in range(len(text))])
    
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write(output)
    else:
        print(output)


if __name__ == '__main__':
    main()
