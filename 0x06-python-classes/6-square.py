#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module prints coordinates of a square
"""


class Square:
    """
    class Square that defines a square
    Attributes:
        size:of type int, the size of square
        position:must be a tupple of 2 positive ints
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        the __init__ method for square class
        Args:
            size:int private instance size of a square(optional).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        call the function to to retrieve the property
        Returns:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        checks the errors and sets position attribute

        Raises:
            TypeError: position must be 2 +ve integers
        """
        def contains_ints(value):
            """
            checks if the tuple contains only ints
            Return:
                true if contains only ints
            """
            return all(isinstance(x, int) for x in value)

        if contains_ints(value) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.position[0]):
                    print(end=" ")
                for k in range(self.__size):
                    print("#", end="")
                print()
