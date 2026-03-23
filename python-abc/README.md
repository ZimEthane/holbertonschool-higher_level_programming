# Python - ABC (Abstract Base Classes)

Apprentissage des classes abstraites et des interfaces en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Classes abstraites](#classes-abstraites)
4. [Héritage abstrait](#héritage-abstrait)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Les classes abstraites permettent de définir une interface fixe que les sous-classes doivent implémenter. Essentielles pour la conception d'architectures robustes et maintenables.

---

## Concepts étudiés

- Module `abc` (Abstract Base Class)
- Décorateur `@abstractmethod`
- Décorateur `@abstractproperty`
- Classes abstraites vs concrètes
- Interfaces en Python
- Force l'implémentation des méthodes
- Polymorphisme abstrait

---

## Classes abstraites

### Syntaxe de base

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """Classe abstraite pour les animaux"""

    @abstractmethod
    def speak(self):
        """Chaque animal doit pouvoir parler"""
        pass

    @abstractmethod
    def move(self):
        """Chaque animal doit pouvoir se déplacer"""
        pass

    def describe(self):
        """Méthode concrète"""
        return "Je suis un animal"

# Ne pas instantier directement
# animal = Animal()  # TypeError !
```

### Implémentation concrète

```python
class Dog(Animal):
    def speak(self):
        return "Woof !"

    def move(self):
        return "Je cours"

class Bird(Animal):
    def speak(self):
        return "Tweet !"

    def move(self):
        return "Je vole"

# Maintenant on peut instantier
dog = Dog()
print(dog.speak())  # "Woof !"

bird = Bird()
print(bird.speak())  # "Tweet !"
```

---

## Propriétés abstraites

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        """Surface de la forme"""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """Périmètre de la forme"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(circle.area)       # ~78.5
print(circle.perimeter)  # ~31.4
```

---

## Héritage abstrait

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starts"

class SportsCar(Car):
    """Sous-classe concrète"""
    def start(self):
        return "High-performance engine roars to life"

# OK
sports_car = SportsCar()

# ERROR : Vehicle est abstraite
# vehicle = Vehicle()
```

---

## Points importants sur l'ABC

```python
from abc import ABC, abstractmethod

class FileProcessor(ABC):
    @abstractmethod
    def process(self, filename):
        """Traiter un fichier"""
        pass

    @abstractmethod
    def validate(self, data):
        """Valider les données"""
        pass

    def log_error(self, msg):
        """Méthode concrète"""
        print(f"ERROR: {msg}")

# Une sous-classe doit implémenter toutes les méthodes abstraites
class CSVProcessor(FileProcessor):
    def process(self, filename):
        return f"Processing CSV: {filename}"

    def validate(self, data):
        return isinstance(data, list)

# OK
processor = CSVProcessor()

# ERROR : JSONProcessor n'implémente pas validate()
# class JSONProcessor(FileProcessor):
#     def process(self, filename):
#         pass
#     # Oups ! validate() manquante
```

---

## Vérifier si une classe est abstraite

```python
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def method(self):
        pass

class Concrete(Abstract):
    def method(self):
        pass

# Vérifier les méthodes abstraites
print(Abstract.__abstractmethods__)  # frozenset({'method'})
print(Concrete.__abstractmethods__)  # frozenset()
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | abc.py | Classes abstraites basiques |
| 1 | duck_typing.py | Polymorphisme sans ABC |
| 2 | verboselist.py | Sous-classe de list |
| 3 | counted_iterator.py | Itérateur abstrait |

---

## Points importants

- Les classes abstraites ne peuvent pas être instantiées
- Les sous-classes doivent implémenter toutes les méthodes abstraites
- Les propriétés peuvent être abstraites
- ABC force un contrat entre les classes
- Utile pour définir une API publique
- Favorise le polymorphisme et la réutilisation de code

---

## Conseils pour bien apprendre

- Comprenez le rôle des interfaces
- Pratiquez la création de hiérarchies abstraites
- Testez les erreurs d'instantiation
- Explorez la vérification des méthodes abstraites
- Utilisez ABC pour améliorer votre architecture

---

## Bon apprentissage !
