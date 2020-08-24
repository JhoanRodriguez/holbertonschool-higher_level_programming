#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""

from sys import argv
import urllib.request as urlreq

if __name__ == '__main__':
    with urlreq.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
