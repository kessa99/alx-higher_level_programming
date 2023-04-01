#!/usr/bin/python3
char1 = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(char1)-1, -1, -1):
    print("{}".format(char1[i] if i % 2 != 0 else char1[i].upper()), end="")
