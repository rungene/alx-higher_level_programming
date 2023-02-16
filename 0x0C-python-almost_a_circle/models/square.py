#!/usr/bin/python3
"""
square.py module
Created on Wednesday 15.02.2023
@author: Rungene
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle

    Attributes
        - None
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init class constructor for Square

        Attributes
            -size (int) the size of square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        __str__ method that return  a string represenation
        of an object(class)

        Return:
            [Square] (<id>) <x>/<y> - <size>(width or height)
        """
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)

    @property
    def size(self):
        """
        property method size value

        Returns:
            private value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size value

        Attribute:
            value: int value to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

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
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) > 0:
            for (k, v) in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
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
        return {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y}
