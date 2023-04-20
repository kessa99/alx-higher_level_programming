#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not message:
        message = "C is fun"
    raise NameError(message)
