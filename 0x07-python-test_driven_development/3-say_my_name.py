#!/usr/bin/python3
"""Module containing a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

    Arguments:
        @first_name: a string that represents the first name
        @last_name: a string that represents the secand name
    Raises:
        TypeError: if 1st or 2nd name is not a string"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
