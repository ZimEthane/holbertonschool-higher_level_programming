# Python - More Data Structures

Apprentissage des structures de données avancées : ensembles (sets) et dictionnaires.

---

## Table des matières

1. [À propos](#à-propos)
2. [Dictionnaires](#dictionnaires)
3. [Ensembles (Sets)](#ensembles-sets)
4. [Opérations sur les structures](#opérations-sur-les-structures)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Les dictionnaires et ensembles sont des structures essentielles pourstockeret accéder efficacement aux données. Ce dossier couvre leur utilisation, leurs méthodes et leurs opérations.

---

## Dictionnaires

### Créer un dictionnaire

```python
# Dictionnaire vide
my_dict = {}

# Dictionnaire avec données
person = {"name": "Alice", "age": 30, "city": "Paris"}

# Créer avec dict()
my_dict = dict(name="Alice", age=30)
```

### Accéder aux valeurs

```python
person = {"name": "Alice", "age": 30}

# Accès direct
print(person["name"])      # "Alice"

# Accès sûr avec get()
print(person.get("age"))    # 30
print(person.get("phone"))  # None (pas d'erreur)
```

### Modifier un dictionnaire

```python
person = {"name": "Alice"}

# Ajouter une clé
person["age"] = 30

# Modifier une valeur
person["name"] = "Bob"

# Supprimer une clé
del person["age"]

# Supprimer et retourner une valeur
age = person.pop("age", 0)  # 0 si la clé n'existe pas
```

### Parcourir un dictionnaire

```python
person = {"name": "Alice", "age": 30, "city": "Paris"}

# Parcourir les clés
for key in person:
    print(key)

# Parcourir les clés explicitement
for key in person.keys():
    print(key)

# Parcourir les valeurs
for value in person.values():
    print(value)

# Parcourir les paires clé-valeur
for key, value in person.items():
    print(f"{key}: {value}")
```

### Méthodes utiles

```python
person = {"name": "Alice", "age": 30}

# Vérifier l'existence
"name" in person  # True

# Obtenir toutes les clés/valeurs
keys = person.keys()
values = person.values()

# Fusionner deux dictionnaires
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = {**dict1, **dict2}  # {"a": 1, "b": 2}

# Effacer le dictionnaire
person.clear()
```

---

## Ensembles (Sets)

### Créer un ensemble

```python
# Ensemble vide
my_set = set()

# Ensemble avec valeurs
numbers = {1, 2, 3, 4, 5}

# Créer à partir d'une liste
unique_numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

### Opérations sur les ensembles

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)           # {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)           # {3}

# Différence
print(set1 - set2)           # {1, 2}

# Différence symétrique
print(set1 ^ set2)           # {1, 2, 4, 5}
```

### Modifier un ensemble

```python
numbers = {1, 2, 3}

# Ajouter
numbers.add(4)               # {1, 2, 3, 4}

# Supprimer
numbers.remove(3)            # {1, 2, 4}

# Supprimer sans erreur
numbers.discard(99)          # Pas d'erreur

# Dépiler
numbers.pop()                # Retire un élément aléatoire

# Effacer
numbers.clear()              # {}
```

### Vérifier l'appartenance

```python
numbers = {1, 2, 3, 4, 5}

# Vérifier un élément
2 in numbers              # True

# Sous-ensemble
{1, 2} < numbers          # True (sous-ensemble strict)
{1, 2} <= numbers         # True (sous-ensemble)

# Sur-ensemble
{1, 2, 3, 4, 5} >= numbers  # True (sur-ensemble)
```

---

## Opérations sur les structures

### Compréhension de dictionnaire

```python
# Créer un dictionnaire à partir d'une liste
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtrer un dictionnaire
evens = {k: v for k, v in squares.items() if v % 2 == 0}
```

### Compréhension d'ensemble

```python
# Créer un ensemble
numbers = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | square_matrix_simple.py | Matrice et boucles |
| 1 | search_replace.py | Modifier les listes |
| 2 | uniq_add.py | Ajouter les éléments uniques |
| 3 | common_elements.py | Trouver les éléments communs |
| 4 | only_diff_elements.py | Différence entre ensembles |
| 5 | number_keys.py | Travailler avec les dictionnaires |
| 6 | print_sorted_dictionary.py | Trier les dictionnaires |
| ... | ... | ... |
| 12 | roman_to_int.py | Convertir romain en entier |

---

## Points importants

- Les dictionnaires sont mutables et ordonnés (Python 3.7+)
- Les ensembles contiennent seules valeurs uniques
- Les dictionnaires utilisent les clés hashables
- Les ensembles sont optimisés pour tester l'appartenance
- Utilisez get() pour un accès sûr aux dictionnaires
- Les compréhensions créent des structures élégamment

---

## Conseils pour bien apprendre

- Testez les opérations sur les ensembles
- Comprenez quand utiliser dictionnaire vs ensemble
- Maîtrisez les compréhensions
- Explorez les méthodes disponibles
- Pratiquez l'itération sur ces structures
- Utilisez ces structures pour résoudre des problèmes réels

---

## Bon apprentissage !
