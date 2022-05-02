#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxn = 0
        for i in my_list:
            if i > maxn:
                maxn = i
        return maxn
    return None
