#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for x, y in zip(my_list_1, my_list_2):
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                print("wrong type")
                result.append(0)
            elif y == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(x / y)
    except IndexError:
        print("out of range")
    finally:
        while len(result) < list_length:
            result.append(0)
    return result
