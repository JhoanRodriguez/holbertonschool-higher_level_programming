#!/usr/bin/python3
"""
This module contains a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This is the class Rectangle containing private instance
    attributes __width,  __height, __x and __y a class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiation of the class private instances
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        returns the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        returns the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        this function returns the area value of the
        rectangle
        """
        return self.height * self.width

    def display(self):
        """
        This function prints in stdout the rectangle
        """
        for item in range(self.y):
            print()
        for item in range(self.height):
            print((self.x * " ") + ("#" * self.width))

    def __str__(self):
        """
        This function returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        function assigns an argument to each attribute
        """
        if (len(args)):
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if (index == 1):
                    self.width = value
                if (index == 2):
                    self.height = value
                if (index == 3):
                    self.x = value
                if (index == 4):
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        This function returns the dictionary representation
        of a rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
