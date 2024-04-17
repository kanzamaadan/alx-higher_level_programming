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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
