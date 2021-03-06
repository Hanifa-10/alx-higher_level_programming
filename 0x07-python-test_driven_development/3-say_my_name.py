#!/usr/bin/python3
"""Say_my_name"""



def say_my_name(first_name, last_name=""):
    """prints full name
    Arguments:
    first_name {[str]} -- First name

    Keyword arguments:
    last_name {str} -- Last name (default: {""})

    Raises:
    TypeError: first_name must be a string
    TypeError: last_name must be a string
    """
    if not isinstance(first_name, (str)) or first_name is None:
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
