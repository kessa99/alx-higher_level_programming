#!/usr/bin/python3
"""
    Write a class Student that defines a
    student by: (based on 10-student.py)
"""
class Student:
    """
        Public instance attributes:
        first_name
        last_name
        age
    """


    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Public method def to_json(self, attrs=None):
            that retrieves a dictionary representation of
            a Student instance (same as 8-class_to_json.py):
            If attrs is a list of strings,
            only attributes name contain in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """

        if attrs is None:
            attrs = self.__dict__.keys()

        value = None
        json_dict = {}

        for attr in attrs:
            if attr in self.__dict__:
                value = getattr(self. attr)

                if isinstance(value, (list, str, int, dict, bool)):
                    json_dict[attr] = value
        return json_dict

    def reload_from_json(self, json):
        """
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        """
        for key, value in json.items():
            setattr(self, key, value)
