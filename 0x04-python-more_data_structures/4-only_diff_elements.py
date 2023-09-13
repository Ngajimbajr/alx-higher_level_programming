#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_set = set()

    # Iterate through set_1 and check if each element is not in set_2
    for element in set_1:
        if element not in set_2:
            diff_set.add(element)

    # Iterate through set_2 and check if each element is not in set_1
    for element in set_2:
        if element not in set_1:
            diff_set.add(element)

    return diff_set
