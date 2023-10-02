#!/usr/bin/python3
"""sum of int."""


def add_integer(a, b=98):
    """Return the sum of int

    Raises:
        TypeError: If a or b is non int or flaot
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
