#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function that prints x elements of a list.
    Returns the real number of elements printed
    """
    i = 0
    try:
        while i < x:
            print(my_list[i], end ="")
            i += 1
    except Exception:
        pass
    print()
    return i
