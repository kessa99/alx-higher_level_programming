#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        interger_value = int(value)
    except ValueError:
            print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
            return True
    else:
        print("{}".format(interger_value))
        return False
