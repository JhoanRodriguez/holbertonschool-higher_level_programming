#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new = ""
        new = new + my_string
        return (new.translate({ord(i): None for i in 'cC'}))
