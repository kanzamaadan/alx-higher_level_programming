#!/usr/bin/python3

"""Defines function that returns True or False."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj an instance of the specified class
    if not, it returns False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
