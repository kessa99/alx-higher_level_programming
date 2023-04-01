#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        print("{}".format(str))
    else:
        new_str = list(str)
        new_str.pop(n)
        j = "".join(new_str)
        print("{}".format(j))
