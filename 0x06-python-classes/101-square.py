#!/usr/bin/python3
"""Creates a square class."""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square instance"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Defines the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square"""
        if self.size == 0:
            print()
        else:
            position = self.position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for i in range(self.size):
                print(" " * position[0] + "#" * self.size)

    def __str__(self):
        """Prints the square"""
        string = ""
        if self.size == 0:
            string += "\n"
        else:
            position = self.position
            if position[1] > 0:
                for i in range(position[1]):
                    string += "\n"
            for i in range(self.size):
                string += " " * position[0] + "#" * self.size + "\n"
        return string[:-1]
