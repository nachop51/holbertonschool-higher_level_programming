#!/usr/bin/python3
''' Module that inverts eq and ne methods of int class '''


class MyInt(int):
    ''' MyInt class '''

    def __eq__(self, other):
        """Equal to inverted"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal to inverted"""
        return super().__eq__(other)
