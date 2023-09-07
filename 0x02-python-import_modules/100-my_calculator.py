#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = map(str.strip, sys.argv[1:4])

    if operator not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operations = {'+': add, '-': sub, '*': mul, '/': div}
    result = operations[operator](int(a), int(b))
    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()

