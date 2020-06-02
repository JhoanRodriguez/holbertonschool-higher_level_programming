#!/usr/bin/python3
"""MyList
    """


class MyList(list):
    """Print a sorted list

    Arguments:
        list {[list]}
    """
    def print_sorted(self):
        print(sorted(self))
