#!/usr/bin/python3
import urllib.request as urlreq
"""
Script that fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    with urlreq.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode(encoding="utf -8")))
