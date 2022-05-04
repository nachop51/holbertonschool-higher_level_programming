#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        a_dictionary.pop(key, "not found")
        return a_dictionary
