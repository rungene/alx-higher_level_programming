#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    r = requests.get(url)
    content = r.text
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(content), content))
