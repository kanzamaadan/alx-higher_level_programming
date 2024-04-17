#!/usr/bin/python3
"""defines function that reads a text"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        file_cntnt = f.read()

    print(file_cntnt, end="")
