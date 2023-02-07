#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


def is_same_class(obj, a_class):
    """
    compares to objects for equality

    Returns:
        True if the object is exactly an instance
        of the specified class ; otherwise False.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return type(obj) is a_class
