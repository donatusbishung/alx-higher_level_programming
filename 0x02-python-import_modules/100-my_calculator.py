#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    new_args = len(argv) - 1
    if new_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    optrn = argv[2]
    if optrn != '+' and optrn != '-' and optrn != '*' and optrn != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])

    if optrn == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif optrn == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif optrn == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
