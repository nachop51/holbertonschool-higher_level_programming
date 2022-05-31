#!/usr/bin/python3
""" Append to a file module """


def append_write(filename="", text=""):
    """ Opens a file in append mode, and writes some text """
    with open(filename, "a") as file:
        chars = file.write(text)
    return chars
