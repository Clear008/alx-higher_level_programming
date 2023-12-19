#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        temp = fct(*args)
        return temp
    except Exception as u:
        print("Exception: ()".format(u), file=stderr)
        return None
