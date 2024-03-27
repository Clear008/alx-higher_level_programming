#!/usr/bin/python3
""" defines a function that should  find a peak """


def find_peak(list_of_integers):
    """Finds a peak in list of integers"""

    if list_of_integers == []:
        return None

    high_idx = len(list_of_integers)
    if high_idx == 1:
        return list_of_integers[0]
    if high_idx == 2:
        return max(list_of_integers)

    low_idx = 0
    mid = ((high_idx - low_idx) // 2) + low_idx
    mid = int(mid)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
