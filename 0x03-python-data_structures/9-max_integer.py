#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        new = sorted(my_list)
        return new[-1]
    else:
        return None
