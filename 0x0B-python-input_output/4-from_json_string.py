#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""
import json


def from_json_string(my_str):
    """
    converts JSON string to an object (Python data structure)

    Attributes:
        my_str(str) - json string

    Return:
        returns an object (Python data structure) from json
    """
    return json.loads(my_str)
