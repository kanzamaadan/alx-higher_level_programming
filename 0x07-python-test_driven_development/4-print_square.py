#!/usr/bin/python3
"""module containing function that prints a square"""


def print_square(size):
    """function that prints a square with the character #

    Arguments:
        @size (integer):  is the size length of the square
    Raises:
        TypeError: if the size is not an integer
        TypeError: if size is less than 0
        TypeError: if size is a float and less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
