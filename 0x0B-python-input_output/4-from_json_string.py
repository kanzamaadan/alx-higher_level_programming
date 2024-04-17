#!/usr/bin/python3

"""defines function returns the Python data structure"""
import json


def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented by a JSON string"""
    py_str = json.loads(my_str)
    return py_str
