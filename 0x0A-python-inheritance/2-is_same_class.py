#!/usr/bin/python3
"""Module that verify is an object of the spesific class """


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""

    if type(obj) == a_class:
        return True
    return False
