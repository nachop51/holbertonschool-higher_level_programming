#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    div = 0
    for tuple in my_list:
        sum += tuple[0] * tuple[1]
        div += tuple[1]
    return (sum / div)
