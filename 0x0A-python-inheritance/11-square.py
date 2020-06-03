#!/usr/bin/python3
"""
Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from rectangle
    Arguments:
        Rectangle {class} -- Class rectangle
    """
    def __init__(self, size):
        """ Square class that inherits from rectangle
        Arguments:
            size {int} -- size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """print funcion

        Returns:
            string
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
