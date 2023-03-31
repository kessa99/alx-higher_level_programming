#!/usr/bin/python3
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(a)-1, -1, -1):
  if i % 2 != 0:
    print(a[i], end="")
  else:
    print(b[i], end="")
