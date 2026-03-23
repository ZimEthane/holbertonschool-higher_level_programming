# Python - Hello World

Premiers pas en Python : apprendre les bases de la syntaxe et les opérations simples.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Liste des exercices](#liste-des-exercices)
4. [Comment exécuter les scripts](#comment-exécuter-les-scripts)

---

## À propos

Ce dossier contient des exercices pour débuter en Python. Vous apprendrez à :
- Utiliser la fonction `print()` pour afficher du texte
- Afficher des nombres entiers et décimaux
- Concaténer des chaînes de caractères
- Manipuler les types de données basiques

---

## Concepts étudiés

- Syntaxe de base de Python
- Fonction `print()`
- Types de données primitifs (int, float, str)
- Concaténation de chaînes
- Utilisation du shebang `#!/usr/bin/python3`
- Exécution de scripts Python depuis le terminal

---

## Liste des exercices

| # | Titre | Description |
|---|---|---|
| 2 | print.py | Afficher une chaîne de caractères sur plusieurs lignes |
| 3 | print_number.py | Afficher un nombre entier avec du texte |
| 4 | print_float.py | Afficher un nombre décimal formaté |
| 5 | print_string.py | Afficher une chaîne de caractères répétée |
| 6 | concat.py | Concaténer plusieurs chaînes de caractères |
| 7 | edges.py | Afficher le premier et le dernier caractère d'une chaîne |
| 8 | concat_edges.py | Combiner les premiers et derniers caractères de deux chaînes |
| 9 | easter_egg.py | Afficher le Zen de Python (easter egg) |

---

## Comment exécuter les scripts

### Méthode 1 : Depuis le terminal (recommandé)

```bash
cd python-hello_world
python3 2-print.py
python3 3-print_number.py
python3 4-print_float.py
```

### Méthode 2 : Avec le shebang

Certains scripts ont le shebang `#!/usr/bin/python3` au début, vous pouvez les exécuter directement :

```bash
./2-print.py
./3-print_number.py
```

### Méthode 3 : Depuis VS Code

1. Ouvrez le fichier Python
2. Appuyez sur `Ctrl + Alt + N` (extensions Code Runner)
3. Ou cliquez sur le bouton "Run" en haut à droite

---

## Concepts clés avec exemples

### Afficher du texte

```python
print("Bonjour le monde")
```

### Afficher des nombres

```python
number = 98
print(f"My number: {number}")
```

### Concaténation

```python
str1 = "Python"
str2 = "est"
str3 = "cool"
print(f"{str1} {str2} {str3}")
```

### Accéder aux caractères

```python
str_data = "Hello"
print(str_data[0])    # Affiche "H"
print(str_data[-1])   # Affiche "o"
```

---

## Points importants

- Python utilise 0 pour l'indentation des blocs de code
- Les chaînes peuvent être en simple ou double guillemets
- Les f-strings (f"{}") facilitent l'insertion de variables
- `print()` ajoute un retour à la ligne automatiquement
- Les índices négatifs permettent d'accéder aux caractères en partant de la fin

---

## Conseils pour bien démarrer

- Écrivez vos scripts et testez-les immédiatement
- Modifiez les valeurs et regardez les résultats changer
- Essayez de comprendre chaque ligne avant de passer à la suivante
- Utilisez `print()` pour déboguer votre code

---

## Besoin d'aide ?

1. Consultez la documentation officielle : https://docs.python.org/3/
2. Lisez les commentaires et docstrings dans les fichiers
3. Testez vos modifications dans la console Python
4. Utilisez `print()` pour afficher les valeurs intermédiaires

---

## Bon apprentissage !
