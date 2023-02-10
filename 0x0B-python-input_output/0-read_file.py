#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout:
    
    Attrubutes:
        filename(str):the name of the file to open
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
