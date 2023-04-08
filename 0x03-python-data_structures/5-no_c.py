#!/usr/bin/python3
def no_c(my_string):
    chaine = list(my_string)
    idx = 0
    while idx < len(chaine):
        if chaine[idx] in ['c', 'C']:
            chaine.pop(idx)
        else:
            idx += 1
    new_string = ''.join(chaine)
    return new_string
