#!/usr/bin/python3
"""
This module adds two integers and returns sum of two numbers a & b.
Only accepts integers and floats else TypeError is raised
This module will convert float to integer
"""


def add_integer(a, b=98):
    """
    add_integer: Check input if correct, cast both into ints and return sum
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
