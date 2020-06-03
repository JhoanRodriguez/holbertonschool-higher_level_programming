#!/usr/bin/python3
"""Read n lines
    """


def read_lines(filename="", nb_lines=0):
    """[summary]

    Keyword Arguments:
        filename str -- name of the file (default: {""})
        nb_lines int -- number of line to be read (default: {0})
    """
    with open(filename, encoding="UTF-8") as MyFile:
        counter = 0
        if nb_lines <= 0:
            print(MyFile.read())
        while counter < nb_lines:
            counter += 1
            line = MyFile.readline()
            print(line)
            if not line:
                break
