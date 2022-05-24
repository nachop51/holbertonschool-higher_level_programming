#!/usr/bin/python3
"""Calculates the multiplication of two given matrix"""


def matrix_mul(m_a, m_b):
    """Matrix multiplication with two given matrix"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for array in m_a:
        if not isinstance(array, list):
            raise TypeError("m_a must be a list of lists")
    for array in m_b:
        if not isinstance(array, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for array in m_a:
        for num in array:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("m_a should contain only integers or floats")
    for array in m_b:
        for num in array:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("m_b should contain only integers or floats")
    for array in m_a:
        if len(array) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for array in m_b:
        if len(array) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]
    # For rows in m_a
    for i in range(len(res)):
        # For cols in m_b
        for j in range(len(res[i])):
            # For rows in m_b
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res
