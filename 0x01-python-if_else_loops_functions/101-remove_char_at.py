#!/usr/bin/python3
def remove_char(s, n):
    nw_s = ""
    for i, c in enumerate (s):
        if i != n:
            nw_s +=c
    return nw_s
