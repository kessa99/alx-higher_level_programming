#!/usr/bin/python3
"""
    Prototype: def to_json_string(my_obj)
    You don’t need to manage exceptions
    if the object can’t be serialized.
"""
import json


def to_json_string(my_dict):
    """
    returns json representation
    """
    return json.dumps(my_dict)
