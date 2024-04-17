#!/usr/bin/python3

"""defines function writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a
    text file, using a JSON representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
