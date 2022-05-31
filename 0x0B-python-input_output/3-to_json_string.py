#!/usr/bin/python3
""" json representation of a python object """
import json


def to_json_string(my_obj):
    """ To json string function, returns the object """
    return json.dumps(my_obj)
