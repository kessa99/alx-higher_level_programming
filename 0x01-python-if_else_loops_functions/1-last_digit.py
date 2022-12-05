#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if (number > 0):
    if (last > 5):
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
    elif (last < 6):
        print(f"Last digit of {number} is {number % 10} and is less then 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is 0")
elif (number < 0):
    if (last > 5):
        print(f"Last digit of {number} is -{number % 10} and is greater than 5")
    elif (last < 6):
        print(f"Last digit of {number} is -{number % 10} and is less then 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is 0")

