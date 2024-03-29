#!/usr/bin/python3
"""Takes in GitHub credentials (username and password) and uses the GitHub API
to display an id"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <password>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        print(user_info.get('id'))
    else:
        print('None')
