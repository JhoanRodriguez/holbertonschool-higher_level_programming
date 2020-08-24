#!/usr/bin/python3
"""
Script to send post request to passed url with email and display
body as response
"""
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.post(argv[1], {'email': argv[2]}).text
    print(response)
