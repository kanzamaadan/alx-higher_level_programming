#!/usr/bin/python3

"""class Student that defines a studen"""


class Student():
    """class Student that defines a studen"""
    def __init__(self, first_name, last_name, age):
        """initializes a Student.
        Args:
            first_name: string for the first name of student
            last_name: string for the last name of student
            age: int for the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
