#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        delete = []
        for k, v in a_dictionary.items():
            if v == value:
                delete.append(k)
        if delete != []:
            length = len(delete)
            i = 0
            while length > 0:
                a_dictionary.pop(delete[i])
                i += 1
                length -= 1
        return a_dictionary
