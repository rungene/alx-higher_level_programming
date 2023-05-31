#!/usr/bin/python3
"""
In this module we write a script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'

    payload = {'q': q}
    r = requests.post(url, payload)

    try:
        json_response = r.json()
        if json_response:
            print('[{}] {}'.format(json_response.get('id'),
                  json_response.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
