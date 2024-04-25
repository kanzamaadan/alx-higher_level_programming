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
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is None:
            list_objs = []
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dict)
        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        list = json.loads(json_string)
        return list
