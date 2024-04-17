#!/usr/bin/python3

"""get the class Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """initialize the size square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
