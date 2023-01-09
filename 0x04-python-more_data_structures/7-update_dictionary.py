#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    a function that replaces or adds key/value in a dictionary.
    """
    for ke, val in sorted(a_dictionary.items()):
        if ke == key:
            a_dictionary[ke] = value
        else:
            a_dictionary[key] = value
    return a_dictionary
