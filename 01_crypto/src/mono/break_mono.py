import random
import re
import string
from itertools import permutations
from random import choice, shuffle

from mono import apply_exchange_map, create_exchange_map, Mode, read_encrypted_file
from argparse import ArgumentParser, Namespace
from pathlib import Path


def parse_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("file", metavar="FILE", type=Path)
    return parser.parse_args()


def compute_mapping(word: str, mapping: dict[str, str] = None) -> tuple[str, dict[str, str]]:
    if not mapping:
        mapping = {}
    
    next_character: int = ord('a')
    while next_character in mapping:
        next_character += 1
    
    output: str = ""
    for character in word:
        if character in mapping:
            output += mapping[character]
        else:
            mapping[character] = chr(next_character)
            next_character += 1
            
            while next_character in mapping:
                next_character += 1
                if next_character > ord('z'):
                    raise Exception("unknown character") # NOSONAR
    
    return output, mapping


def default_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for char in string.ascii_lowercase:
        mapping[char] = char
    return mapping


def main() -> None:
    # args: Namespace = parse_args()
    # encrypted_line: str = read_encrypted_file(args.file)
    # 
    # words, word_lengths = load_common_words()
    # 
    # minimum_length: int = min(list(word_lengths.keys()))
    # maximum_length: int = max(list(word_lengths.keys()))
    
    # just brute force the solution
    # THIS DOESN'T WORK because the word list is missing works
    # there is no differentiation between random letters and missing words
    # for guessed_key in permutations(string.ascii_lowercase):
    #     print("".join(guessed_key))

    """
    # word list is lacking words
    # 'Chapter' - the first word - is missing
    for length in range(minimum_length, maximum_length + 1):
        for word in word_lengths[length]:
            mapping: dict[str, str] = default_mapping()
            for encrypted_char in encrypted_line[0:length]:
                for char in word:
                    # assume this is the correct decryption
                    mapping[encrypted_char] = char
                    mapping[char] = encrypted_char
    """
                
    
    """
    used_key: str | None = None
    
    def brute_force_key(map_: dict[str, str], offset: int = 0) -> bool:
        if len(encrypted_line) < offset:
            return True
        
        for length in range(minimum_length, maximum_length + 1):
            if apply_exchange_map(encrypted_line[offset:length], map_) in word_lengths[length]:
                if brute_force_key(map_, offset + length):
                    return True
        
        return False
    
    key: str = string.ascii_lowercase
    while not brute_force_key(create_exchange_map(key, Mode.DECRYPT)):
        letters: list[str] = list(string.ascii_lowercase)
        shuffle(letters)
        key = "".join(letters)
        print(f"\rattempting {key}...", end="")
        
        if key == "EDMHOSUPLGJCQFVAYNZRKBXWIT".lower():
            print("\nYOU HAVE FOUND IT\n")
    
    print()
    print(key)
    """


def load_common_words() -> tuple[list[str], dict[int, list[str]]]:
    with open("common.txt", "r") as common_words_input:
        common_words: list[str] = [word.strip() for word in common_words_input.readlines()]
    
    length_lookup: dict[int, list[str]] = { }
    for word in common_words:
        length_lookup.setdefault(len(word), []).append(word)
    
    return common_words, length_lookup


if __name__ == '__main__':
    main()
