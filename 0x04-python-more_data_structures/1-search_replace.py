#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = my_list.count(search)
    while count > 0:
        idx = new_list.index(search)
        new_list[idx] = replace
        count -= 1
    return new_list
