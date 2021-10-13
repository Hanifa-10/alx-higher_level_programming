#!/usr/bin/python3
"""write a file"""

def write_file(filename="", text=""):
    """Write a file

    Arguments:
    filename {str} -- name of the file to be written (default: {""})
    text {str} -- text to be written (default: {""})

    Returns:
    int -- number of char written
    """
    with open(filename, "w", encoding="UTF-8") as Myfile:
        return Myfile.write(str(text))
