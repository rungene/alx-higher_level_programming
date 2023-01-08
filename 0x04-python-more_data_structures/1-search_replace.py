#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    a function that replaces all occurrences of an element by
    another in a new list
    """
    my_list2 = []
    for i in my_list:
        if i == search:
            i = replace
        my_list2.append(i)
    return my_list2
