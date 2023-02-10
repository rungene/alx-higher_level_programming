#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""


def write_file(filename="", text=""):
    """
    function that writes a text file (UTF8)

    Attrubutes:
        filename(str):the name of the file to open
        text(str):the string to write

    Returns:
        the number of characters written:
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
