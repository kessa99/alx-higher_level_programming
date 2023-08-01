#!/usr/bin/python3
"""print add of a and b"""


def add_integer(a, b=98):
    """function to add"""

    if a is None or (type(a) != int and type(a) != float):
        raise ValueError("a must be a integer")
    if isinstance(b, str):
        try:
            b = float(b)
        except ValueError:
            raise ValueError("b must be a integer")
    if type(b) != int and type(b) != float:
        raise ValueError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
