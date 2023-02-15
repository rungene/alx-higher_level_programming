#!/usr/bin/python3
"""
square.py module
Created on Wednesday 15.02.2023
@author: Rungene
"""
from models.base import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle

    Attributes
        - None
    """
        def __init__(self, size, x=0, y=0, id=None):
        """
        init class constructor for Square

        Attributes
            -size (int) the size of square
        """
        super().__init__(size, size, x, y, id)
        self.size = size
