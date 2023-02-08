#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


def inherits_from(obj, a_class):
    """
    compares bject is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Returns:
        Returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified
        class ; otherwise False.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be type")
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
