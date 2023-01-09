#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    a function that returns a new dictionary
    with all values multiplied by 2
    """
    b_dict = dict(a_dictionary)
    for ke, val in sorted(b_dict.items()):
        b_dict[ke] = val * 2
    return b_dict
