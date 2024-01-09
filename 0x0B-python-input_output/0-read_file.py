#!/usr/bin/python3
"""Defines a function that open and reads a file  ."""


def read_file(filename=""):
    """Read a text file."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)