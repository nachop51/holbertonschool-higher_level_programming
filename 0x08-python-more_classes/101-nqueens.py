#!/usr/bin/python3
"""N queens problem"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    BOARD_SIZE = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)

if BOARD_SIZE < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


for solution in queens(BOARD_SIZE, 0, [], [], []):
    print(list(enumerate(solution)))


# def under_attack(col, queens):
#     return col in queens or \
#         any(abs(col - x) == len(queens)-i for i, x in enumerate(queens))


# def solve(n):
#     solutions = [[]]
#     for row in range(n):
#         solutions = [solution+[i]
#                      for solution in solutions
#                      for i in range(BOARD_SIZE)
#                      if not under_attack(i, solution)]
#     return solutions


# for answer in solve(BOARD_SIZE):
#     print(list(enumerate(answer)))
