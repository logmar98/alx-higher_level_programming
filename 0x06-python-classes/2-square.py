#!/usr/bin/python3
"""this our class Square."""


class Square:
    """it just a class that skip Square."""
    def __init__(self, size=0):
        """make new square

        Args:
            size (int): is a size
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

