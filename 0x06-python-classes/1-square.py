#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module demonstrates an empty class Square that defines a square:
without  import any module
"""


class Square:
    """
    empty class Square that defines a square
    Attributes:
        none
    """
    def __init__(self, size=None):
        """
        the __init__ method for square class
        Args:
            size:private instance size of a square.
        """
        self.__size = size
