#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        delete = ""
        for k, v in a_dictionary.items():
            if v == value:
                delete = k
        if delete != "":
            a_dictionary.pop(delete)
        return a_dictionary
