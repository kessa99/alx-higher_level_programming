#!/usr/bin/python3
if __name__ == "__main":
    from calculator_1.py import add, sub, mul,div
    import sys

    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("{}".format(len(sys.argv)))
     sys.exit(1)


    
