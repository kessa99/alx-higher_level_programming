#!/usr/bin/python3
"""
Prototype: def text_indentation(text):
text must be a string, otherwise raise
a TypeError exception with the message text must be a string
There should be no space at the beginning
or at the end of each printed line
You are not allowed to import any module
"""

def text_indentation(text):
    """
    funtion that print a text with 2 new
    linw afeter each of these character
    .,?,:
    """
    text = list(text)
    for arg in text:
        if arg == "." or arg =="?" or arg == ":":
            print()
            print()
