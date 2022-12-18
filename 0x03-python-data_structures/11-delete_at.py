#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    li_len = len(my_list)
    if idx > li_len - 1 or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
