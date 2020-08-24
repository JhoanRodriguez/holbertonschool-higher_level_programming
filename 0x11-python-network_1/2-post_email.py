#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response
"""

from sys import argv
import urllib.request as urlreq
from urllib.parse import urlencode


if __name__ == '__main__':
    url = argv[1]
    data = urlencode({'email': argv[2]})
    data = data.encode('ascii')

    with urlreq.urlopen(url, data) as response:
        print(response.read().decode())
