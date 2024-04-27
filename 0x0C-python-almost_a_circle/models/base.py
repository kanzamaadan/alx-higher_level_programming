#!/usr/bin/python3
""" Module that contains class Base """
import json
import os.path
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as f:
            data = f.read()

        dic_list = cls.from_json_string(data)
        instances = []

        for i in range(len(dic_list)):
            instance = cls.create(**dic_list[i])
            instances.append(instance)

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            list_dict = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dict = [0, 0, 0, 0]
            list_keys = ['id', 'size', 'x', 'y']

        obj_attr = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for k in range(len(list_keys)):
                    list_dict[k] = obj.to_dictionary()[list_keys[k]]
                obj_attr.append(list_dict[:])

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(obj_attr)

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        obj_attr = []

        for csv_elem in csv_list:
            csv_dic = {}
            for k in enumerate(csv_elem):
                csv_dic[list_keys[k[0]]] = int(k[1])
            obj_attr.append(csv_dic)

        list_ins = []

        for i in range(len(obj_attr)):
            list_ins.append(cls.create(**obj_attr[i]))

        return list_ins
