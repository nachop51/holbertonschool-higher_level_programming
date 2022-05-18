#!/usr/bin/python3
"""Creates a rectangle class."""


class Rectangle:
    """Defines a rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle class."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """Prints the rectangle"""
        string = ""
        if self.height == 0 or self.width == 0:
            string += "\n"
        else:
            for i in range(self.height):
                string += "#" * self.width + "\n"
        return string[:-1]

    def __repr__(self):
        """Returns a representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor method of the class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
