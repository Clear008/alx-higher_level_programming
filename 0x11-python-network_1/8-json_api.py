#!/usr/bin/python3
"""Makes a POST request to http://0.0.0.0:5000/search_user."""

import requests
from sys import argv

if __name__ == "__main__":
    query = "" if len(argv) == 1 else argv[1]
    rt = requests.post('http://0.0.0.0:5000/search_user', data={'q': query})
    try:
        res = rt.json()
        if res == {}:
            print('No result')
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
