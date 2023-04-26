#!/usr/bin/python3
"""Print a square"""


class Square:
    """Print a squre like c"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
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
            raise ValueError("size must ne >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end="")
            print()
