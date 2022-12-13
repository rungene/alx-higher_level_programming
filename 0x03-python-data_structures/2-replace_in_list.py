#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    A function that replaces an element
    from a list and returns it
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
