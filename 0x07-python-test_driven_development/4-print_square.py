#!/usr/bin/python3
"""Prints a square with a given size"""


def print_square(size):
    """With a given number this function prints a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        print((f"{('#' * size)}\n" * size)[:-1])
