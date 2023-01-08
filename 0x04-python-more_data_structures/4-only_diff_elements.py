#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    a function that returns a set of all elements present in only one set.
    """
    c_set = ((set_1 | set_2) - (set_1 & set_2))
    return c_set
