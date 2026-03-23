# SQL - More Queries

Approfondissement de SQL : jointures, sous-requêtes et concepts avancés.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Jointures](#jointures)
4. [Sous-requêtes](#sous-requêtes)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Ce dossier approfondit SQL avec des concepts avancés : jointures multiples, sous-requêtes imbriquées et agrégations complexes.

---

## Concepts étudiés

- Jointures : INNER, LEFT, RIGHT, OUTER
- Sous-requêtes
- AUTO_INCREMENT et les clés étrangères
- Limites et permissions utilisateur
- Constraints CHECK, DEFAULT
- Modifications de structure (ALTER TABLE)
- Vues et requêtes préparées

---

## Jointures

### INNER JOIN (intersection)

```sql
SELECT users.name, orders.order_id
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Plus court :
SELECT users.name, orders.order_id
FROM users
JOIN orders ON users.id = orders.user_id;
```

### LEFT JOIN (toutes les lignes à gauche)

```sql
SELECT users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id;
```

### RIGHT JOIN (toutes les lignes à droite)

```sql
SELECT users.name, orders.order_id
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```

### FULL OUTER JOIN (union)

```sql
SELECT users.name, orders.order_id
FROM users
FULL OUTER JOIN orders ON users.id = orders.user_id;
```

### Self Join

```sql
SELECT a.name as employee, b.name as manager
FROM employees a
JOIN employees b ON a.manager_id = b.id;
```

---

## Sous-requêtes

### Sous-requête dans WHERE

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT name
FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);
```

### Sous-requête dans FROM

```sql
SELECT avg_salary
FROM (
    SELECT AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) as dept_avg;
```

### EXISTS

```sql
SELECT name FROM users
WHERE EXISTS (
    SELECT 1 FROM orders WHERE orders.user_id = users.id
);
```

---

## Contraintes et clés

### Clés étrangères

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

### Contraintes CHECK

```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    CHECK (price > 0)
);
```

### Contraintes UNIQUE

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL
);
```

---

## Agrégations avancées

### GROUP BY avec HAVING

```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING avg_salary > 50000;

SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 5;
```

### Fenêtres (Window Functions)

```sql
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as rank,
    AVG(salary) OVER () as avg_salary
FROM employees;
```

---

## Modification de structure

### ALTER TABLE

```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users MODIFY name VARCHAR(100);
ALTER TABLE users RENAME TO customers;
```

---

## Vues

```sql
CREATE VIEW high_value_orders AS
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id
WHERE orders.total > 1000;

SELECT * FROM high_value_orders;
```

---

## Permissions utilisateur

```sql
-- Créer un utilisateur
CREATE USER 'john'@'localhost' IDENTIFIED BY 'password123';

-- Accorder des permissions
GRANT SELECT, INSERT ON my_database.* TO 'john'@'localhost';
GRANT ALL PRIVILEGES ON my_database.* TO 'john'@'localhost';

-- Révoquer les permissions
REVOKE INSERT ON my_database.* FROM 'john'@'localhost';

-- Supprimer un utilisateur
DROP USER 'john'@'localhost';
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | privileges.sql | Permissions utilisateur |
| 1 | create_user.sql | CREATE USER |
| 2 | create_read_user.sql | Permissions SELECT |
| 3 | force_name.sql | Contrainte NOT NULL |
| 4 | never_empty.sql | Contrainte DEFAULT |
| 5 | unique_id.sql | Contrainte UNIQUE |
| 6 | states.sql | Créer une table |
| 7 | cities.sql | Clés étrangères |
| 8 | cities_of_california_subquery.sql | Sous-requête |
| 9 | cities_by_state_join.sql | JOIN |
| ... | ... | ... |

---

## Points importants

- Choisissez le bon type de JOIN
- Les sous-requêtes doivent être simples et lisibles
- Les index sur les clés étrangères améliorent pas
- FOREIGN KEY ON DELETE CASCADE peut supprimer automatiquement
- Les vues simplifient les requêtes complexes
- Testez toujours les permissions correctement

---

## Conseils pour bien apprendre

- Dessinez les diagrammes des jointures
- Testez chaque type de JOIN
- Pratiquez les sous-requêtes progressivement
- Comprenez les permissions utilisateur
- Explorez les INDEX pour l'optimisation
- Utilisez EXPLAIN pour analyser les performances

---

## Ressources

- [MySQL Joins](https://dev.mysql.com/doc/)
- [SQL Advanced Queries](https://www.w3schools.com/sql/)

---

## Bon apprentissage !