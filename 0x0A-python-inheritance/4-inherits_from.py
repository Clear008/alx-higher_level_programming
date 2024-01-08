#!/usr/bin/python3
"""Module that verify is an object of the spesific class """


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
