#!/usr/bin/python3
""" Module pascal triangle """


def pascal_triangle(n):
    ''' Returns a list of lists of integers of the pascal triangle '''
    if n <= 0:
        return []
    pascal = []
    for i in range(1, n + 1):
        row = [0 for _ in range(i)]
        for num in range(len(row)):
            if num == 0 or num == len(row) - 1:
                row[num] = 1
            else:
                row[num] += pascal[len(row) - 2][num] + \
                    pascal[len(row) - 2][num - 1]
        pascal.append(row)
    return pascal
