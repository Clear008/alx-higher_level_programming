#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        n = 0
        roman_a = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(roman_string)):
            if i > 0 and roman_a[roman_string[i]] > roman_a[roman_string[i - 1]]:
                n += roman_a[roman_string[i]] - 2 * roman_a[roman_string[i - 1]]
            else:
                n += roman_a[roman_string[i]]
        return n
