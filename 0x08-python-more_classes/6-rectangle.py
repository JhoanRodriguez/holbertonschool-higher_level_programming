#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle():
    """Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiation function
        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of a rectangle
        Returns:
            int -- area
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of a rectangle
        Returns:
            int -- perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Print the rectangle with #

        Returns:
            [str] -- Return string to be printed
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        printed = width
        for x in range(0, self.height - 1):
            printed += "\n" + width
        return printed

    def __repr__(self):
        """Return a string of the representation

        Returns:
            [string] -- Return a representation of string
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Print message for deleted rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
