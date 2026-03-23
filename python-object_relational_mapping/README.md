# Python - Object Relational Mapping

Apprentissage de l'ORM (Object Relational Mapping) avec SQLAlchemy en Python.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [SQLAlchemy basique](#sqlalchemy-basique)
4. [Modèles et relations](#modèles-et-relations)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Les ORM permettent de travailler avec les bases de données en utilisant des objets Python au lieu de requêtes SQL brutes. SqlAlchemy est le plus populaire ORM Python.

---

## Concepts étudiés

- Configuration SQLAlchemy
- Création de connecteurs de base de données
- Définition de modèles (tables comme classes)
- Relations entre modèles
- Créer, lire, modifier, supprimer (CRUD)
- Requêtes complexes
- Sessions et transactions
- Héritage de modèles

---

## SQLAlchemy basique

### Installation

```bash
pip install sqlalchemy mysqldb
```

### Configuration de base

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Créer une connexion
engine = create_engine('mysql://user:password@localhost/my_database')

# Créer une base pour les modèles
Base = declarative_base()

# Créer une session
Session = sessionmaker(bind=engine)
session = Session()
```

---

## Modèles

### Définir un modèle

```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"

# Créer la table
Base.metadata.create_all(engine)
```

---

## CRUD Operations

### Create (Créer)

```python
# Créer un nouvel utilisateur
user = User(name="Alice", email="alice@example.com", age=30)
session.add(user)
session.commit()
```

### Read (Lire)

```python
# Récupérer un utilisateur par ID
user = session.query(User).filter_by(id=1).first()

# Récupérer tous les utilisateurs
all_users = session.query(User).all()

# Filtrer
adults = session.query(User).filter(User.age >= 18).all()

# Ordonner
sorted_users = session.query(User).order_by(User.name).all()

# Limiter
first_five = session.query(User).limit(5).all()
```

### Update (Modifier)

```python
# Récupérer et modifier
user = session.query(User).filter_by(id=1).first()
user.age = 31
session.commit()
```

### Delete (Supprimer)

```python
# Supprimer un utilisateur
user = session.query(User).filter_by(id=1).first()
session.delete(user)
session.commit()
```

---

## Relations

### One-to-Many

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

# Utilisation
author = Author(name="Tolkien")
book1 = Book(title="The Hobbit", author=author)
book2 = Book(title="The Lord of the Rings", author=author)

session.add(author)
session.commit()

# Accéder aux livres de l'auteur
print(author.books)  # [book1, book2]
```

---

## Requêtes complexes

```python
# Jointure
results = session.query(Author).join(Book).filter(Book.title.like('%Hobbit%')).all()

# Agrégation
from sqlalchemy import func

# Compter
count = session.query(User).count()

# Moyenne
avg_age = session.query(func.avg(User.age)).scalar()

# Grouper
by_age = session.query(User.age, func.count(User.id)).group_by(User.age).all()
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | select_states.py | Requête SELECT basique |
| 1 | filter_states.py | Filtrer avec WHERE |
| 2 | filter_states_by_user_input.py | Entrée utilisateur |
| ... | ... | ... |
| 10 | model_state_my_get.py | Trouver par ID |
| 11 | model_state_insert.py | Insérer un nouvel objet |

---

## Points importants

- Les modèles sont des classes qui mappe les tables
- Les relations facilitent la navigation entre les tables
- Les sessions gèrent les transactions
- Toujours commit() après les modifications
- Utiliser filter() pour les requêtes complexes
- Les ORM protègent contre les injections SQL

---

## Conseils pour bien apprendre

- Commencez avec des modèles simples
- Testez chaque opération CRUD
- Explorez les relations
- Utilisez la documentation SQLAlchemy
- Pratiquez avec une Base de données réelle
- Comprenez les transactions

---

## Ressources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/14/orm/index.html)

---

## Bon apprentissage !