#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle/BaseGeometry

    Attributes:
        None
    """
    def __init__(self, size):
        """
        __init__method for square.

        Attributes:
            self.size = size(size of square,must be int)
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        __str__ method for square.

        Returns:
            return, the square description: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
