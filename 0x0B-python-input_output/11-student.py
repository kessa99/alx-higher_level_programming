#!/usr/bin/python3
"""
"""
class Student:
    """
    """


    def __init__(self, first_name, last_name, age):
        """
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
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
        """
        for key, value in json.items():
            setattr(self, key, value)
