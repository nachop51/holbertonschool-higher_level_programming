#!/usr/bin/python3
""" Square module, creates a square model """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle class, from rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the instance of a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the square by args or kwargs """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """ Returns a dictionary representation of the square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
