#!/usr/bin/python3
"""
This module creates a class
student with defined attributes
"""


class Student:
    """
    This class is defining the attributes for
    the said class
    """
    def __init__(self, first_name, last_name, age):
        """
        This is the instantiation of the attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            return (self.__getattribute__(attrs.name))