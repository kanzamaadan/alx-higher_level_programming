#!/usr/bin/python3

"""defines class MyInt that inherits from int."""


class MyInt(int):
    """this class MyInt"""
    def __init__(self, value):
        """method to initialize the MyInt object"""
        self.value = value

    def __eq__(self, other):
        """ methods to invert the behavior of the =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """ methods to invert the behavior of the !="""
        return not self.__eq__(other)
