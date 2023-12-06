#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        n = 0
        ra = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(roman_string)):
            if i > 0 and ra[roman_string[i]] > ra[roman_string[i - 1]]:
                n += ra[roman_string[i]] - 2 * ra[roman_string[i - 1]]
            else:
                n += ra[roman_string[i]]
        return n
