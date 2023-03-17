#!/usr/bin/python3
def no_c(my_string):
    chaine = list(my_string)
    for char in chaine:
        if char in ['c', 'C']:
            chaine.remove(char)
    new_string = ''.join(chaine)
    return new_string
