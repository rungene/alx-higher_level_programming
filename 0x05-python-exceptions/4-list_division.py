#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    a function that divides element by element 2 lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements can’t be divided, the division result should be equal to 0
    """
    new_list = []
    try:
        new_list = [my_list_1 / my_list_2
                    for my_list_1, my_list_2 in zip(my_list_1, my_list_2)]
    except ValueError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return new_list
