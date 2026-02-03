#!/usr/bin/python3
"""module docstring for python-inheritance.9-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle héritant de BaseGeometry.
    Width et height sont privés.
    """

    def __init__(self, width, height):
        """
        Initialise le rectangle avec width et height privés.
        Valide que ce sont des entiers strictement positifs.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne la description du rectangle au format :
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
