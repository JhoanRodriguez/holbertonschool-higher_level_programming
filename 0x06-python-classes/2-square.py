#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Class Square

        Keyword Arguments:
            size {int} -- size of square(default: {0})

        Raises:
            ValueError: must be > 0
            TypeError: must be an int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
