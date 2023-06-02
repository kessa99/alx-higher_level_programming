#!/usr/bin/python3
"""
"""
def write_file(my_first_file="", text=""):
    with open('my_first_file', 'w', encoding="utf-8") as f:
        return f.write(text)

