#!/usr/bin/python3
"""
This file contains a function
that creates an object from a "JSON FILE"
"""
import json


def load_from_json_file(filename):
    """
    function that creates obj from json file
    """
    with open(filename) as Myfile:
        return json.loads(Myfile.read())
