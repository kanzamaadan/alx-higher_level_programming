#!/usr/bin/python3
""" Module that contains class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the y """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """prints Rectangle instance with the character #"""
        rec = self.y * "\n"
        for i in range(self.height):
            rec += " " * self.x
            rec += ("#" * self.width) + "\n"
        print(rec, end='')

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ this returns a dictionary representation of rectangles"""
        rec = ['id', 'width', 'height', 'x', 'y']
        dic = {}
        for k in rec:
            dic[k] = getattr(self, k)
        return dic
