#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """Class to represent a square"""

    def __init__(self, size=0):
        """Initialize square with a specific size."""
        self.__size = size

    def dict_(self):
        """Return dictionary representation of the Square instance."""
        return {'size': self.__size}
