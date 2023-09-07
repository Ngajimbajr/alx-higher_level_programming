#!/usr/bin/python3

import sys

def main():
    # Get the command-line arguments, excluding the script name
    arguments = sys.argv[1:]

    # Initialize a variable to store the sum
    result = 0

    # Loop through the arguments and add them to the total
    for arg in arguments:
        result += int(arg)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()

