#!/usr/bin/python3

def element_at(my_list, idx):
    """
    A function that retrives an element
    from a list and returns it
    """
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    return (my_list[idx])
