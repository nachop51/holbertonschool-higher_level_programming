#!/usr/bin/python3
def convert_nums(string):
    list = []
    for i in string:
        if i == "M":
            list.append(1000)
        elif i == "D":
            list.append(500)
        elif i == "C":
            list.append(100)
        elif i == "L":
            list.append(50)
        elif i == "X":
            list.append(10)
        elif i == "V":
            list.append(5)
        elif i == "I":
            list.append(1)
        else:
            return None
    return list


def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        list = convert_nums(roman_string)
        if list is not None:
            list.insert(0, 0)
            for i in range(len(list)):
                if i == 0:
                    r = 0
                    c = 0
                    v = list.pop()
                    continue
                if v >= c:
                    r += v
                else:
                    r -= v
                c = v
                v = list.pop()
            return r
        else:
            return 0
    return 0
