#!/usr/bin/python3
"""MyInt

    Returns:
        return the opposite of == and !=
    """


class MyInt(int):
    """MyInt

    Arguments:
        int return the opposite of == and !=
    """
    def __eq__(self, value):
        return not super().__eq__(value)

    def __ne__(self, value):
        return not super().__ne__(value)
