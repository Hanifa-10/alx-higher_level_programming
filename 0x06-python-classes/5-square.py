#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Class Square
        Keyword Arguments:
            size {int} -- size of square(default: {0})
        Raises:
            ValueError: must be > 0
            TypeError: must be an int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area
        Returns:
            [int] -- area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
