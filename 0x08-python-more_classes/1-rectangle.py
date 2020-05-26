#!/usr/bin/python3
"""Rectangle class

    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: height must be an integer
        ValueError: height must be >= 0

    Returns:
        int -- dimensions for the rectangle
    """


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """init funcion

        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width if setter checks have passed
        Returns:
            int -- width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter validates if value is >= 0
        Arguments:
            value {int} -- Value to be setted
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return height if setter checks have passed
        Returns:
            int -- height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter validates if value is >= 0
        Arguments:
            value {int} -- Value to be setted
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
