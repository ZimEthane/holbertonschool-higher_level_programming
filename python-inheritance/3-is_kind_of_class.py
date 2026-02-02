#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Retourne True si obj est une instance de a_class
    ou d'une classe qui hérite de a_class, sinon False.
    """
    return isinstance(obj, a_class)
