#!/usr/bin/python3
''' Module that inherits and adds a method '''


class MyList(list):
    ''' MyList class that inherits of class list '''

    def print_sorted(self):
        ''' Prints the list sorted '''
        print(sorted(self))
