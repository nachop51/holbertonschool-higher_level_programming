#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        l = []
        for k, v in a_dictionary.items():
            l.append([k, v])
        l = sorted(l)
        for row in l:
            print(f"{row[0]}: {row[1]}")
