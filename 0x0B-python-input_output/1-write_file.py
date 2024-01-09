#!/usr/bin/python3
"""Defines a function that open and write to a testfile."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)."""
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(text)
        return content
