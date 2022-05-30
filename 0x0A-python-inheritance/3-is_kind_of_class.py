#!/usr/bin/python3
''' Module that checks if is kind of class '''


def is_kind_of_class(obj, a_class):
    '''
    function that returns if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class
    '''
    return isinstance(obj, a_class)
