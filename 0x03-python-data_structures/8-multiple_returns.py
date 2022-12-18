#!/usr/bin/python3

def multiple_returns(sentence):
    """
    a function that returns a tuple with the
    length of a string and its first character.
    """
    strlen = len(sentence)
    if strlen == 0:
        first = None
    else:
        first = sentence[0]
    return (strlen, first)
