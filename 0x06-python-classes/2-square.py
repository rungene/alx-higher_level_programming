#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module demonstrates Size validation
"""


class Square:
    """
    empty class Square that defines a square
    Attributes:
        none
    """
    def __init__(self, size=0):
        """
        the __init__ method for square class
        Args:
            size:int private instance size of a square(optional).
        Raises:
            TypeError:size must be an integer
            ValueError :size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
