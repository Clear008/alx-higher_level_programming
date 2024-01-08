#!/usr/bin/python3
"""defines an inherits Mylist from list """


class Mylist(list):
    """class with only one attribute"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
