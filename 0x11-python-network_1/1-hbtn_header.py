#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id
"""

import sys
import urllib.request

with urllib.request.urlopen('sys.argv[1]') as response:
    head = response.headers.get('X-Request-Id')
    print(head)
