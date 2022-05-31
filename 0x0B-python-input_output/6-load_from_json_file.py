#!/usr/bin/python3
import json
""" Load from json file module """


def load_from_json_file(filename):
    """ Loads data from a json file """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
