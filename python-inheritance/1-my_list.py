#!/usr/bin/python3
"""module docstring for python-inheritance.1-my_list"""


class MyList(list):
    """
    Classe MyList qui hérite de la classe list.
    """

    def print_sorted(self):
        """
        Affiche la liste triée par ordre croissant
        sans modifier la liste originale.
        """
        print(sorted(self))
