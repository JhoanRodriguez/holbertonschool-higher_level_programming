#!/usr/bin/python3
"""add_attribute
    """


def add_attribute(ob, attr, value):
    """add an attribute

    Arguments:
        ob dict
        attr
        value

    Raises:
        TypeError: can't add new attribute
    """
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
