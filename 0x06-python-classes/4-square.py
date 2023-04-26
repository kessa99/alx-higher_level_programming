#!/usr/bin/python3
"""Access and udapte private attribute"""


class Square:
    """Calcul and modification"""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not size:
            self.__size = 0
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
    """calcul"""
    def area(self):
        return self.__size * self.__size
