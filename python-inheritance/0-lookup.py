#!/usr/bin/python3
"""module docstring for python-inheritance.0-lookup"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: n'importe quel objet Python

    Returns:
        list: liste des noms des attributs et méthodes de l'objet
    """
    return dir(obj)
