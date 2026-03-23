# RESTful API

Apprentissage du développement d'APIs RESTful avec Python et Flask.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Principes REST](#principes-rest)
4. [Flask basique](#flask-basique)
5. [Liste des exercices](#liste-des-exercices)

---

## À propos

Ce dossier couvre les concepts des APIs RESTful et leur implémentation avec Flask. Vous apprendrez à construire des services web modernes.

---

## Concepts étudiés

- Architecture REST (Representational State Transfer)
- Méthodes HTTP : GET, POST, PUT, DELETE
- Codes de réponse HTTP (200, 201, 400, 404, 500)
- JSON comme format de données
- Flask pour créer des APIs
- Routes et endpoints
- Requêtes HTTP avec le module `requests`
- Sécurité basique

---

## Principes REST

### Les 6 contraintes REST

1. **Client-Serveur** : Séparation des responsabilités
2. **Statelessness** : Le serveur ne stocke pas l'état du client
3. **Uniform Interface** : API cohérente et prévisible
4. **Ressources** : Chaque données est une ressource avec une URI unique
5. **Représentation** : Les ressources sont représentées en JSON, XML, etc.
6. **État** : Transitions entre états via les méthodes HTTP

---

## Méthodes HTTP

| Méthode | Opération | Sûr | Idempotent |
|---|---|---|---|
| GET | Lire | Oui | Oui |
| POST | Créer | Non | Non |
| PUT | Remplacer | Non | Oui |
| PATCH | Modifier | Non | Non |
| DELETE | Supprimer | Non | Oui |

---

## Codes de réponse HTTP

| Code | Signification | Exemple |
|---|---|---|
| 200 | OK | Requête réussie |
| 201 | Created | Ressource créée |
| 204 | No Content | Succès, pas de contenu |
| 400 | Bad Request | Requête invalide |
| 401 | Unauthorized | Authentification requise |
| 403 | Forbidden | Accès refusé |
| 404 | Not Found | Ressource introuvable |
| 500 | Server Error | Erreur serveur |

---

## Flask basique

### Installation

```bash
pip install flask
```

### Premier serveur

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour le monde !"

@app.route('/api/users')
def get_users():
    return {"users": [{"id": 1, "name": "Alice"}]}

if __name__ == '__main__':
    app.run(debug=True, port=8000)
```

### Routes avec paramètres

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25}
]

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return {"error": "User not found"}, 404

@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data.get('name'),
        "age": data.get('age')
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return {"error": "User not found"}, 404

    data = request.get_json()
    user.update(data)
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return "", 204

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Requêtes HTTP avec requests

```python
import requests

# GET
response = requests.get('http://localhost:5000/api/users')
print(response.json())

# POST
data = {"name": "Alice", "age": 30}
response = requests.post('http://localhost:5000/api/users', json=data)
print(response.status_code)  # 201

# PUT
data = {"name": "Alice", "age": 31}
response = requests.put('http://localhost:5000/api/users/1', json=data)
print(response.json())

# DELETE
response = requests.delete('http://localhost:5000/api/users/1')
print(response.status_code)  # 204
```

---

## Gestion des erreurs

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Server error"}), 500

@app.route('/api/data')
def get_data():
    try:
        # Votre logique
        data = {"message": "Success"}
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

---

## Sécurité basique

### Validation d'entrée

```python
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('age'):
        return {"error": "Missing required fields"}, 400

    if not isinstance(data['age'], int) or data['age'] < 0:
        return {"error": "Invalid age"}, 400

    # Créer l'utilisateur
    return jsonify(new_user), 201
```

### CORS (Cross-Origin Resource Sharing)

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Active CORS pour tous les routes
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 2 | requests.py | Faire des requêtes HTTP |
| 3 | http_server.py | Serveur HTTP basique |
| 4 | flask.py | API avec Flask |
| 5 | basic_security.py | Sécurité et validation |

---

## Points importants

- REST utilise les méthodes HTTP appropriées
- Les réponses JSON doivent être valides
- Toujours valider les entrées utilisateur
- Retourner les bons codes HTTP
- Documenter votre API
- Sécuriser l'authentification

---

## Conseils pour bien apprendre

- Testez votre API avec curl ou Postman
- Commencez avec un serveur simple
- Ajoutez progressivement de la complexité
- Testez les codes d'erreur
- Explorez la documentation Flask
- Comprenez les principes REST

---

## Ressources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [REST API Best Practices](https://restfulapi.net/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html)

---

## Bon apprentissage !