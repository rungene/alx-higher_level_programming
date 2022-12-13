#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix
    of integers.
    """
    for row in matrix:
        len_row = len(row)
        for val in range(len_row):
            if val != len_row - 1:
                print("{:d}".format(row[val]), end=' ')
            else:
                print("{:d}".format(row[val]), end='')
        print()
