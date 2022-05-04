#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        s_mtx = []
        for row in matrix:
            s_mtx.append(list(map(lambda x: x**2, row)))
        return s_mtx


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
