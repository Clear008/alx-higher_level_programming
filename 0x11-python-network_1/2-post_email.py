#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
