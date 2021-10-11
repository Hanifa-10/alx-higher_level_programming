#!/usr/bin/python3
"""Mylist"""

class Mylist(list):
    """Print a sorted list
    Arguments:
    list {[list]}
    """
    def print_sorted(self):
        print(sorted(self))
