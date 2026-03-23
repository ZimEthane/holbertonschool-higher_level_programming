# Python - Test Driven Development

Apprentissage de la méthodologie Test Driven Development (TDD) en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Framework unittest](#framework-unittest)
4. [Écrire des tests](#écrire-des-tests)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

TDD est une méthodologie où on écrit les tests AVANT le code. Ce dossier couvre le framework `unittest` et les bonnes pratiques de test.

---

## Concepts étudiés

- Méthodologie TDD : Red-Green-Refactor
- Framework `unittest`
- Assertions et tests
- Setup et teardown
- Tests unitaires vs tests d'intégration
- Couverture de code
- Mocking et patching
- Bonnes pratiques

---

## Framework unittest

### Structure de base

```python
import unittest

class TestAddition(unittest.TestCase):
    def setUp(self):
        """s'exécute avant chaque test"""
        self.x = 5
        self.y = 3

    def tearDown(self):
        """s'exécute après chaque test"""
        pass

    def test_add(self):
        """Tester l'addition"""
        result = self.x + self.y
        self.assertEqual(result, 8)

    def test_add_fails(self):
        """Tester que ça fail"""
        result = self.x + self.y
        self.assertNotEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
```

---

## Assertions disponibles

```python
import unittest

class TestAssertions(unittest.TestCase):
    def test_assertions(self):
        # Vérifier l'égalité
        self.assertEqual(5 + 3, 8)
        self.assertNotEqual(5 + 3, 10)

        # Vérifier True/False
        self.assertTrue(5 > 3)
        self.assertFalse(5 < 3)

        # Vérifier None
        self.assertIsNone(None)
        self.assertIsNotNone([])

        # Vérifier l'appartenance
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(5, [1, 2, 3])

        # Vérifier les types
        self.assertIsInstance("hello", str)
        self.assertNotIsInstance(5, str)

        # Vérifier les listes
        self.assertListEqual([1, 2], [1, 2])

        # Vérifier les exceptions
        with self.assertRaises(ValueError):
            int("not a number")

        # Vérifier une condition
        self.assertTrue(True, "Message si ça fail")
```

---

## Tests de fonction

```python
def add(a, b):
    """Additionne deux nombres"""
    return a + b

def divide(a, b):
    """Divise a par b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

import unittest

class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
```

---

## Tests de classe

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 60

import unittest

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student_pass = Student("Alice", 75)
        self.student_fail = Student("Bob", 45)

    def test_student_passing(self):
        self.assertTrue(self.student_pass.is_passing())

    def test_student_failing(self):
        self.assertFalse(self.student_fail.is_passing())

    def test_student_name(self):
        self.assertEqual(self.student_pass.name, "Alice")
```

---

## Exécuter les tests

```bash
# Exécuter tous les tests d'un fichier
python3 -m unittest test_file.py

# Exécuter une classe de test
python3 -m unittest test_file.TestClass

# Exécuter une méthode de test
python3 -m unittest test_file.TestClass.test_method

# Exécuter avec verbose
python3 -m unittest -v test_file.py

# Découvrir et exécuter tous les tests
python3 -m unittest discover
```

---

## Méthodologie Red-Green-Refactor

1. **RED** : Écrire un test qui fail
2. **GREEN** : Écrire le code minimum pour passer le test
3. **REFACTOR** : Améliorer le code sans casser les tests

```python
# Étape 1 : RED - test qui fail
def test_calculate_average():
    result = calculate_average([1, 2, 3, 4, 5])
    self.assertEqual(result, 3)

# Étape 2 : GREEN - code minimal
def calculate_average(numbers):
    return 3

# Étape 3 : REFACTOR - code correct
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | add_integer.py | Tests basiques |
| 1 | add_integer.py | More testing |
| 2 | matrix_divided.py | Diviser une matrice |
| 3 | say_my_name.py | Formater une chaîne |
| 4 | print_square.py | Afficher un carré |
| 5 | text_indentation.py | Indenter un texte |

---

## Points importants

- Écrire les tests AVANT le code (TDD)
- Chaque test doit tester UNE chose
- Utiliser des noms explicites pour les tests
- setUp et tearDown pour la préparation
- Assertions claires avec des messages
- Toujours tester les cas limites

---

## Conseils pour bien apprendre

- Écrivez des tests pour chaque fonction
- Testez les cas normaux et les cas limites
- Testez les exceptions
- Utilisez setUp pour préparer les données
- Explorez coverage pour vérifier votre couverture
- Pratiquez TDD sur de petits projets

---

## Bon apprentissage !