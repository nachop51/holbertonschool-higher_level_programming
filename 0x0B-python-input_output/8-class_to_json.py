#!/usr/bin/python3
import json
""" Class to json """


def class_to_json(obj):
    """ Returns a json from an instance """
    return json.dumps(obj.__dict__)
