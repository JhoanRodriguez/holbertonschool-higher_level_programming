#!/usr/bin/python3
def add_attribute(ob, attr, value):
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
