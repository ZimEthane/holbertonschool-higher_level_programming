# Python - Inheritance

Apprentissage de l'héritage et de la programmation orient\u00e9e objet avanc\u00e9e.

---

## Table des mati\u00e8res

1. [À propos](#à-propos)
2. [Concepts \u00e9tudi\u00e9s](#concepts-\u00e9tudi\u00e9s)
3. [H\u00e9ritage de base](#h\u00e9ritage-de-base)
4. [M\u00e9thodes et attributs h\u00e9rit\u00e9s](#m\u00e9thodes-et-attributs-h\u00e9rit\u00e9s)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

L'h\u00e9ritage permet de cr\u00e9er une hi\u00e9rarchie de classes et de r\u00e9utiliser du code. Ce dossier couvre les bases de l'h\u00e9ritage en Python.

---

## Concepts \u00e9tudi\u00e9s

- Classe parente et classe enfant
- H\u00e9ritage simple
- M\u00e9thode `super()`
- Red\u00e9finition de m\u00e9thodes (override)
- Appel des m\u00e9thodes parentes
- Attributs h\u00e9rit\u00e9s
- V\u00e9rification d'h\u00e9ritage
- H\u00e9ritage multiple

---

## H\u00e9ritage de base

### Syntaxe simple

```python
# Classe parente
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} fait du bruit")

# Classe enfant
class Dog(Animal):
    def speak(self):
        print(f"{self.name} aboie")

# Utilisation
dog = Dog("Rex")
dog.speak()  # "Rex aboie"
```

### Appeler la m\u00e9thode parente avec `super()`

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)  # Appeler le constructeur parent
        self.race = race

dog = Dog("Rex", 5, "Labrador")
print(dog.name)   # "Rex"
print(dog.age)    # 5
print(dog.race)   # "Labrador"
```

---

## M\u00e9thodes et attributs h\u00e9rit\u00e9s

### Acc\u00e9der aux m\u00e9thodes parent

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        return f"V\u00e9hicule de marque {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def describe(self):
        parent_desc = super().describe()
        return f"{parent_desc} avec {self.doors} portes"

car = Car("Toyota", 4)
print(car.describe())  # "V\u00e9hicule de marque Toyota avec 4 portes"
```

### V\u00e9rifier l'h\u00e9ritage

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# V\u00e9rifier si dog est une instance de Dog
print(isinstance(dog, Dog))      # True

# V\u00e9rifier l'h\u00e9ritage
print(isinstance(dog, Animal))   # True

# V\u00e9rifier la classe parente
print(issubclass(Dog, Animal))   # True
```

---

## H\u00e9ritage multiple

```python
class Flyer:
    def fly(self):
        print("Je vole")

class Swimmer:
    def swim(self):
        print("Je nage")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Coin coin")

duck = Duck()
duck.fly()     # "Je vole"
duck.swim()    # "Je nage"
duck.quack()   # "Coin coin"
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | lookup.py | Explorer les attributs d'un objet |
| 1 | my_list.py | Cr\u00e9er une classe h\u00e9ritant de list |
| 2 | is_same_class.py | V\u00e9rifier la classe d'un objet |
| 3 | is_kind_of_class.py | V\u00e9rifier l'h\u00e9ritage |
| 4 | only_sub_class_of.py | V\u00e9rifier si c'est une sous-classe |
| 5 | geometry.py | Cr\u00e9er une classe de base |
| 6 | rectangle.py | H\u00e9riter d'une classe |
| 7 | full_rectangle.py | Implémenter str et repr |
| 8 | square.py | H\u00e9ritage en cascade |
| 9 | square.py | Ajouter des m\u00e9thodes |
| 10 | square.py | Ignorer des attributs privés |

---

## Points importants

- L'h\u00e9ritage favorise la r\u00e9utilisation de code
- Utilisez `super()` pour appeler les m\u00e9thodes parent
- Vous pouvez red\u00e9finir les m\u00e9thodes parent
- V\u00e9rifiez l'h\u00e9ritage avec `isinstance()` et `issubclass()`
- L'h\u00e9ritage multiple existe mais doit être utilis\u00e9 avec prudence
- L'attribut `__bases__` liste les classes parentes

---

## Conseils pour bien apprendre

- Comprenez la hi\u00e9rarchie des classes
- Utilisez `super()` plutôt que de r\u00e9p\u00e9ter le code parent
- Testez les m\u00e9thodes h\u00e9rit\u00e9es
- Explorez `dir()` pour voir les attributs h\u00e9rit\u00e9s
- Pratiquez la conception d'hi\u00e9rarchies logiques

---

## Bon apprentissage !