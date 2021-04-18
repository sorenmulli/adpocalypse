from __future__ import annotations
import os
import json


def get_names(path: str = "data") -> dict[str, list[str]]:
    """
    Reads the character data base characters.json.
    """
    with open(os.path.join(path, "characters.json"), "r") as f:
        characters = json.load(f)
    return characters

def find_names(doc: str, name_db: dict[str, list[str]]) -> list[str]:
    """
    Returns a list of all characters that were present in the document.
    Characters are returned as full names and not as they were found.
    """
    out = list()
    for w in doc.lower().split():
        for name, keys in name_db.items():
            if any(k.lower() == w for k in keys):
                out.append(name)
                break
    return out

if __name__ == '__main__':
    name_db = get_names()
    example =\
    """
I’m just curious to see which characters you think really, truly deserve a happy ending, not who you want to have a happy ending or who you think should have one because they’re your favorite character.
For me, it’s Jeyne Poole and Arya Stark. Jeyne is an innocent girl who’s been horrifically abused by Ramsay. She’s an example of the terrible effects war can have on ordinary people. Arya has navigated her way through dangerous, harrowing situations. She’s resilient, brave, and an eleven year old girl who still, deep down, longs for home. Call me naive, but they’ve both been through so much and I really want George to just give them a peaceful ending:)
    """
    print(
        find_names(example, name_db),
    )
