#!/usr/bin/python3
"""Read file
    """


def number_of_lines(filename=""):
    """Red file

    Keyword Arguments:
        filename str -- file to be read default: {""}

    Returns:
        int -- return the number of lines
    """
    with open(filename, encoding="UTF-8") as MyFile:
        counter = 0
        line = MyFile.readline()
        while line:
            counter += 1
            line = MyFile.readline()

    return counter
