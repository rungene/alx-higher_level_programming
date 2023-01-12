#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    a function that divides element by element 2 lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements can’t be divided, the division result should be equal to 0
    """
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = (my_list_1[i]/my_list_2[i])
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
