#!/usr/bin/python3

def uppercase(str):
    for upper in str:
        if ord(upper) >= 97 and ord <= 122:
            print("{:c}".format(chr(ord(upper) - 32), end=''))
        else:
            print("{:c}".format(upper), end='')
