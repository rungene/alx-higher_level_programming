#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
     a function that adds all unique integers in
     a list (only once for each integer).
     """
    sum_unique = 0
    unique_list = set(my_list)
    for i in unique_list:
        sum_unique += i
    return sum_unique
