#!/usr/bin/python3
"""
Docstring pour python-classes.4-square
Defines a Square class with a private instance attribute size.
The size attribute is initialized through the constructor
with a default value of 0.
The constructor raises exceptions for invalid size values.
Includes a method to calculate the area of the square.
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        return self.__position
    """
    Docstring pour position
    Getter method to retrieve the position of the square.
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

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """
    Docstring pour position
    Setter method to set the position of the square with validation.
    """

    def area(self):
        return self.__size * self.__size
    """
    Docstring pour area
    Calculates and returns the area of the square.
    """

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")

            for j in range(self.__size):
                print("#", end="")
        print()
    """
    Docstring pour my_print
    Prints the square using the '#' character.
    """

    pass
