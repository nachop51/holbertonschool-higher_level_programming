#!/usr/bin/python3
"""Divides a given matrix by a given number"""


def matrix_divided(matrix, div):
    """Checks if the matrix and the
    div number is valid, and then
    proceeds to divide the matrix by div
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for array in matrix:
        if not isinstance(array, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(array) == len(matrix[0]):
            check_array(array)
        else:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x/div, 2), array)) for array in matrix]


def check_array(array):
    """Checks for each number of the array
    if the number is valid (int/float)
    """
    for number in array:
        if not isinstance(number, int) and not isinstance(number, float):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
