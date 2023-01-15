#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module prints a square
"""


class Square:
    """
    class Square that defines a square
    Attributes:
        size:of type int, the size of square
    """
    def __init__(self, size=0):
        """
        the __init__ method for square class
        Args:
            size:int private instance size of a square(optional).
        """
        self.size = size

    @property
    def size(self):
        """
        call the function to get the property
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Check the errors and sets the size attribute

        Raises:
            TypeError:size must be an integer
            ValueError :size must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square

        returns the current square area
        """
        return ((self.__size) ** 2)

    def my_print(self):
        """
        Public instance method
        prints in stdout the square with the character #
        """
        if self.__size:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
