#!/usr/bin/python3
islower = __import__('7-islower').islower

print("\" is {}".format("lower" if islower("\"") else "upper"))
print("4 is {}".format("lower" if islower("4") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
