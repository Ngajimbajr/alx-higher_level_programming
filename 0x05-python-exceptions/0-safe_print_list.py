#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()  # Add a new line after printing all elements
        return count
    except IndexError:
        print()
        return count
