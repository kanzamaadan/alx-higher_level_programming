#!/usr/bin/python3

"""get the class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes a new Rectangle and checks the width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """this is the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """this is the string representation of the rectangle"""
        r = "[" + str(self.__class__.__name__) + "] "
        r += str(self.__width) + "/" + str(self.__height)
        return r
