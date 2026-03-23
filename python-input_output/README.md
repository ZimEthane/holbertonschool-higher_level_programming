# Python - Input/Output

Apprentissage de la manipulation de fichiers et de l'entrée/sortie en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Lire et écrire des fichiers](#lire-et-écrire-des-fichiers)
4. [Formats de données](#formats-de-données)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Ce dossier couvre la manipulation des fichiers : lire, écrire, analyser et sérialiser des données. Essentiels pour tout programme qui doit persister des données.

---

## Concepts étudiés

- Ouvrir et fermer des fichiers
- Modes d'ouverture (lecture, écriture, ajout)
- Lire le contenu d'un fichier
- Écrire dans un fichier
- Gérer le contexte avec `with`
- Lire ligne par ligne
- Gérer les exceptions lors de la lecture
- Sérialisation JSON
- Parsing CSV

---

## Lire et écrire des fichiers

### Ouvrir un fichier

```python
# Mode lecture
file = open("data.txt", "r")

# Mode écriture (créer ou remplacer)
file = open("output.txt", "w")

# Mode ajout (ajouter à la fin)
file = open("log.txt", "a")

file.close()
```

### Utiliser `with` (recommandé)

```python
# Le fichier se ferme automatiquement
with open("data.txt", "r") as file:
    content = file.read()
    # Pas besoin de file.close()
```

### Lire un fichier

```python
with open("data.txt", "r") as file:
    # Lire tout le contenu
    content = file.read()

    # Lire ligne par ligne
    for line in file:
        print(line)

    # Lire toutes les lignes dans une liste
    lines = file.readlines()
```

### Écrire dans un fichier

```python
# Écrire du texte
with open("output.txt", "w") as file:
    file.write("Bonjour le monde\n")
    file.write("Deuxième ligne\n")

# Écrire plusieurs lignes
with open("output.txt", "w") as file:
    lines = ["Ligne 1\n", "Ligne 2\n", "Ligne 3\n"]
    file.writelines(lines)
```

---

## Formats de données

### JSON

```python
import json

# Écrire JSON
data = {"name": "Alice", "age": 30, "city": "Paris"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Lire JSON
with open("data.json", "r") as file:
    data = json.load(file)
```

### CSV

```python
import csv

# Écrire CSV
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
    writer.writerow(["Bob", 25])

# Lire CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## Gestion des erreurs

```python
try:
    with open("fichier.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Le fichier n'existe pas")
except IOError:
    print("Erreur de lecture/écriture")
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | read_file.py | Lire un fichier texte |
| 1 | write_file.py | Écrire dans un fichier |
| 2 | append_to_file.py | Ajouter du contenu |
| 3 | to_json_string.py | Convertir en JSON |
| 4 | from_json_string.py | Charger depuis JSON |
| 5 | save_to_json_file.py | Sauvegarder en JSON |
| 6 | load_from_json_file.py | Charger un fichier JSON |
| ... | ... | ... |
| 10 | student.py | Sérialiser une classe |
| 11 | student.py | Désérialiser une classe |
| 12 | pascal_triangle.py | Générer et sauvegarder des données |

---

## Points importants

- Toujours utiliser `with` pour ouvrir les fichiers
- Fermer les fichiers proprement évite les corruptions
- Gérer les exceptions lors de la manipulation de fichiers
- JSON permet de stocker des structures complexes
- CSV est idéal pour les données tabulaires
- Le chemin du fichier peut être absolu ou relatif

---

## Conseils pour bien apprendre

- Testez la lectureécriture de fichiers locaux
- Utilisez des fichiers de test pour vos expériences
- Vérifiez le contenu des fichiers après écriture
- Gérez les erreurs : fichier introuvable, permissions, etc.
- Comprenez les différentes modes d'ouverture
- Explorez JSON et CSV avec vos propres données

---

## Bon apprentissage !
