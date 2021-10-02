#!/usr/bin/python3
"""
This is 0-add_integer module supplied with one function, add_integer(a, b)
"""

def add_integer(a, b):
    """Return the sum of two integer numbers"""
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
