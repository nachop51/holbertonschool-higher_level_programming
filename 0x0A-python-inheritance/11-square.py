#!/usr/bin/python3
''' Module that creates a rectangle and a square class '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


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
