#!/usr/bin/python3

"""Docstring pour python-classes.4-square
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
    Includes a method to calculate the area of the square.
    """

    @property
    def size(self):
        return self.__size
    """
    Docstring pour size
    Getter method to retrieve the size of the square.
    """

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    Docstring pour size
    Setter method to set the size of the square with validation.
    """

    def area(self):
        return self.__size * self.__size
    """
    Docstring pour area
    Calculates and returns the area of the square.
    """

    pass
