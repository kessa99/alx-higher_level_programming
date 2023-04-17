#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        fonction_sqrt = lambda x: x ** 2
        new_row = list(map(fonction_sqrt, row))
        new_matrix.append(new_row)
    return new_matrix
