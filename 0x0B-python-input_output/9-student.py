#!/usr/bin/python3
"""
    Public instance attributes:
    first_name
    last_name
    age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves
    a dictionary representation of a Student instance
    (same as 8-class_to_json.py)
    You are not allowed to import any module
"""


class Student:
    """
    initialization
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"
        description of dict
        """
        json_dict = {}

        for attr in self.__dict__:
            value = getattr(self, attr)

            if isinstance(value, (dict, str, bool, int, list)):
                json_dict[attr] = value

        return json_dict
