#!/usr/bin/python3
""""
module 0-add_integer
This module contains a function that adds two integers.
The function checks for type errors and raises appropriate exceptions.

"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int/float): The first integer.
        b (int/float): The second integer (default is 98).

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
