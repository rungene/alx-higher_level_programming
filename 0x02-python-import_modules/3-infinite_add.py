#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()
sum = 0
for args in range(1, len(sys.argv)):
    sum += int(sys.argv[args])
print(sum)
