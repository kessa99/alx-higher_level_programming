#!/usr/bin/python3
"""
    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def read_file(my_file_0=""):
    """
    Read a file
    """
    with open('my_file_0.txt', 'r', encoding="utf-8") as files:
        show = files.read()
        print(show)
