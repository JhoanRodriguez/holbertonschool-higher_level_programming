#!/usr/bin/python3
"""BaseGeometry
    """


class BaseGeometry:
    """Empty class
    """
    pass

    def area(self):
        """Area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a value is an integer

        Arguments:
            name
            value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
