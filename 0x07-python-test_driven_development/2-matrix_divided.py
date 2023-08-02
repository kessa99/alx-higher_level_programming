#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    function for matrix divided
    """
    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(element, (int, float)) for element in
                   [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row))for row in matrix])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
