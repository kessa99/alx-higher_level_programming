#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list:
        try:
            if count < x:
                print(item, end=" ")
                count += 1
            else:
                break
        except:
            break
    print()
