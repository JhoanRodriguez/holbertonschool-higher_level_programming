#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new = my_string
        new = new.translate({ord(i): None for i in 'cC'})
        return (new)
    new = my_string
    return (new)
