#!/usr/bin/python3
"""
class_to_json module
Created on Sunday 12.02.2023
@author: Rungene
"""


def class_to_json(obj):
    """
   seri;ialization of simple data structure (list, dictionary,
   string, integer and boolean) to JSON

   Attributes:
    obj:is an instance of a Class

    Return:
        the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for
        JSON serialization of an object:
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
