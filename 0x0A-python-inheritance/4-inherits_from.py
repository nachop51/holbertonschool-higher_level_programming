#!/usr/bin/python3
''' Module inherits_from '''


def inherits_from(obj, a_class):
    ''' Checks if inherits or not '''
    return isinstance(obj, a_class) and type(obj) != a_class
