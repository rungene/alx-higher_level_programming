#!/usr/bin/python3
"""
In this module we write a script that takes in a URL and
an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    pay_load = {'email': email}
    response = requests.post(url, data=pay_load)
    print(response.text)
