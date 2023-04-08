#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operator1 = ['+', '-', '*', '/']
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sucess = 1
    elif sys.argv[2] not in operator1:
        print("Unknown operator. Available operators: +, -, * and /")
        sucess = 1
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        print("{} {} {} ". format(a, operator, b), end="")

        if operator == "+":
            print("= {}". format(add(a, b)))
        if operator == "-":
            print("= {}". format(sub(a, b)))
        if operator == "*":
            print("= {}". format(mul(a, b)))
        if operator == "/":
            print("= {}". format(div(a, b)))
        sucess = 0
sys.exit(sucess)
