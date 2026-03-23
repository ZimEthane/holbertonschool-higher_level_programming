# Python - Data Structures

Apprentissage des structures de données fondamentales en Python : listes et tuples.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Liste des exercices](#liste-des-exercices)
4. [Listes vs Tuples](#listes-vs-tuples)

---

## À propos

Les structures de données sont essentielles pour stocker et organiser les données. Ce dossier couvre les deux structures les plus fondamentales : les listes (modifiables) et les tuples (immuables).

---

## Concepts étudiés

### Listes
- Créer et initialiser les listes
- Accéder aux éléments (indexation)
- Ajouter et supprimer des éléments
- Parcourir les listes (boucles)
- Méthodes de liste (`append()`, `remove()`, `pop()`, etc.)
- Slicing (découpage)

### Tuples
- Créer et initialiser les tuples
- Immuabilité (pas de modification)
- Avantages par rapport aux listes
- Déballage de tuples
- Tuples comme clés de dictionnaire

---

## Liste des exercices

| # | Titre | Description |
|---|---|---|
| 0 | print_list_integer.py | Afficher les éléments d'une liste d'entiers |
| 1 | element_at.py | Accéder à un élément à un index donné |
| 2 | replace_in_list.py | Remplacer un élément dans une liste |
| 3 | print_reversed_list_integer.py | Afficher une liste en ordre inverse |
| 4 | new_in_list.py | Créer une nouvelle liste modifiée |
| 5 | no_c.py | Filtrer les éléments contenant 'c' |
| 6 | print_matrix_integer.py | Afficher une matrice (liste de listes) |
| 7 | tuples_on_the_same_line.py | Travailler avec les tuples |
| 8 | more_returns.py | Retourner plusieurs valeurs avec un tuple |
| 9 | more_string.py | Convertir une chaîne en liste |
| 10 | divisible_by_2.py | Filtrer les nombres divisibles par 2 |
| 11 | delete_at.py | Supprimer un élément à un index |
| 12 | switch.py | Inverser deux variables |

---

## Listes vs Tuples

### Listes (modifiables)

```python
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # Modification possible
my_list.append(6)  # Ajout possible
```

**Avantages :**
- Flexibles et modifiables
- Beaucoup de méthodes utiles
- Idéales pour les données qui changent

### Tuples (immuables)

```python
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # ERREUR !
# Les tuples ne peuvent pas être modifiés
```

**Avantages :**
- Plus rapides que les listes
- Peuvent être utilisés comme clés
- Plus sûrs (pas de modification accidentelle)

---

## Opérations courantes

### Créer une liste

```python
fruits = ["pomme", "banane", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "texte", 3.14, True]
```

### Accéder aux éléments

```python
fruits = ["pomme", "banane", "orange"]
print(fruits[0])    # "pomme"
print(fruits[-1])   # "orange" (dernier élément)
```

### Modifier une liste

```python
fruits = ["pomme", "banane"]
fruits.append("orange")  # Ajouter
fruits.remove("pomme")   # Supprimer
fruits[0] = "ananas"     # Modifier
```

### Boucler sur une liste

```python
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

### Créer un tuple

```python
my_tuple = (1, 2, 3)
single_element = (1,)  # Important : virgule obligatoire
```

---

## Points importants

- Les listes utilisent des crochets `[]` ; les tuples utilisent des parenthèses `()`
- L'indexation commence à 0
- L'indexation négative accède aux éléments en partant de la fin
- Le slicing `list[start:end:step]` crée une nouvelle liste
- Les tuples sont plus efficaces pour les données immuables
- Une liste peut contenir différents types de données

---

## Conseils pour bien apprendre

- Testez chaque opération dans la console Python
- Comprenez quand utiliser les listes et les tuples
- Maîtrisez le slicing, c'est très utile
- Utilisez des boucles pour parcourir les structures
- Consultez la documentation des méthodes de liste

---

## Bon apprentissage !
