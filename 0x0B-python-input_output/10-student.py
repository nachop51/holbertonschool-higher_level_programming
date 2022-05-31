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
            for attr in attrs:
                if not isinstance(attr, str):
                    return self.__dict__.copy()
            dict_copy = {}
            for attr in dict:
                if attr in self.__dict__:
                    dict_copy.update({attr: self.__dict__[attr]})
            return dict_copy
        return self.__dict__.copy()
