#!/usr/bin/python3
"""
    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions 
    if the JSON string doesn’t represent an object.
"""
import json



def from_json_string(my_str):
    """
    return an object representaion by a JSON
    """
    return json.loads(my_str)
