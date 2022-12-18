#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
     a function that finds all multiples of 2 in a list.
     Return a new list with True or False
     """
    li_len = len(my_list)
    if li_len == 0:
        return None

    div_list = []
    for ele in my_list:
        if ele % 2 == 0:
            div_list.append(True)
        else:
            div_list.append(False)
    return div_list
