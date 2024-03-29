#!/usr/bin/python3
"""akes in a letter and sends a POST request to http://0.0.0.0:5000/search_user."""

import requests
from sys import argv

if __name__ == "__main__":
    l = "" if len(sys.argv) == 1 else sys.argv[1]
    rt = requests.post('http://0.0.0.0:5000/search_user', data={'q': l})
    try:
        res = rt.json()
        if res == {}:
            print('No result')
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
