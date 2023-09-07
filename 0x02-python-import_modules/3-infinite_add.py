#!/usr/bin/python3

import sys

def main():
    # Get the command-line arguments, excluding the script name
    arguments = sys.argv[1:]

    # Initialize a variable to store the sum
    total = 0

    # Loop through the arguments and add them to the total
    for arg in arguments:
        total += int(arg)

    # Print the result
    print(total)

if __name__ == "__main__":
    main()

