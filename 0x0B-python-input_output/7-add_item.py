#!/usr/bin/python3
"""
    Write a script that adds all arguments
    to a Python list, and then save them to a file:

    You must use your function save_to_json_file
    from 5-save_to_json_file.py
    You must use your function load_from_json_file
    from 6-load_from_json_file.py
    The list must be saved as a JSON
    representation in a file named add_item.json
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.
"""
import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    list_of_json = load_from_json_file("add_item.json")
else:
    list_of_json = []

for arg in sys.argv[1:]:
    list_of_json.append(arg)

save_to_json_file(list_of_json, 'add_item.json')
