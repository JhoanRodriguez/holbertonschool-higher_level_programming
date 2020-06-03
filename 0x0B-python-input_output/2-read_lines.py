#!/usr/bin/python3
"""
This file contains functions that
reads n lines of a txt file and prints
it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines
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
