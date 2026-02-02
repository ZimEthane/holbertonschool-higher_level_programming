#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.
    """

    def __init__(self, size):
        """
        Initialise un carré avec size privé.
        Valide que size est un entier strictement positif.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Retourne l'aire du carré.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Retourne la description du carré :
        [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
