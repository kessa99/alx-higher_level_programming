#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copie = my_list.copy()
    if idx < 0 or idx >= len(my_copie):
        return my_copie
    else:
        my_copie[idx] = element
        return my_copie
