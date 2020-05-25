#!/usr/bin/python3
class Rectangle:
    """Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init funcion

        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle

        Returns:
            [int] -- area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Return the perimeter of  rectangle

        Returns:
            [int] -- perimeter of reactangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        """Print the rectangle with #

        Returns:
            [str] -- Return string to be printed
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = ("{}".format(self.print_symbol)) * self.width
        printed = width
        for x in range(0, self.height - 1):
            printed += "\n" + width
        return printed

    def __repr__(self):
        """Return a string of the representation

        Returns:
            [string] -- Return a representation of string
        """
        return ("Rectangle({},{})".format(self.width, self.height))

    def __del__(self):
        """Print message for deleted rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
