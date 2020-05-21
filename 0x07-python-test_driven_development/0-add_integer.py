#!/usr/bin/python3
"""add two numbers"""


def add_integer(a, b=98):
    """add two numbers, cast to int and return it.

    Arguments:
        a {[int, float]} -- number1

    Keyword Arguments:
        b {int, float} -- number2 (default: {98})

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        [int] -- return a + b
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
