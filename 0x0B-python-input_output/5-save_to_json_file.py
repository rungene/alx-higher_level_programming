#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation:

    Attributes:
        my_obj - python object
        filename - json file to write to

    Return:
        file in json format
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        return (a_file.write(json.dumps(my_obj)))
