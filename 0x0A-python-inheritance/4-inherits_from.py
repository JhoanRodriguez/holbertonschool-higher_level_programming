#!/usr/bin/python3
"""inherit from
    """


def inherits_from(obj, a_class):
    """[summary]

    Arguments:
        obj type class
        a_class type class

    Returns:
        Boolean -- True or False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
