#!/usr/bin/env python3
from marvel_chars import marvelchars


def get_user_input():
    chars = list(marvelchars.keys())
    stats = list(marvelchars[chars[0]].keys())

    char_name = input(f"Which character do you want to know about? ({', '.join(map(str,chars))}) ")
    char_stat = input(f"What statistic do you want to know about? ({', '.join(map(str,stats))}) ")

    return {"char_name": char_name, "char_stat": char_stat}

def list_chars():
    user_input = get_user_input()
    char_name = user_input['char_name'].title()
    char_stat = user_input['char_stat'].lower()

    if char_name in marvelchars:
        if char_stat in marvelchars[char_name]:
            return f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}."
        else:
            return f"{char_name} has no {char_stat} attribute."
    else:
        return f"{char_name} character not found."

print(list_chars())