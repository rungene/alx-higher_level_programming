#!/usr/bin/python3
"""
In this module we write a script that takes in a URL and
an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    body_data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    http_req = urllib.request.Request(url, body_data)

    with urllib.request.urlopen(http_req) as response:
        html = response.read().decode('utf-8')
        print(html)
