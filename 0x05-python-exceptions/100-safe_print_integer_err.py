#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    _integer = True
    try:
        print("{:d}".format(value))
    except Exception as u:
        print("Exception:", u, file=stderr)
        return False
