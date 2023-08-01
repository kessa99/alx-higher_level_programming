#!/usr/bin/python3
"""print add of a and b"""


def add_integer(a, b=98):
    """function to add"""
    if a is None or not isinstance(a, (int, float)):
        raise ValueError("a must be a integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be a integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
