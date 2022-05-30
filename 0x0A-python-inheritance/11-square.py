#!/usr/bin/python3
''' Module that creates a rectangle and a square class '''


class BaseGeometry:
    ''' BaseGeometry class '''

    def area(self):
        ''' Area function (not implemented) '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates a value '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    ''' Rectangle class '''

    def __init__(self, width, height):
        ''' Initializes an instance of a rectangle '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Overrides the area method, and returns the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' Prints the dimensions of the rectangle '''
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    ''' Square class '''

    def __init__(self, size):
        ''' Initializes an instance of a square '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Overrides the area method, and returns the area '''
        return self.__size ** 2

    def __str__(self):
        ''' Prints the dimensions of the square '''
        return f"[Square] {self.__size}/{self.__size}"
