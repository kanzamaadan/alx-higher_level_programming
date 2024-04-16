#!/usr/bin/python3
"""class prevents the user from dynamically creating
    new instance attributes
"""

class LockedClass():
    """class dynamically creating new instance attributes"""
    __slots__ = ['first_name'] 

    def __init__(self):
        """initialize method"""
        pass
