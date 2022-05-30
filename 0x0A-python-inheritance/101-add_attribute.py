#!/usr/bin/python3
''' Module to add attribute to a class '''


def add_attribute(obj, att, value):
    ''' Adds an attribute to a class '''
    if hasattr(obj, "__slots__") and not hasattr(obj, att):
        raise TypeError("can't add new attribute")
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
