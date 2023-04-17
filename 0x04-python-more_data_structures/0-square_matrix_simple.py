#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix1 = matrix.copy()
    new_matrix2 = []
    for row in new_matrix1:
        fonction_sqrt = lambda x: x ** 2
        new_row = list(map(fonction_sqrt, row))
        new_matrix2.append(new_row)
    return new_matrix2
