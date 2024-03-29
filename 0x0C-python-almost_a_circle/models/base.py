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
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(out_file, 'w', encoding='utf-8')as json_file:
            json_file.write(cls.to_json_string(string))

    def from_json_string(json_string):
        """
        json string to a dictionary

        Attribute:
            json_string - is a string representing a list of dictionaries
        Return:
            the list of the JSON string representation json_string
            if json_string is None or empty, return an empty list
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method create - takes in a dictinary converts to an instance.

        Attribute
            dictionary - used as **kwargs of the method upda

        Return:
            returns an instance with all attributes already set:
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Shape":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method

        Return:
             returns a list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []

        try:
            with open(file_name, 'r', encoding='utf-8')as o_file:
                json_obj = cls.from_json_string(o_file.read())
            for (key, value) in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except Exception:
            pass
        return json_obj
