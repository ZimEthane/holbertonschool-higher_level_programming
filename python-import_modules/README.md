# Python - Import Modules

Apprentissage de l'utilisation des modules et du import en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Types d'importations](#types-dimportations)
4. [Liste des exercices](#liste-des-exercices)

---

## À propos

Les modules permettent de réutiliser du code et d'organiser son projet. Ce dossier couvre l'import de modules, la création de modules personnalisés et l'utilisation de modules intégrés.

---

## Concepts étudiés

- Importer des modules avec `import`
- Importer depuis des modules avec `from ... import`
- Importer tous les éléments avec `*`
- Aliasing avec `as`
- Créer vos propres modules
- Utiliser les modules intégrés (sys, math, etc.)
- Structure `if __name__ == "__main__"`
- Gestion des arguments de ligne de commande

---

## Types d'importations

### Import simple

```python
import math

result = math.sqrt(16)  # 4.0
```

### Import spécifique

```python
from math import sqrt, pi

result = sqrt(16)
print(pi)  # 3.14159...
```

### Import avec alias

```python
import numpy as np

array = np.array([1, 2, 3])
```

### Import tous les éléments

```python
from math import *

result = sqrt(16)  # Tous les éléments de math sont importés
```

---

## Modules courants

### sys

```python
import sys

# Accéder aux arguments de ligne de commande
print(sys.argv)

# Quitter le programme
sys.exit(0)
```

### math

```python
from math import sqrt, pi, ceil, floor

print(sqrt(25))    # 5.0
print(pi)          # 3.14159...
print(ceil(4.3))   # 5
print(floor(4.8))  # 4
```

### os

```python
import os

# Obtenir le chemin courant
current_dir = os.getcwd()

# Lister les fichiers
files = os.listdir('.')
```

---

## Créer un module personnalisé

### Fichier `my_module.py`

```python
def greet(name):
    """Salue une personne"""
    return f"Bonjour {name}"

def add(a, b):
    """Additionne deux nombres"""
    return a + b

PI = 3.14159
```

### Utiliser le module

```python
import my_module

message = my_module.greet("Alice")
result = my_module.add(5, 3)
print(my_module.PI)
```

---

## Structure `if __name__ == "__main__"`

```python
def my_function():
    print("Fonction executée")

if __name__ == "__main__":
    # Ce code ne s'exécute que si le fichier est exécuté directement
    # Pas s'il est importé dans un autre fichier
    my_function()
```

---

## Arguments de ligne de commande

### Fichier `script.py`

```python
import sys

print(sys.argv)  # Liste des arguments
print(sys.argv[0])  # Nom du script
print(sys.argv[1])  # Premier argument
```

### Exécution

```bash
python3 script.py arg1 arg2
# sys.argv = ['script.py', 'arg1', 'arg2']
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | add.py | Importer une fonction personnalisée |
| 1 | calculation.py | Importer et utiliser des modules |
| 2 | args.py | Accéder aux arguments de ligne de commande |
| 3 | infinite_add.py | Boucler sur les arguments |
| 4 | hidden_discovery.py | Découvrir les fonctions d'un module |

---

## Points importants

- Les modules facilitent la réutilisation de code
- L'import simple : `import module` ; import spécifique : `from module import function`
- Utilisez `as` pour créer des alias courts
- Évitez `from module import *` en production
- Utilisez `if __name__ == "__main__"` pour le code de test
- Les arguments sont accessibles via `sys.argv`

---

## Conseils pour bien apprendre

- Explorez les modules intégrés avec `dir()` et `help()`
- Créez vos propres modules pour pratiquer
- Utilisez les arguments de ligne de commande dans vos scripts
- Lisez la documentation des modules
- Organisez votre code en modules réutilisables

---

## Bon apprentissage !