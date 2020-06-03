#!/usr/bin/python3
"""Append write
    """


def append_write(filename="", text=""):
    """Append write

    Keyword Arguments:
        filename {str} -- file to be appended (default: {""})
        text {str} -- text to be appended on the file (default: {""})

    Returns:
        [int] -- counter of lines appended
    """
    with open(filename, "a", encoding="UTF-8") as Myfile:
        return Myfile.write(str(text))
