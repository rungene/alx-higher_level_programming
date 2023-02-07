#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


def is_kind_of_class(obj, a_class):
    """
    compares if the object is an instance of, or if the
    object is an instance of a class that inherited from,
    the specified class

    Returns:
        True if the object is an instance, or if
        the object is an instance of a class that inherited from
        the specified class ; otherwise False.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type a")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
