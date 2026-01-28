#!/usr/bin/python3
"""
Module that defines a Rectangle class with width and height attributes.
"""


class Rectangle:
    """
    A Rectangle class that defines width and height with validation.
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.
        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    pass
