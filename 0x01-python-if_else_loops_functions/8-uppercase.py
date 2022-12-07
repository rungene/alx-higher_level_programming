#!/usr/bin/python3

def uppercase(str):
    for upper in str:
        if ord(upper) >= 97 and ord <= 122:
            print("{}".format(chr(ord(upper) - 32)))
        else:
            print("{}".format(upper))
