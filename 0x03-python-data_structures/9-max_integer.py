#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_value = my_list[0]
        for idx in range(1, len(my_list)):
            if my_list[idx] > max_value:
                max_value = my_list[idx]
        return max_value
