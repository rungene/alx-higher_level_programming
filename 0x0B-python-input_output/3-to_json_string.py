#!/usr/bin/python3
import json
"""
Created on Friday 10.02.2023
@author: Rungene
"""


def to_json_string(my_obj):
    """
    converts a python object (string)
    to the JSON representation

    Attributes:
        my_obj - python object to convert

    Return:
        the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
