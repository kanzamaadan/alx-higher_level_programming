#!/usr/bin/python3
""" Module that contains class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square  inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
