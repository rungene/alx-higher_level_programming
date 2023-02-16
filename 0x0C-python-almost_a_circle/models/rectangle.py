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
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
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
        return '[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """
        update method.assigns an argument to each attribute:

        Attribute:
            args(list): list of inputs to update the rectangle class
            kwargs: dictionary of inputss to update the reclangle class
        """
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) > 0:
            for (k, v) in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        public method to_dictionary

        Return:
            returns the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
