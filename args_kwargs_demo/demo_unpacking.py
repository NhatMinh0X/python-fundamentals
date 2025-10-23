#!/usr/bin/env python3
# demo_unpacking.py
def add(x, y, z):
    return x + y + z

def greet(name, lang="en"):
    if lang == "en":
        return f"Hello, {name}"
    return f"Hi, {name} (lang={lang})"

if __name__ == "__main__":
    nums = [1, 2, 3]
    print("add(*nums) =", add(*nums))           # unpack list -> positional args

    info = {"name": "Alice", "lang": "vi"}
    print("greet(**info) =", greet(**info))     # unpack dict -> keyword args