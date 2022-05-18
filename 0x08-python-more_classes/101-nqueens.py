#!/usr/bin/python3
"""N queens problem"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    BOARD_SIZE = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if BOARD_SIZE < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(size, i, a, b, c):
    """Calculates the positions of the queens"""
    if i < size:
        for j in range(size):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(size, i + 1, a + [j],
                                  b + [i + j], c + [i - j])
    else:
        yield a


for solution in queens(BOARD_SIZE, 0, [], [], []):
    solve, i = [], 0
    for sol in solution:
        solve.append([i, sol])
        i += 1
    print(solve)
