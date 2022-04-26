#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    for i in range(len(str)):
        if i != n:
            strcpy += str[i]
    return(strcpy)
