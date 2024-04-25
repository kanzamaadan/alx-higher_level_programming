#!/usr/bin/python3
""" Module that contains class Base """
import json


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'a') as f:
            data = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(data)
            f.write(json_string)
