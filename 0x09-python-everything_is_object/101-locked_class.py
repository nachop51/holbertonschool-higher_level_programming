#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Locked Class"""
    __slots__ = ['first_name']

    def __init__(self, value=""):
        """Inits the instance"""
        self.first_name = value
