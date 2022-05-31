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
        a_dict = dict()
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
                if attr in self.__dict__:
                    a_dict.update({attr: self.__dict__[attr]})
            return a_dict
        return self.__dict__
