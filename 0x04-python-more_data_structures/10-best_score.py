#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        highest = ["", 0]
        for k, v in a_dictionary.items():
            if v > highest[1]:
                highest = [k, v]
        return highest[0]
    else:
        return None
