#!/usr/bin/python3
"""Python script that fetches a URL"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
