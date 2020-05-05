#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return (new)
        new[idx] = element
        return (new)
