#!/usr/bin/python3
""" Class to json """


def class_to_json(obj):
    """ Returns a json from an instance """
    return obj.__dict__
