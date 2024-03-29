#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response
"""

if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
