#!/usr/bin/python3

"""
    print add of a and b
    >>> add_integer(5, 6)
    11
    >>> add_integer(100)
    198
    >>> add_integer(4, "School")
    b must be an integer
    >>> add_integer(None)
    a must be an integer
"""


def add_integer(a, b=98):
    if a is None and not isinstance(a, (int, float)):
        raise ValueError("a must be a integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be a integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
