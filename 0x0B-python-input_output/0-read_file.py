#!/usr/bin/python3
"""read file function"""


def read_file(filename=""):
    """A function that reads a text file and prints it to stdout
    """

    with open(filename, encoding="UTF-8") as MyFile:
        for line in MyFile:
            print(line, end="")
