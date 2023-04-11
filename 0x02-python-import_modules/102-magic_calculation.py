#!/usr/bin/python3
import dis
import calculator_1
def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
dis.dis(magic_calculation.__code__.co_code)
