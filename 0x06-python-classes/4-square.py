#!/usr/bin/python3
"""Creates a square class."""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the square instance"""
        self.size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
