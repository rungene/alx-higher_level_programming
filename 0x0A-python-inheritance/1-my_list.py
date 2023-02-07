#!/usr/bin/python3
"""
Created on Tuesday 7.02.2023
@author: Rungene
"""


class MyList(list):
    """
    inherits from list:

    Attributes:
        None
    """
    def print_sorted(self):
        """
        Public instance method
        prints the list(type int), but sorted (ascending sort)
        """
        mylist = self[:]
        mylist.sort()
        print(mylist)
