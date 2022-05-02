#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for i in item:
            print(i, end=" " if i != item[-1] else "")
        print()
