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

    def area(self):
        """ returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectan = []
        for i in range(self.__height):
            [rectan.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """return a string representation of the rectangle"""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return rectan

    def __del__(self):
        """Print the message when instance of Rectangle is deleted"""
        print("Bye rectangle...")
