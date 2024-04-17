#!/usr/bin/python3

"""Defines class BaseGeometry."""


class BaseGeometry():
    """this is an empty class BaseGeometry"""

    def area(self):
        """raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
