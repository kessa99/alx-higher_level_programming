#!/usr/bin/python3
"""
    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, it should be created
    You must use the with statement
    You don’t need to manage file permission
    or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def append_write(filename="", text=""):
    """
    APPEND in file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
