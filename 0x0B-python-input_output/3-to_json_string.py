#!/usr/bin/python3

"""defines function returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)"""
    json_obj = json.dumps(my_obj)
    return json_obj
