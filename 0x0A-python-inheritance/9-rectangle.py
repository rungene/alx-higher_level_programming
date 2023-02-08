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

    def area(self):
        """
        area method, calculates the area of Rectanggle
        Attributes
            None
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ method, returns a string

        Return:
            following rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
