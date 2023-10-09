#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """subclass list"""
    def __init__(self):
        """initializes object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
