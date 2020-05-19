#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
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
            self.size = size
            self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area

        Returns:
            [int] -- area of square
        """
        return self.__size * self.__size

    def my_print(self):
        self.row = 0
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            while self.row < self.size:
                print("{}{}".format(" " * self.position[0], "#" * self.size))
                self.row += 1
