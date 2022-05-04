#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        dict = a_dictionary.copy()
        for k, v in dict.items():
            dict[k] = v * 2
        return dict
