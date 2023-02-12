#!/usr/bin/python3
"""
Student class module
Created on Sunday 12.02.2023
@author: Rungene
"""


class Student():
    """
    class student, defines a student.

    Attributes:
        None
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ method

        Attributes-public instance
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json - Public method. retrieves a dictionary
        representation of a Student instance

        Return:
            student class as json format
        """
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
