#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        list = []
        for k, v in a_dictionary.items():
            list.append([k, v])
        list = sorted(list)
        for row in list:
            print(f"{row[0]}: {row[1]}")
