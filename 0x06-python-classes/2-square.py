#!/usr/bin/python3
"""my module is for defining a class Square"""


class Square:
    """Defining a square"""
    def __init__(self, size=0):
        """Initialising the data"""
        self.__size = size
        """size is a private attribute of the class Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        """if size is less than 0, raise a ValueError exception"""
        if size < 0:
            """size must be >= 0"""
            raise ValueError("size must be >= 0")
