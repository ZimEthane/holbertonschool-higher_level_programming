# SQL - Introduction

Apprentissage des bases de SQL pour interroger et manipuler les bases de données.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Commandes SQL de base](#commandes-sql-de-base)
4. [Liste des exercices](#liste-des-exercices)

---

## À propos

SQL (Structured Query Language) est le langage standard pour accéder et manipuler les bases de données relationnelles. Ce dossier couvre les opérations fondamentales.

---

## Concepts étudiés

- Bases de données et tables
- Commandes DDL : CREATE, ALTER, DROP
- Commandes DML : SELECT, INSERT, UPDATE, DELETE
- Clauses : WHERE, ORDER BY, LIMIT
- Fonctions d'agrégation : COUNT, SUM, AVG, MIN, MAX
- Types de données SQL
- Contraintes et clés

---

## Commandes SQL de base

### Créer une base de données

```sql
CREATE DATABASE IF NOT EXISTS my_database;
DROP DATABASE IF EXISTS my_database;
SHOW DATABASES;
USE my_database;
```

### Créer une table

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT DEFAULT 18
);

SHOW TABLES;
DESCRIBE users;
```

### Insérer des données

```sql
INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 30);

INSERT INTO users (name, email, age) VALUES
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);
```

### Sélectionner les données

```sql
-- Sélectionner tout
SELECT * FROM users;

-- Colonnes spécifiques
SELECT name, email FROM users;

-- Avec conditions
SELECT * FROM users WHERE age > 25;

-- Ordonner
SELECT * FROM users ORDER BY age ASC;

-- Limiter
SELECT * FROM users LIMIT 5;
SELECT * FROM users LIMIT 10 OFFSET 5;
```

### Modifier les données

```sql
UPDATE users SET age = 31 WHERE name = 'Alice';
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;
```

### Supprimer les données

```sql
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE age < 18;
```

---

## Clauses et filtrage

### WHERE avec opérateurs

```sql
-- Opérateurs de comparaison
SELECT * FROM users WHERE age = 30;
SELECT * FROM users WHERE age != 30;
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE age >= 25 AND age <= 35;

-- LIKE pour les chaînes
SELECT * FROM users WHERE name LIKE 'A%';        -- Commence par A
SELECT * FROM users WHERE email LIKE '%@example.com';

-- IN
SELECT * FROM users WHERE age IN (25, 30, 35);

-- BETWEEN
SELECT * FROM users WHERE age BETWEEN 25 AND 35;

-- IS NULL
SELECT * FROM users WHERE email IS NULL;
```

### Ordonner et grouper

```sql
-- ORDER BY
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY age DESC;

-- LIMIT
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;
```

---

## Fonctions d'agrégation

```sql
SELECT COUNT(*) FROM users;
SELECT COUNT(email) FROM users;
SELECT AVG(age) FROM users;
SELECT MIN(age) FROM users;
SELECT MAX(age) FROM users;
SELECT SUM(age) FROM users;

-- GROUP BY
SELECT age, COUNT(*) FROM users GROUP BY age;
SELECT name, COUNT(*) as count FROM orders GROUP BY name;
```

---

## Types de données courants

| Type | Description |
|---|---|
| INT | Nombre entier |
| VARCHAR(n) | Chaîne de longueur variable |
| CHAR(n) | Chaîne de longueur fixe |
| TEXT | Texte long |
| DECIMAL(p,s) | Nombre décimal |
| DATE | Date YYYY-MM-DD |
| DATETIME | Date et heure |
| BOOLEAN | Vrai/Faux |

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | list_databases.sql | SHOW DATABASES |
| 1 | create_database_if_missing.sql | CREATE DATABASE |
| 2 | remove_database.sql | DROP DATABASE |
| 3 | list_tables.sql | SHOW TABLES |
| 4 | first_table.sql | CREATE TABLE |
| 5 | full_table.sql | DESCRIBE TABLE |
| 6 | list_values.sql | SELECT * |
| 7 | insert_value.sql | INSERT INTO |
| 8 | count_89.sql | WHERE et COUNT |
| 9 | full_creation.sql | Créer une table complète |
| 10 | top_score.sql | TOP values |
| ... | ... | ... |

---

## Points importants

- SQL n'est pas sensible à la casse pour les commandes
- Les requêtes se terminent par `;`
- Utiliser les index pour des recherches rapides
- Toujours valider les entrées utilisateur
- Les contraintes assurent l'intégrité des données
- Faire des backups régulièrement

---

## Conseils pour bien apprendre

- Testez each en créant votre propre base
- Comprenez les jointures (LEFT, RIGHT, INNER, OUTER)
- Pratiquez les sous-requêtes
- Explorez les INDEX pour l'optimisation
- Utilisez des outils comme phpMyAdmin pour visualizer
- Écrivez des requêtes complexes progressivement

---

## Ressources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

---

## Bon apprentissage !