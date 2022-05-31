#!/usr/bin/python3
""" Writes a file some given text """


def write_file(filename="", text=""):
    """ Opens a file and writes on it """
    with open(filename, "w") as file:
        chars = file.write(text)
    return chars
