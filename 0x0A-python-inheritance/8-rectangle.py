#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Recatangle class inherit from BaseGeometry

    Arguments:
        BaseGeometry class type
    """
    def __init__(self, width, height):
        """instantion of class

        Arguments:
            width int
            height int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
