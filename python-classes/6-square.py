#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes,
including validation, area calculation, and a method to print the square.
"""


class Square:
    """
    Represents a square with size and position attributes.
    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of
            2 positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(num, int) for num in position) or \
           not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: Retrieves the size of the square."""
        return self.__size

    @property
    def position(self):
        """tuple: Retrieves the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters considering its position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
    pass
