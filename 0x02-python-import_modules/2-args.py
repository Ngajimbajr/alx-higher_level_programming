#!/usr/bin/python3

import sys

def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
        return

    print(f"{num_args}")

    if num_args == 1:
        print("Argument:")
    else:
        print("Arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    args = sys.argv[1:]
    print_arguments(args)
