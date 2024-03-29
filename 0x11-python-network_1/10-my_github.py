#!/usr/bin/python3
"""akes your GitHub credentials (username and password) and uses
    the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
