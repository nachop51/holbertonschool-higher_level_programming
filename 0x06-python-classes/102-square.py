#!/usr/bin/python3
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

    def __eq__(self, other):
        """Equal to"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greather than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greather or equal than"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less or equal than"""
        return self.area() <= other.area()


s_5 = Square(5)
s_6 = Square(6)

if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")

if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
