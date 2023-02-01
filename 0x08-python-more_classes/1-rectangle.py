#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 1.2.23
@author: Rungene
"""


class Rectangle:
    """
     class Rectangle that defines a rectangle

     Attributes:
        None
     """
    def __init__(self, width=0, height=0):
        """
        init method for a rectagle

        Attributes:
           width(must be int, optional) the width of rectangles
           height(must be int, optional. the height of rectangles)
           self.height = height
           self.width = width
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        property width to retrive width
          Returns:
              width,of type int. The height of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width of the Rectangle,type int

        Attributes:
            width(int):the width of Rectangle
        Raises:
            TypeError:if width is not an integer
            ValueError: if width < 0
        """
        if type(value) is int:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        property height to retrive height
          Returns:
              height,of type int. The height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter height of the rectangle,type int

        Attributes:
            height(int):the height of Rectangle
        Raises:
            TypeError:if height is not an integer
            ValueError: if height < 0
        """
        if type(value) is int:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
