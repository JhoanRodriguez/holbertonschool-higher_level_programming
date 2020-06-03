#!/usr/bin/python3
"""Read file
    """


def read_file(filename=""):
    """Read file

    Keyword Arguments:
        filename {str} -- file to be read (default: {""})
    """
    with open(filename, encoding="UTF-8") as MyFile:
        line = MyFile.readline()
        while line:
            print(line, end="")
            line = MyFile.readline()
        print("")
