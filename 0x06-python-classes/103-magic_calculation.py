#!/usr/bin/python3
"""Math module"""
import math


class MagicClass:
    """Magic class"""

    def __init__(self, radius=0):
        """Initialization of the class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Returns the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference"""
        return 2 * math.pi * self._MagicClass__radius
