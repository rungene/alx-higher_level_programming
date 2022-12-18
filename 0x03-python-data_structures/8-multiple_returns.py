#!/usr/bin/python3

def multiple_returns(sentence):
    """
    a function that returns a tuple with the
    length of a string and its first character.
    """
    if len(sentence) <= 0:
        return None
    else:
        length = len(sentence)
        first = sentence[0]
        return length, first
