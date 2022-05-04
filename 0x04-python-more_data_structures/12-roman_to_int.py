#!/usr/bin/python3
def convert_nums(string):
    l = []
    for i in string:
        if i == "M":
            l.append(1000)
        elif i == "D":
            l.append(500)
        elif i == "C":
            l.append(100)
        elif i == "L":
            l.append(50)
        elif i == "X":
            l.append(10)
        elif i == "V":
            l.append(5)
        elif i == "I":
            l.append(1)
        else:
            return None
    return l


def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        l = convert_nums(roman_string)
        if l is not None:
            l.insert(0, 0)
            for i in range(len(l)):
                if i == 0:
                    r = 0
                    c = 0
                    v = l.pop()
                    continue
                if v >= c:
                    r += v
                else:
                    r -= v
                c = v
                v = l.pop()
            return r
        else:
            return 0
    return 0


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
