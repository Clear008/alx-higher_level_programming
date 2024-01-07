#!/usr/bin/python3
"""Integer addition function."""

def add_integer(a, b=98):
	
    """
    Adds two integers a and b.
    
    Parameters:
    - a first integer must be int or float
    - b second integer must be int or float
    Returns:
    - int: The sum of a and b.
    
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer") 
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
