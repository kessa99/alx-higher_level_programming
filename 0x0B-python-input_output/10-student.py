#!/usr/bin/python3
"""
    Public instance attributes:
    first_name
    last_name
    age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None):
    that retrieves a dictionary representation of a
    Student instance (same as 8-class_to_json.py):
    If attrs is a list of strings, only attribute names
    contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved
    You are not allowed to import any module
"""


class Student:
    """
        description of dict
    """
    def __init__(self, first_name, last_name, age):
        """
            initialiazation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            function for the description
        """

        if attrs is None:
            attrs = self.__dict__.keys()

        json_dict = {}
        value = None
        for attr in attrs:
            if attr in self.__dict__:
                value = getattr(self, attr)

                if isinstance(value, (list, str, int, dict, bool)):
                    json_dict[attr] = value
            else:
                json_dict[attr] = None
        return json_dict
