#!/usr/bin/python3
"""Takes in a URL and an email address,
    sends a POST request to the passed URL
"""

import sys
import requests
if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
