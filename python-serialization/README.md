# Python - Serialization

Apprentissage de la sérialisation et désérialisation des données en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Formats de sérialisation](#formats-de-sérialisation)
4. [JSON vs Pickle vs CSV](#json-vs-pickle-vs-csv)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

La sérialisation convertit les objets Python en format de fichier et inversement. Essentielle pour sauvegarder et transférer les données.

---

## Concepts étudiés

- Sérialisation JSON
- Sérialisation Pickle (sécurité)
- Index de fichiers CSV
- Formats XML de base
- Conversion aller-retour
- Gestion des exceptions
- Sérialisation d'objets personnalisés
- Best practices de sécurité

---

## Formats de sérialisation

### JSON (JavaScript Object Notation)

```python
import json

# Dictionnaire Python
data = {
    "name": "Alice",
    "age": 30,
    "cities": ["Paris", "Lyon", "Marseille"],
    "active": True
}

# Convertir en JSON string
json_string = json.dumps(data)
print(json_string)

# Convertir en JSON et sauvegarder
with open("data.json", "w") as f:
    json.dump(data, f)

# Charger depuis JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)

# Convertir JSON string en Python
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
```

### Pickle (Python Object Serialization)

```python
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# Sérialiser avec pickle
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

# Désérialiser
with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)

print(loaded_person.name)  # "Alice"

# Attention : ne pas utiliser pickle avec des données non fiables !
# Pickle peut exécuter du code arbitraire
```

### CSV (Comma-Separated Values)

```python
import csv

# Écrire un CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "Paris"],
    ["Bob", 25, "Lyon"],
    ["Charlie", 35, "Marseille"]
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Lire un CSV
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### XML (eXtensible Markup Language)

```python
import xml.etree.ElementTree as ET

# Créer un arbre XML
root = ET.Element("people")

person1 = ET.SubElement(root, "person")
ET.SubElement(person1, "name").text = "Alice"
ET.SubElement(person1, "age").text = "30"

# Sauvegarder
tree = ET.ElementTree(root)
tree.write("people.xml")

# Charger et lire
tree = ET.parse("people.xml")
root = tree.getroot()
for person in root.findall("person"):
    name = person.find("name").text
    age = person.find("age").text
    print(f"{name}: {age}")
```

---

## JSON vs Pickle vs CSV

| Format | Type de données | Lisible | Sécurité | Utilisation |
|---|---|---|---|---|
| JSON | Structures simples | Oui | Sûr | APIs, configuration |
| Pickle | Objets Python | Non | Dangereux | Caching interne |
| CSV | Données tabulaires | Oui | Sûr | Spreadsheets, rapports |
| XML | Structures hiérarchiques | Oui | Sûr | Configurationen |

---

## Sérialisation personnalisée

```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Créer un encoder personnalisé
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)

person = Person("Alice", 30)
json_string = json.dumps(person, cls=PersonEncoder)
print(json_string)  # {"name": "Alice", "age": 30}
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | basic_serialization.py | JSON dump/load |
| 1 | pickle.py | Pickle dump/load |
| 2 | csv.py | Lecture/écriture CSV |
| 3 | xml.py | Manipulation XML |

---

## Points importants

- JSON est lisible et sûr, préféré pour les APIs
- Pickle est rapide mais ne sérialise que les objets Python
- Pickle n'est jamais fiable avec des données non fiables
- CSV est parfait pour les données tabulaires
- Toujours spécifier l'encodage (UTF-8 par défaut)
- Gérer les exceptions lors de la désérialisation

---

## Conseils pour bien apprendre

- Testez chaque format avec vos données
- Comprenez les limitations de chaque format
- Pratiquez l'aller-retour (sérialisation + désérialisation)
- Explorez le pretty-printing pour les formats texte
- Créez des encoders personnalisés pour vos classes

---

## Bon apprentissage !
