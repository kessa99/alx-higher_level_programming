#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for value, keys in a_dictionary.items():
        print("{}: {}".format(value, keys))
