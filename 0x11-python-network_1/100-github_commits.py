#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository name> <owner name>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rsp = requests.get(url)
    commits = rsp.json()
    try:
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
