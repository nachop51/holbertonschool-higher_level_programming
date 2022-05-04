#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s_mtx = []
    for row in matrix:
        s_mtx.append(list(map(lambda x: x**2, row)))
    return s_mtx
