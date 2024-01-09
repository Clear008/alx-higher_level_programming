#!/usr/bin/python3
"""Defines a function that open and reads a file  ."""


def read_file(filename=""):
    """Read a text file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
