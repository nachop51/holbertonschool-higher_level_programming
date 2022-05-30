#!/usr/bin/python3
''' Module that creates a rectangle class '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
