#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file

    Attrubutes:
        filename(str):the name of the file to open
        text(str):the string to append

    Returns:
        the number of characters added:
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
