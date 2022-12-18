#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    a function that finds the biggest integer of a list.
    """
    lilen = len(my_list)
    if lilen == 0:
        return None
    else:
        largest_num = my_list[0]
        for number in my_list:
            if largest_num < number:
                largest_num = number
        return largest_num
