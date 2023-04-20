#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for idx in range(x):
            if isinstance(my_list[idx], int):
                print("{}".format(my_list[idx]), end="")
                count += 1
            else:
                pass
    except IndexError:
        pass
    print()
    return count
