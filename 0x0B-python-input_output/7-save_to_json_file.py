#!/usr/bin/python3
import json
"""save to json file
    """


def save_to_json_file(my_obj, filename):
    """
    function that writes an obj  to a text file
    """
    with open(filename, "w") as Myfile:
        Myfile.write(json.dumps(my_obj))
