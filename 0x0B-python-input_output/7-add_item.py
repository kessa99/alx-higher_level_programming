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
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file
import json

my_list = []
for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, 'add_item.json')
load_from_json_file('add_item.json')
