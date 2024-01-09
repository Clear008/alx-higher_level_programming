#!/usr/bin/python3
"""a script that adds and save all arguments to a Python list """
import sys


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_and_save_to_file(arguments):
    try:

        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(arguments)
    save_to_json_file(existing_data, "add_item.json")


if __name__ == "__main__":
    add_and_save_to_file(arguments)
