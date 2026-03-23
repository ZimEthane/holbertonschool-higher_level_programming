# Python - Classes

Introduction aux classes en Python et à la programmation orientée objet.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Liste des exercices](#liste-des-exercices)
4. [Comment exécuter les scripts](#comment-exécuter-les-scripts)

---

## À propos

Ce dossier contient des exercices progressifs sur les classes Python. Vous apprendrez à créer et utiliser des classes, des attributs et des méthodes pour structurer votre code.

---

## Concepts étudiés

- Création de classes
- Constructeur `__init__`
- Attributs d'instance
- Méthodes d'instance
- Attributs privés et publics
- Encapsulation
- Validation des données
- Représentation des objets avec `__str__` et `__repr__`

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | empty_square.py | Classe vide, syntaxe de base |
| 1 | square_size.py | Constructeur avec attribut |
| 2 | size_validation.py | Validation et levée d'exceptions |
| 3 | area.py | Calcul d'une propriété |
| 4 | full_square.py | Affichage avec caractères |

---

## Progression de complexité

Les exercices augmentent graduellement en complexité :

1. **Exercice 0** : Définir une classe vide
2. **Exercices 1-2** : Ajouter des attributs avec validation
3. **Exercice 3** : Implémenter des méthodes de calcul
4. **Exercice 4** : Afficher des représentations graphiques

---

## Syntaxe de base

### Créer une classe

```python
class Square:
    """Description de la classe"""

    def __init__(self, size):
        """Constructeur"""
        self.__size = size

    def area(self):
        """Calculer la surface"""
        return self.__size ** 2
```

### Utiliser une classe

```python
my_square = Square(5)
print(my_square.area())  # Affiche 25
```

---

## Points importants

- Las une classe doit décrire un concept
- Le constructeur `__init__` initialise les attributs
- Les attributs privés commencent par `__`
- Les méthodes modifient ou retournent les attributs
- Utilisez des getters et des setters pour contrôler l'accès

---

## Conseils pour bien apprendre

- Testez chaque exercice en créant des instances
- Modifiez les valeurs et observez les changements
- Utilisez `print()` pour déboguer
- Lisez les messages d'erreur attentivement
- Essayez de créer vos propres classes

---

## Bon apprentissage !
