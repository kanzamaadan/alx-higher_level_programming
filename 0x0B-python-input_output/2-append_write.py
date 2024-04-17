#!/usr/bin/python3
"""defines function that writes a string to a text file"""


def append_write(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
