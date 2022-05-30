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
