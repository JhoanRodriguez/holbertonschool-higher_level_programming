#!/usr/bin/python3
"""
Script to send requests to url and display body of response
"""
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get(argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
