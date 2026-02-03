#!/usr/bin/python3
"""module docstring for python-inheritance.8-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle héritant de BaseGeometry
    avec width et height privés.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur privées.
        Valide que ce sont des entiers strictement positifs.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
