#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
     function that returns a list with all values
     multiplied by a number without using any loops.
     """
    list_mult = []
    list_mult = list(map((lambda x: x * number), my_list))
    return list_mult
