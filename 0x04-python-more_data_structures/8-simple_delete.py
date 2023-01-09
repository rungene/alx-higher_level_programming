#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
     a function that deletes a key in a dictionary.
     """
    keys = list(a_dictionary)
    keys.sort()
    for ke in keys:
        if ke == key:
            a_dictionary.pop(ke)
    return a_dictionary
