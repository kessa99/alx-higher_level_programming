#!/usr/bin/python3
"""
    Prototype: def class_to_json(obj):
    obj is an instance of a Class
    All attributes of the obj Class are serializable:
    list, dictionary, string, integer and boolean
    You are not allowed to import any module
"""


def class_to_json(obj):
    """
        creat a empty dictionnary to save the description
        Obtain the value of attribute
        Check value type and move on the empty dict
    """
    json_dict = {}

    for attr in obj.__dict__:
        value = getattr(obj, attr)

        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
