#!/usr/bin/python3
""" Append after module """


def append_after(filename="", search_string="", new_string=""):
    """ Append after function """
    with open(filename, "r") as file:
        data = file.readlines()
    content = ""
    for line in data:
        content += line
        if search_string in line:
            content += new_string
    with open(filename, "w") as file:
        file.write(content)
