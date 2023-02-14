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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        public method for calculating the area of rectangle

        Return:
            Area of rectangle
        """
        return self.width * self.height

    @property
    def width(self):
        """
        propert method width

        Returns:
            private value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width value

        Attributes:
            value-value to check if int />0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        property method for getting height

        Return:
            private value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height value

        Attributes:
            value - value to check if int and > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        property method for getting x

        Return:
            private value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x value

        Attributes:
            value - value to check if int and > 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        property method for getting y

        Return:
            private vallue y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y value

        Attributes:
            value - value to check if int and > 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def display(self):
        """
        display method.prints in stdout the Rectangle
        instance with the character #
        """
        for i in range(self.height):
            for x in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        __str__ method that return  a string represenation
        of an object

        Return:
            The string: [class_name] (id) x/y - width/height
        """
        return '[{}] {} {}/{} - {}/{}'.format(self.__class__name,
                                              self.id, self.x, self.y,
                                              self.width, self.height)
