#!/usr/bin/python3
"""
rectangle.py module
Created on Monday 13.02.2023
@author: Rungene
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class, inherits from Base

    Attributes
        - None
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init class constructor

        Attributes
            - __width -> width private attribute for width of rectangle
            - __height -> height private attribute for height of rectangle
            - __x -> x private attribute for x value of rectangle
            - __y -> y private attribute for y value of rectangle
            -id (int) attribute id inherits from the base class
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
