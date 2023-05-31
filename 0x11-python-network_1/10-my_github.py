#!/usr/bin/python3
"""
In this module we write a script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, password))

    if r.status_code == 200:
        json_response = r.json()
        if json_response:
            print('{}'.format(json_response.get('id')))
    else:
        print('None')
