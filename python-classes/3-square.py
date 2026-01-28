#!/usr/bin/python3

"""
Docstring pour python-classes.3-square
Defines a Square class with a private instance attribute size.
The size attribute is initialized through the constructor with a default value of 0.
The constructor raises exceptions for invalid size values.
Includes a method to calculate the area of the square.

"""


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    Docstring pour Square
    Defines a Square class with a private instance attribute size.
    The size attribute is initialized through the constructor
    with a default value of 0.
    The constructor raises exceptions for invalid size values.
    Includes a method to calculate the area of the square."""

    def area(self):
        return self.__size * self.__size
    """
    Docstring pour area
    Calculates and returns the area of the square.
    """
    pass
