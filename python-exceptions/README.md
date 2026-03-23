# Python - Exceptions

Apprentissage de la gestion des erreurs et des exceptions en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Types d'exceptions courantes](#types-dexceptions-courantes)
4. [Liste des exercices](#liste-des-exercices)

---

## À propos

Les exceptions sont des événements qui se produisent lors de l'exécution d'un programme et qui interrompent le flux normal. Ce dossier vous apprend à les gérer correctement avec try/except.

---

## Concepts étudiés

- Comprendre les exceptions
- Syntaxe try/except/else/finally
- Attraper des exceptions spécifiques
- Lever des exceptions avec `raise`
- Créer des exceptions personnalisées
- Assurer la robustesse du code
- Nettoyage des ressources avec `finally`

---

## Types d'exceptions courantes

| Exception | Cause |
|---|---|
| `ZeroDivisionError` | Division par zéro |
| `ValueError` | Type correct mais valeur invalide |
| `TypeError` | Type de données incorrect |
| `IndexError` | Index inexistant dans une séquence |
| `KeyError` | Clé inexistante dans un dictionnaire |
| `FileNotFoundError` | Fichier non trouvé |
| `AttributeError` | Attribut ou méthode inexistante |

---

## Liste des exercices

| # | Titre | Description |
|---|---|---|
| 0 | safe_print_list.py | Afficher une liste sans crash |
| 1 | safe_print_integer.py | Afficher un entier de manière sûre |
| 2 | safe_print_list_integers.py | Afficher les entiers d'une liste |
| 3 | safe_print_division.py | Division sûre avec gestion d'erreurs |
| 4 | list_division.py | Diviser les éléments de deux listes |
| 5 | raise_exception.py | Lever une exception personnalisée |
| 6 | raise_message.py | Lever une exception avec message |

---

## Syntaxe de base

### Try/Except simple

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro !")
```

### Catch multiple

```python
try:
    value = int(input("Entrez un nombre : "))
except ValueError:
    print("Ce n'est pas un nombre !")
except TypeError:
    print("Type incorrect !")
```

### Try/Except/Else/Finally

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("Fichier non trouvé")
else:
    print("Fichier lu avec succès")
finally:
    file.close()  # S'exécute toujours
```

### Lever une exception

```python
def validate_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")
    return age
```

---

## Points importants

- Toujours attraper les exceptions les plus spécifiques d'abord
- Ne jamais utiliser `except Exception` sans raison
- `finally` s'exécute TOUJOURS, même en cas d'exception
- `raise` permet de lever vos propres exceptions
- Les exceptions facilient le débogage du code
- Utilisez des messages d'erreur clairs

---

## Bonnes pratiques

```python
# BON : gérer les erreurs proprement
try:
    result = 10 / number
except ZeroDivisionError:
    print("Impossible de diviser par zéro")
    result = None

# MAUVAIS : ignorer les erreurs silencieusement
try:
    result = 10 / number
except:
    pass
```

---

## Exercices pratiques

Pour chaque exercice :
1. Lisez le code existant
2. Identifiez les points susceptibles de lever une exception
3. Écrivez du code try/except approprié
4. Testez avec des entrées invalides
5. Vérifiez que le programme ne crash pas

---

## Conseils pour bien apprendre

- Forcez les erreurs intentionnellement pour comprendre
- Lisez les messages d'erreur complètement
- Utilisez `print()` pour déboguer avant et après les blocs try
- Pratiquez avec différents types d'exceptions
- Consultez la documentation des exceptions intégrées

---

## Bon apprentissage !
