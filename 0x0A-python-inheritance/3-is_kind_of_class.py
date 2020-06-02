#!/usr/bin/python3
"""is kind of class
    """


def is_kind_of_class(obj, a_class):
    """Verify if the a_class is an instance of the obj

    Arguments:
        obj class type
        a_class class type

    Returns:
        Boolean -- True or False
    """
    return (isinstance(obj, a_class))
