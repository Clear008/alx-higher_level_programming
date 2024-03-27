#!/usr/bin/python3
""" defines a function that should  find a peak """


def find_peak(list_of_integers):
    """Finds a peak in list of integers"""

    if list_of_integers == []:
        return None

    low_idx = 0
    high_idx = len(list_of_integers) - 1

    while low_idx < high_idx:
        mid = (low_idx + high_idx) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low_idx = mid + 1
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            high_idx = mid - 1
        else:
            return list_of_integers[mid]

    return list_of_integers[low_idx]
