#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    a function that prints a dictionary by ordered keys.
    """
    for key, value in sorted(a_dictionary.items()):
        print(f'{key}: {value}')
