#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


class BaseGeometry():
    """
    calculates the area

    Attributes:
        None
    """
    def __init__(self):
        """
        init method
        """
    def area(self):
        """
        Public instance method area

        Raises:
            Exception("area() is not implemented")
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method:
        validates value

        Attributes:
            name:always a string
            value (int):must be greater than 0
        Raises:
            TypeError(<name> must be an integer)
            ValueError(name> must be greater than 0)
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
