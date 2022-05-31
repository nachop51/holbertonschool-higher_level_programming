#!/usr/bin/python3
import json
""" Saves to a json file """


def save_to_json_file(my_obj, filename):
    """ Opens a file and dumps a json """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
