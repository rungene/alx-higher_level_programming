#!/usr/bin/python3
"""
Base class module
Created on Monday 13.02.2023
@author: Rungene
"""


class Base:
    """
    Base class

    Attributes:
       private int __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ method for initializing instance variables

        Attributes:
            id integer input for for id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
