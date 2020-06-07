#!/usr/bin/python3
"""
This module contains the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class contains instantiation of the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This function is the instantiation of the
        square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        This function returns the size (width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This function sets the size (width and height)
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns string representation of square
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        """
        This function assigns values and attributes
        """
        if (len(args)):
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if (index == 1):
                    self.size = value
                if (index == 2):
                    self.x = value
                if (index == 3):
                    self.y = value

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        This function contains the dictionary representation
        of the square
        """
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
