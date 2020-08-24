#!/usr/bin/python3
"""
Script that takes in a URL, sends a request
to the URL and displays the body of the response
"""

import urllib.request as urlreq
from sys import argv
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlreq.urlopen(url) as response:
            print(response.read().decode())
    except URLError as error:
        print("Error code: {}".format(error.code))
