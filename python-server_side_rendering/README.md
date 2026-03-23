# Python Server Side Rendering - Templates et Applications Flask

Un projet complet démontrant le rendu côté serveur (SSR) en Python avec Flask, Jinja2, et l'intégration de multiples sources de données (JSON, CSV, SQLite).

## Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Structure du projet](#structure-du-projet)
- [Tâches](#tâches)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemples d'URL](#exemples-durl)
- [Architecture](#architecture)

## Vue d'ensemble

Ce projet explore les concepts clés du rendu de templates côté serveur:
- Templating avec Jinja2
- Héritage et composition de templates
- Contenu dynamique avec boucles et conditions
- Intégration de multiples sources de données
- Gestion d'erreurs robuste

## Structure du projet

```
python-server_side_rendering/
├── README.md                  # Documentation
├── create_db.py             # Script d'initialisation BD
│
├── task_00_intro.py         # Tâche 0 : Templating simple
├── task_01_jinja.py         # Tâche 1 : Templates Flask
├── task_02_logic.py         # Tâche 2 : Boucles et conditions
├── task_03_files.py         # Tâche 3 : JSON et CSV
├── task_04_db.py            # Tâche 4 : SQLite ajouté
│
├── template.txt             # Template pour invitations
├── items.json               # Données items
├── products.json            # Données produits (JSON)
├── products.csv             # Données produits (CSV)
├── products.db              # Base de données SQLite
│
└── templates/               # Dossier des templates Flask
    ├── base.html            # Template de base (héritage)
    ├── header.html          # Header réutilisable
    ├── footer.html          # Footer réutilisable
    ├── index.html           # Page d'accueil
    ├── about.html           # Page À propos
    ├── contact.html         # Page Contact
    ├── items.html           # Liste items dynamique
    └── product_display.html # Affichage produits
```

## Tâches

### Tâche 0 : Templating Simple en Python

**Fichier**: `task_00_intro.py`

Création d'une fonction de templating qui génère des fichiers d'invitation personnalisés.

**Fonctionnalités**:
- Lecture de templates avec placeholders
- Remplacement de variables
- Gestion des données manquantes (N/A)
- Génération de fichiers séquentiels (output_1.txt, output_2.txt, etc.)

**Exécution**:
```bash
python3 main.py
```

**Exemple**:
```python
from task_00_intro import generate_invitations

template = "Hello {name}, You are invited to {event_title}..."
attendees = [
    {"name": "Alice", "event_title": "Python Conference", ...},
    {"name": "Bob", ...}
]

generate_invitations(template, attendees)
# Génère: output_1.txt, output_2.txt
```

---

### Tâche 1 : Templates Flask de Base

**Fichier**: `task_01_jinja.py`

Construction d'une application Flask avec templates Jinja et composants réutilisables.

**Fonctionnalités**:
- Héritage de template (base.html)
- Inclusion de composants (header, footer)
- 3 routes principales (/, /about, /contact)
- Blocs de contenu personnalisables

**Routes disponibles**:
```
GET /              → Page d'accueil
GET /about         → Page À propos
GET /contact       → Page Contact
```

**Structure template**:
```
base.html
├── header.html (navigation)
├── {% block content %}
└── footer.html
```

**Exécution**:
```bash
python3 task_01_jinja.py
# Visite: http://localhost:5000/
```

---

### Tâche 2 : Contenu Dynamique avec Boucles et Conditions

**Fichier**: `task_02_logic.py`

Rendu dynamique de contenu utilisant les boucles et conditions Jinja.

**Fonctionnalités**:
- Lecture de fichier JSON (`items.json`)
- Boucles Jinja (`{% for item in items %}`)
- Conditions (`{% if items %} ... {% else %}`)
- Affichage en liste HTML

**Routes**:
```
GET /items         → Affiche la liste des items
```

**Données JSON** (items.json):
```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

**Template** (templates/items.html):
```jinja
{% if items %}
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>No items found</p>
{% endif %}
```

**Exécution**:
```bash
python3 task_02_logic.py
# Visite: http://localhost:5000/items
```

---

### Tâche 3 : Affichage de Données JSON et CSV

**Fichier**: `task_03_files.py`

Intégration de multiples sources de données avec query parameters.

**Fonctionnalités**:
- Lecture JSON (`products.json`)
- Lecture CSV (`products.csv`)
- Query parameter `source` (json, csv, sql)
- Filtrage optionnel par `id`
- Affichage en tableau formaté
- Gestion complète des erreurs

**Routes**:
```
GET /products?source=json              → Tous les produits JSON
GET /products?source=json&id=1         → Produit ID=1 JSON
GET /products?source=csv               → Tous les produits CSV
GET /products?source=csv&id=2          → Produit ID=2 CSV
GET /products?source=invalid           → Erreur "Wrong source"
```

**Données** (products.json / products.csv):
```json
[
  {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
  {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
  {"id": 3, "name": "Python Book", "category": "Books", "price": 45.99},
  {"id": 4, "name": "Wireless Mouse", "category": "Electronics", "price": 29.99},
  {"id": 5, "name": "Desk Lamp", "category": "Home Goods", "price": 35.50}
]
```

**Format table**:
```
ID | Name             | Category       | Price
1  | Laptop           | Electronics    | $799.99
2  | Coffee Mug       | Home Goods     | $15.99
...
```

**Exécution**:
```bash
python3 task_03_files.py
# Visite: http://localhost:5000/products?source=json
```

---

### Tâche 4 : Intégration SQLite (NOUVEAU)

**Fichiers**: `task_04_db.py`, `create_db.py`

Extension du système pour supporter SQLite en tant que source de données.

**Fonctionnalités**:
- Base de données SQLite (`products.db`)
- Support du query parameter `source=sql`
- Même interface que JSON/CSV
- Gestion des erreurs de base de données
- Template réutilisable pour toutes les sources

**Routes**:
```
GET /products?source=sql               → Tous les produits SQLite
GET /products?source=sql&id=3          → Produit ID=3 SQLite
GET /products?source=invalid           → Erreur "Wrong source"
```

**Structure BD**:
```
Table: Products
┌─────┬──────────────────┬────────────────┬────────┐
│ id  │ name             │ category       │ price  │
├─────┼──────────────────┼────────────────┼────────┤
│ 1   │ Laptop           │ Electronics    │ 799.99 │
│ 2   │ Coffee Mug       │ Home Goods     │ 15.99  │
│ 3   │ Python Book      │ Books          │ 45.99  │
│ 4   │ Wireless Mouse   │ Electronics    │ 29.99  │
│ 5   │ Desk Lamp        │ Home Goods     │ 35.50  │
└─────┴──────────────────┴────────────────┴────────┘
```

**Initialisation BD**:
```bash
python3 create_db.py
# Crée products.db avec les données
```

**Exécution**:
```bash
python3 task_04_db.py
# Visite: http://localhost:5000/products?source=sql
```

## Installation

### Prérequis
- Python 3.7+
- Flask 3.0+

### Setup

```bash
# 1. Cloner le repository
git clone https://github.com/holbertonschool/holbertonschool-higher_level_programming.git
cd python-server_side_rendering

# 2. Installer les dépendances
pip install Flask

# 3. Créer la base de données SQLite
python3 create_db.py

# 4. Lancer l'application Flask
python3 task_04_db.py
```

## Utilisation

### Démarrer l'application complète

```bash
python3 task_04_db.py
```

L'application s'exécute sur `http://localhost:5000`

### Navigation

```
Accueil          http://localhost:5000/
À propos         http://localhost:5000/about
Contact          http://localhost:5000/contact
Items            http://localhost:5000/items
Produits         http://localhost:5000/products?source=json
```

## Exemples d'URL

### Sources de Données

```
# JSON
http://localhost:5000/products?source=json
http://localhost:5000/products?source=json&id=1

# CSV
http://localhost:5000/products?source=csv
http://localhost:5000/products?source=csv&id=3

# SQLite (NOUVEAU)
http://localhost:5000/products?source=sql
http://localhost:5000/products?source=sql&id=2
```

### Gestion des Erreurs

```
# Source invalide
http://localhost:5000/products?source=xml
→ Affiche: "Wrong source"

# Produit non trouvé
http://localhost:5000/products?source=json&id=999
→ Affiche: "Product not found"

# Format ID invalide
http://localhost:5000/products?source=sql&id=abc
→ Affiche: "Invalid product ID"
```

## Architecture

### Flux de traitement

```
Client Request
    ↓
Flask Route (/products)
    ↓
Query Parameters (source, id)
    ↓
Validation (source ∈ {json, csv, sql})
    ↓
Read Data Function
├─ read_json_products()
├─ read_csv_products()
└─ read_sqlite_products()   ← NOUVEAU
    ↓
Filter by ID (optional)
    ↓
Render Template (product_display.html)
    ↓
HTML Response
```

### Gestion des Erreurs

```
┌─────────────────────────────────┐
│   Erreurs Possibles             │
├─────────────────────────────────┤
│ • Source invalide               │
│   → "Wrong source"              │
│                                 │
│ • Données non trouvées          │
│   → "Product not found"         │
│                                 │
│ • Format ID invalide            │
│   → "Invalid product ID"        │
│                                 │
│ • Erreur de fichier/BD          │
│   → Message descriptif          │
└─────────────────────────────────┘
```

## Comparaison des Sources de Données

| Fonctionnalité | JSON | CSV | SQLite |
|---|---|---|---|
| Lecture rapide | Oui | Oui | Oui |
| Scalabilité | Limité | Limité | Excellente |
| Requêtes complexes | Non | Non | SQL |
| Indexation | Non | Non | Oui |
| ACID | Non | Non | Oui |

## Tests

### Vérifier que tout fonctionne

```bash
# Test Task 0
python3 main.py

# Test Task 1
python3 -c "from task_01_jinja import app; print('Task 1 OK')"

# Test Task 2
python3 -c "from task_02_logic import app; print('Task 2 OK')"

# Test Task 3
python3 -c "from task_03_files import app; print('Task 3 OK')"

# Test Task 4
python3 -c "from task_04_db import app; print('Task 4 OK')"
```

## Concepts Couverts

### Templating
- Héritage de templates
- Blocs de contenu
- Inclusion de composants
- Variables et filtres Jinja

### Flask
- Routes et query parameters
- Rendu de templates
- Gestion des erreurs
- HTTP status codes

### Sources de Données
- Lecture JSON
- Lecture CSV
- Requêtes SQLite
- Conversion de types

### Gestion d'Erreurs
- Validation des entrées
- Gestion des exceptions
- Messages d'erreur utilisateur
- Fallback gracieux

## Ressources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Template Designer](https://jinja.palletsprojects.com/templates/)
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [Python csv Module](https://docs.python.org/3/library/csv.html)

## Auteur

Projet éducatif - Holbertonschool Higher Level Programming

## Licence

MIT License

---

**Version**: 1.0
**Dernière mise à jour**: Mars 2026
**Statut**: Complet (4/4 tâches)