#!/usr/bin/python3
"""Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square."""

    def __init__(self, size):
        """new square.

        Args:
            size (int): The size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size