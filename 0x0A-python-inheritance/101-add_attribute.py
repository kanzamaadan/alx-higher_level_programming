#!/usr/bin/python3

"""defines function that adds a new attribute."""


def add_attribute(obj, attr, value):
    """function that adds a new attribute to an object if it's possible
    Raise a TypeError exception, with the message can't
    add new attribute if the object can't have new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
