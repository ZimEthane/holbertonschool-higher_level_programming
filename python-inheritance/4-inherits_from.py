#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Retourne True si obj est une instance d'une classe
    qui hérite (directement ou indirectement) de a_class,
    mais n'est PAS une instance directe de a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
