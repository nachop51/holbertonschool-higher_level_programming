#!/usr/bin/python3
""" Module that reads a file and prints its content """


def read_file(filename=""):
    """ Opens a file and reads from it """
    with open(filename, "r") as file:
        print("".join(file.readlines()))
