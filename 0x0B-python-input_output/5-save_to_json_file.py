#!/usr/bin/python3
"""Defines a function that writes an Object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file JSON representation."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
