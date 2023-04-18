#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    key = a_dictionary.keys()
    value = a_dictionary.values()
    mul = map((lambda x: x * 2), value)
    new_dic.update(zip(key, mul))
    return new_dic
