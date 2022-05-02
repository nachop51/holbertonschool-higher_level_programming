#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i, v in enumerate(my_list):
        if i == idx:
            my_list.remove(v)
    return my_list
