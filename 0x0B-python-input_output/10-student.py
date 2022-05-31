#!/usr/bin/python3
""" student module, creates a class student """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """ Initiliazes the instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a json about the class """
        dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
        }
        if attrs and isinstance(attrs, list):
            dict_copy = dict.copy()
            for attr in dict:
                if attr not in attrs:
                    dict_copy.pop(attr)
            dict = dict_copy
        return dict