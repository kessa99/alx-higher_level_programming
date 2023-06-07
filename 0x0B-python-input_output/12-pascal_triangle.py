#!/usr/bin/python3
"""
Technical interview preparation
"""


def pascal_triangle(n):
    """
    Triangle de pascal(French word)
    """

    triangle = []

    if n <= 0 or not isinstance(n, int):
        return triangle

    for ligne in range(n):
        new_ligne = [1 if colonne == 0 or colonne == ligne else triangle[ligne - 1][colonne - 1] + triangle[ligne - 1][colonne] for colonne in range(ligne + 1)]
        triangle.append(new_ligne)
    return triangle
