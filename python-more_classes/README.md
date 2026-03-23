# Python - More Classes

Approfondissement des classes Python : méthodes spéciales, opérateurs et concepts avancés.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Méthodes spéciales](#méthodes-spéciales)
4. [Opérateurs surchargés](#opérateurs-surchargés)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Ce dossier approfondit la programmation orientée objet avec les méthodes spéciales (dunder methods), la surcharge d'opérateurs et les concepts avancés des classes.

---

## Concepts étudiés

- Méthodes spéciales (`__init__`, `__str__`, `__repr__`, etc.)
- Surcharge d'opérateurs (`__add__`, `__sub__`, `__eq__`, etc.)
- Propriétés avec `@property`
- Méthodes statiques et de classe
- Composition d'objets
- Gestion des attributs privés
- Itérateurs avec `__iter__` et `__next__`
- Comparaison d'objets

---

## Méthodes spéciales

### `__str__` et `__repr__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} ans"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(str(person))   # "Alice, 30 ans"
print(repr(person))  # "Person('Alice', 30)"
```

### Autres méthodes spéciales

```python
class MyClass:
    def __len__(self):
        return 10

    def __contains__(self, item):
        return item in [1, 2, 3]

    def __getitem__(self, index):
        return index * 2

    def __setitem__(self, key, value):
        print(f"Set {key} to {value}")

obj = MyClass()
print(len(obj))         # 10
print(2 in obj)         # True
print(obj[5])           # 10
obj[3] = 9              # "Set 3 to 9"
```

---

## Opérateurs surchargés

### Arithmétiques

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
print(v1 - v2)     # Vector(-2, -2)
print(v1 * 2)      # Vector(2, 4)
```

### Comparaison

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 < p3)   # False
print(p3 < p1)   # True
```

---

## Propriétés

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("La largeur doit être positive")
        self._width = value

rect = Rectangle(10, 5)
print(rect.area)      # 50
rect.width = 20       # OK
# rect.width = -5     # Levera ValueError
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | rectangle.py | Classe Rectangle basique |
| 1 | rectangle.py | Ajouter String representation |
| 2 | rectangle.py | Implémenter Rectangle delete |
| 3 | rectangle.py | Ajouter la surface |
| 4 | rectangle.py | Détecter les carrés |
| 5 | rectangle.py | Augmenter et réduire |
| 6 | rectangle.py | Comparer les surfaces |
| 7 | rectangle.py | Découper les rectangles |
| 8 | rectangle.py | Optimiser les instances |
| 9 | rectangle.py | Ajouter les affichages |

---

## Points importants

- Les méthodes spéciales ` __method__` ont un rôle précis
- La surcharge d'opérateurs rend les classes plus intuitives
- Les propriétés contrôlent l'accès aux attributs
- Les méthodes de classe et statiques ont des usages spécifiques
- Toujours valider les données dans les setters

---

## Conseils pour bien apprendre

- Testez toutes les méthodes spéciales
- Comparez vos classes à celles des types intégrés
- Utilisez les propriétés pour valider les données
- Maîtrisez la surcharge d'opérateurs pour des classes intuitives
- Explorez `dir()` pour voir toutes les méthodes spéciales

---

## Bon apprentissage !