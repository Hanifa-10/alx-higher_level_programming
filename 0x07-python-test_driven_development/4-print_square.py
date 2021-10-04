#!/usr/bin/python3
"""print_square module"""

def print_square(size):
    """Prints square with #

    Arguments:
    size {[int]} -- size of the square

    Raises:
    TypeError: size must be an integer
    ValueError: size must be >= 0"
    """
    x = 0
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    while (x < size):
        print("#" * size)
        x += 1
