#!/usr/bin/python3
"""
In this module we write a script that takes in a URL and
sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""

import urllib.request
import sys
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except HTTPError as error:
        print("Error code: {}".format(error.status))
