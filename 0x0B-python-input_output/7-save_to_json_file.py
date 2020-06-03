#!/usr/bin/python3
"""save to json file
    """
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an obj  to a text file
    """
    with open(filename, "w") as Myfile:
        Myfile.write(json.dumps(my_obj))
