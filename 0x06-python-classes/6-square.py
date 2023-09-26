#!/usr/bin/python3
"""this our class Square."""


class Square:
    """it just a class that skip Square."""

    def __init__(self, size=0, position=(0, 0)):
        """make new square

        Args:
            size (int): is a size
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """set our position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """show area of from value"""
        return self.__size * self.__size

    def my_print(self):
        """print a square shap"""
        for e in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for p in range(0, self.__position[0]):
                print(" ", end="")
            for s in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
