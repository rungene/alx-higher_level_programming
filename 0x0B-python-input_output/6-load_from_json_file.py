#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:

    Attributes:
        filename - json file to create the object from

    Return:
        python object
    """
    with open(filename, encoding='utf-8') as a_file:
        return (json.loads(a_file.read()))
