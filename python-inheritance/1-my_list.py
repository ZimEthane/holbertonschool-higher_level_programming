#!/usr/bin/python3
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
