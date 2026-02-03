#!/usr/bin/python3
"""module docstring for python-inheritance.7-base_geometry"""


class BaseGeometry:
    """
    Classe BaseGeometry.
    """

    def area(self):
        """
        Lève une Exception indiquant que la méthode
        area() n'est pas implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que value est un entier strictement positif.

        Args:
            name (str): nom de la valeur
            value (int): valeur à valider

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
