#!/usr/bin/python3
"""
Base class module
Created on Monday 13.02.2023
@author: Rungene
"""
import json


class Base:
    """
    Base class

    Attributes:
       private int __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ method for initializing instance variables

        Attributes:
            id integer input for for id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method to_json_sting - converts
        an object to json representation

        Attributes:
            list_dictionaries -  is a list of dictionaries
        Return:
           t he JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         writes the JSON string representation of list_objs to a file:

         Attributes:
            list_objs: a list of instances who inherits of Base -
            example: list of Rectangle or list of Square instances
        Return:
            json object to save to file
        """
        out_file = cls.__name__ + ".json"
        json_string = []
        if list_objs is None:
            for i in list_objs:
                json_string.append(cls.to_json_string(i))
        with open(out_file, 'w', encoding='utf8')as json_file:
            json_file.write(cls.to_json_string(json_string))
