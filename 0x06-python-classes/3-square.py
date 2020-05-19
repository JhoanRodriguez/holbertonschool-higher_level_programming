#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0):
        """[summary]

        Keyword Arguments:
            size {int} -- size of square(default: {0})

        Raises:
            ValueError: must be > 0
            TypeError: must be an int
        """
        if (size < 0):
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """area

        Returns:
            [int] -- area of square
        """
        return self.__size * self.__size
