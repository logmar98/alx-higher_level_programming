#!/usr/bin/python3
"""this our class Square."""


class Square:
    """it just a class that skip Square."""
    def __init__(self, size=0):
        """make new square

        Args:
            size (int): is a size
        """
        self.size = size

    @property
    def size(self):
        """set our size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """show area of from value"""
        return self.__size * self.__size
