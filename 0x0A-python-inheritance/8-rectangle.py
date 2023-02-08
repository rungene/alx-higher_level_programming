#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry

    Attributes:
        None
    """
    def __init__(self, width, height):
        """
        __init__method.

        Attributes:
            self.width = width
            self.height = height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
