#!/usr/bin/python3
def matrix_divided(matrix, div):
    """  divides all elements of a matrix.

    Args:
        matrix:must be a list of ints or floats
        div:must be a nits/floats

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats\
        Each row of the matrix must have the same size
        ZeroDivisionError: if div == 0

    Returns:
        Returns a new matrix
    """
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
        return matrix

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
        return matrix

    if div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix
    if type(matrix) is list:
        new_matrix = [x[:] for x in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
                    return matrix
                else:
                    new_matrix[i][j] = round(matrix[i][j]/div, 2)
    else:
        raise TypeError("x must be a matrix (list of lists)\
        of integers/floats")
    return new_matrix
