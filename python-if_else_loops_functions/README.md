# Python - If/Else/Loops/Functions

Apprentissage des concepts fondamentaux : conditions, boucles et fonctions.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Conditions (if/elif/else)](#conditions)
4. [Boucles (for/while)](#boucles)
5. [Fonctions](#fonctions)

---

## À propos

Ce dossier couvre les concepts essentiels de la programmation : faire des choix avec les conditions, répéter des actions avec les boucles, et réutiliser du code avec les fonctions.

---

## Concepts étudiés

- Opérateurs de comparaison (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Opérateurs logiques (`and`, `or`, `not`)
- Instructions conditionnelles (`if`, `elif`, `else`)
- Boucles `for` et `while`
- Définition et appel de fonctions
- Paramètres et valeurs de retour
- Prototypage de fonctions

---

## Conditions

### Syntaxe if/elif/else

```python
age = 15

if age < 13:
    print("Vous êtes un enfant")
elif age < 18:
    print("Vous êtes un adolescent")
else:
    print("Vous êtes un adulte")
```

### Opérateurs logiques

```python
# AND
if age > 18 and age < 65:
    print("En âge de travailler")

# OR
if temperature < 0 or temperature > 40:
    print("Température extrême")

# NOT
if not is_weekend:
    print("C'est un jour de semaine")
```

---

## Boucles

### Boucle for

```python
# Itérer sur une liste
for fruit in ["pomme", "banane", "orange"]:
    print(fruit)

# Itérer avec range()
for i in range(5):
    print(i)  # Affiche 0, 1, 2, 3, 4

# Itérer avec range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # Affiche 1, 3, 5, 7, 9
```

### Boucle while

```python
count = 0
while count < 5:
    print(count)
    count += 1

# break : sortir de la boucle
while True:
    user_input = input("Entrez 'quit' pour sortir : ")
    if user_input == "quit":
        break

# continue : passer à l'itération suivante
for i in range(10):
    if i % 2 == 0:
        continue  # Sauter les nombres pairs
    print(i)
```

---

## Fonctions

### Définir une fonction

```python
def greet(name):
    """Fonction qui salue quelqu'un"""
    return f"Bonjour {name}"

# Appeler la fonction
message = greet("Alice")
print(message)  # "Bonjour Alice"
```

### Fonction avec plusieurs paramètres

```python
def add(a, b):
    """Additionne deux nombres"""
    return a + b

result = add(5, 3)  # 8
```

### Fonction avec valeurs par défaut

```python
def power(base, exponent=2):
    """Élève un nombre à une puissance"""
    return base ** exponent

print(power(3))      # 9 (exponent=2 par défaut)
print(power(3, 3))   # 27
```

### Fonction qui retourne plusieurs valeurs

```python
def get_coordinates():
    """Retourne x et y"""
    return 10, 20

x, y = get_coordinates()
print(x, y)  # 10 20
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | positive_or_negative.py | Conditions if/else |
| 1 | last_digit.py | Modulo et conditions |
| 2 | fizzbuzz.py | Boucles et conditions combinées |
| ... | ... | ... |
| 10 | add.py | Fonctions simples |
| 11 | pow.py | Fonction de calcul |
| 12 | fizzbuzz.py | Fonction classique |

---

## Points importants

- Les blocs de code en Python sont délimités par l'indentation
- L'égalité se teste avec `==` (pas `=`)
- Les fonctions facilitent la réutilisation de code
- Utilisez des noms de fonction explicites
- Documentez vos fonctions avec des docstrings
- Les paramètres par défaut rendent les fonctions flexibles

---

## Conseils pour bien apprendre

- Testez chaque condition avec différentes valeurs
- Tracez mentalement l'exécution des boucles
- Écrivez des fonctions réutilisables
- Utilisez `print()` pour déboguer le flux d'exécution
- Pratiquez les boucles imbriquées
- Créez vos propres exercices

---

## Bon apprentissage !