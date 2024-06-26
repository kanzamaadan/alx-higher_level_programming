#!/usr/bin/python3
"""defines a rectangle with a specified width and height"""


class Rectangle:
    """ class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a new Rectangle
        Args:
            @width (int): the width of the rectangle
            @height (int): the height of the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
