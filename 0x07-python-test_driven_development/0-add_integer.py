#!/usr/bin/python3
"""
Created on Sat 2nd Feb 2023

@author: Rungene
"""


def add_integer(a, b=98):
    """
     a function that adds 2 integers.

     Args:
        a(int): first parameter
        b(int): second parameter

     Raises:
        TypeError:if params are not ints

     Returns:
        an integer: the addition of a and b
    """
    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float and abs(a) <= 1.7976931348623158e+308 and b == b:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
