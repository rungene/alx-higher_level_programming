#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object

    Returns:
        a list object
    """
    return dir(obj)
