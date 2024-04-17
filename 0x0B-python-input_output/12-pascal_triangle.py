#!/usr/bin/python3

"""defines function that returns the Pascal's triangle"""


def pascal_triangle(n):
    """function that returns a list of lists
    of integers representing the Pascal's triangle of n
    Args:
        @n: the number of lists
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
