#!/usr/bin/env python3

import unicodedata
import sys

from rich import print

NUMBER_OUT_OF_THE_BLUE = 1000000

def get_chars_with_names() -> dict:
    """ Retuns dictionary with the characters having names
    { 
        char_id:{
            'name': character_name,
            'symbol': chr(char_id)
        }
    }
    """
    chars_with_names = {}

    for c in range(NUMBER_OUT_OF_THE_BLUE):
        try:
            charcter = chr(c)
            charcter_name = unicodedata.name(charcter)
            chars_with_names[c] = {
                'name': charcter_name,
                'symbol': charcter
            }
        except:
            # This means that the character doesn't have a name
            pass
    
    return chars_with_names


def find_chars_by_name(chars_with_names: dict, lookup_name: str) -> dict:
    found_characters = {}
    for char_id, info in chars_with_names.items():
        # all character names must consist only of uppercase Latin letters (A–Z), digits (0–9), hyphens, and spaces.
        if info.get('name','').find(lookup_name.upper()) > -1:
            found_characters[char_id] = info.copy()

    return found_characters


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(find_chars_by_name(get_chars_with_names(), ' '.join(sys.argv[1:])))
    else:
        print("\n[yellow]Give me something to look up :)[/]\n")
