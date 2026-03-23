# JavaScript - DOM Manipulation

Exercices d'apprentissage sur la manipulation du DOM (Document Object Model) en JavaScript.

---

## Table des matières

1. [Installation de Live Server](#installation-de-live-server)
2. [Comment utiliser Live Server](#comment-utiliser-live-server)
3. [Liste des exercices](#liste-des-exercices)
4. [Instructions pour chaque exercice](#instructions-pour-chaque-exercice)
5. [Dépannage](#dépannage)

---

## Installation de Live Server

### Qu'est-ce que Live Server ?

**Live Server** est une extension VS Code qui lance un **serveur local** et recharge automatiquement la page quand tu modifies un fichier. C'est parfait pour développer rapidement.

### Étapes d'installation

#### 1. Ouvre VS Code
- Ouvre le dossier `javascript-dom_manipulation`

#### 2. Accès aux extensions
- **Windows/Linux** : `Ctrl + Shift + X`
- **Mac** : `Cmd + Shift + X`

#### 3. Recherche Live Server
- Tape `Live Server` dans la barre de recherche
- Cherche l'extension par **Ritwick Dey** (vérifiée avec le badge bleu)

#### 4. Installe l'extension
- Clique sur le bouton **"Install"**
- Attends que l'installation se termine

#### 5. Redémarre VS Code (optionnel)
- Ferme et rouvre VS Code si nécessaire

**Voilà ! Live Server est installé !**

---

## Comment utiliser Live Server

### Démarrer le serveur

#### Méthode 1 : Clic droit (Plus facile)
1. **Ouvre l'explorateur de fichiers** (panneau de gauche)
2. **Clique droit** sur le fichier HTML que tu veux tester
3. Sélectionne **"Open with Live Server"**
4. Ton navigateur s'ouvre automatiquement

#### Méthode 2 : Bouton en bas (Alternative)
1. **Ouvre** le fichier HTML dans VS Code
2. Regarde en bas à droite : tu dois voir **"Go Live"**
3. Clique sur **"Go Live"**
4. Ton navigateur s'ouvre à `http://localhost:5500`

#### Méthode 3 : Menu (Autre alternative)
1. Clic sur **"File"** → **"Open with Live Server"**

### Arrêter le serveur

- Clique sur **"Port: 5500"** en bas à droite pour arrêter

### Astuce

Quand tu **modifies et sauvegardes** un fichier (`Ctrl + S`), la page **se recharge automatiquement** ! Pas besoin d'appuyer sur F5 !

---

## Liste des exercices

| # | Titre | Concepts clés |
|---|---|---|
| 2 | Add .red class | `addEventListener`, `querySelector`, `classList.add()` |
| 3 | Toggle class | `classList.contains()`, `classList.remove()`, conditions |
| 4 | List of elements | `createElement()`, `appendChild()`, `textContent` |
| 5 | Change the text | `textContent`, changement de contenu |
| 6 | Star Wars character | `fetch()`, `.then()`, Promises, APIs |
| 7 | Star wars movies | `fetch()`, `forEach()`, boucles sur Arrays |
| 8 | Say Hello! | `DOMContentLoaded`, scripts dans le `<head>` |

---

## Instructions pour chaque exercice

### Exercice 2 - Add .red class

**Fichiers :**
- HTML : `html-2.html`
- JavaScript : `2-script.js`

**Instructions :**
1. Clique droit sur `html-2.html`
2. Sélectionne **"Open with Live Server"**
3. La page s'ouvre dans le navigateur
4. **Clique** sur "Red header"
5. Le titre devient **ROUGE**

**Concepts :** Ajouter une classe CSS avec JavaScript

---

### Exercice 3 - Toggle class

**Fichiers :**
- HTML : `html-3.html`
- JavaScript : `3-script.js`

**Instructions :**
1. Clique droit sur `html-3.html`
2. Sélectionne **"Open with Live Server"**
3. Le titre est initialement **VERT**
4. **Clique** sur "Toggle header"
5. Le titre devient **ROUGE**
6. **Clique à nouveau**
7. Le titre redevient **VERT**
8. Clique autant que tu veux, ça bascule

**Concepts :** Vérifier une classe et la remplacer

---

### Exercice 4 - List of elements

**Fichiers :**
- HTML : `html-4.html`
- JavaScript : `4-script.js`

**Instructions :**
1. Clique droit sur `html-4.html`
2. Sélectionne **"Open with Live Server"**
3. Tu vois une liste avec 1 élément : "Item"
4. **Clique** sur "Add item"
5. Un nouvel "Item" s'ajoute à la liste
6. **Clique plusieurs fois** pour ajouter plus d'éléments
7. La liste grandit à chaque clic

**Concepts :** Créer des éléments HTML dynamiquement

---

### Exercice 5 - Change the text

**Fichiers :**
- HTML : `html-5.html`
- JavaScript : `5-script.js`

**Instructions :**
1. Clique droit sur `html-5.html`
2. Sélectionne **"Open with Live Server"**
3. Le titre affiche "First HTML page"
4. **Clique** sur "Update the header"
5. Le titre change à **"New Header!!!!"**
6. Clique à nouveau, le texte reste le même (une seule action)

**Concepts :** Changer le contenu texte d'un élément

---

### Exercice 6 - Star Wars character

**Fichiers :**
- HTML : `html-6.html`
- JavaScript : `6-script.js`

**Instructions :**
1. Clique droit sur `html-6.html`
2. Sélectionne **"Open with Live Server"**
3. **Attends quelques secondes** (les données se chargent)
4. Le nom **"Leia Organa"** apparaît

**Concepts :**
- Faire une requête HTTP avec `fetch()`
- Utiliser les Promises avec `.then()`
- Accéder aux données d'une API

**Important :**
- Le navigateur a besoin d'**Internet** pour récupérer les données
- Attends 1-2 secondes que l'API réponde

---

### Exercice 7 - Star Wars movies

**Fichiers :**
- HTML : `html-7.html`
- JavaScript : `7-script.js`

**Instructions :**
1. Clique droit sur `html-7.html`
2. Sélectionne **"Open with Live Server"**
3. **Attends quelques secondes**
4. Une liste de **9 films Star Wars** apparaît :

```
• A New Hope
• The Empire Strikes Back
• Return of the Jedi
• The Phantom Menace
• Attack of the Clones
• Revenge of the Sith
• The Force Awakens
• The Last Jedi
• The Rise of Skywalker
```

**Concepts :**
- Utiliser `fetch()` pour récupérer une liste
- Utiliser `forEach()` pour boucler sur les données
- Créer plusieurs éléments dynamiquement

**Important :**
- Internet requis
- La première fois prend plus de temps (cache vide)

---

### Exercice 8 - Say Hello!

**Fichiers :**
- HTML : `html-8.html`
- JavaScript : `8-script.js`

**Instructions :**
1. Clique droit sur `html-8.html`
2. Sélectionne **"Open with Live Server"**
3. **Attends une seconde**
4. Le mot **"Bonjour"** apparaît

**Concepts :**
- Utiliser `DOMContentLoaded` quand le script est dans le `<head>`
- Attendre que le page soit complètement chargée avant d'y accéder
- Récupérer des données d'une API simple

**Important :**
- Internet requis
- Le script est intentionnellement dans le `<head>` (teste un nouveau concept)

---

## Dépannage

### Problème : "Live Server n'apparaît pas"

**Solution :**
1. Redémarre VS Code complètement
2. Réinstalle Live Server
3. Vérifie que l'extension est bien activée (onglet "Extensions")

### Problème : La page ne se recharge pas automatiquement

**Solution :**
1. Clique sur **"Go Live"** en bas à droite
2. Vérifie que tu as sauvegardé (`Ctrl + S`)
3. Attends 1 seconde, la page devrait recharger

### Problème : Erreur "Cannot GET /"

**Solution :**
1. Assure-toi que tu as **cliqué droit sur un fichier HTML**
2. Clique sur **"Open with Live Server"** et non "Open with Code"

### Problème : La console affiche une erreur

**Solution :**
1. Ouvre la console du navigateur : `F12`
2. Onglet **"Console"**
3. Lis le message d'erreur
4. Vérifie que :
   - L'ID du fichier HTML correspond au sélecteur JavaScript
   - La syntaxe JavaScript est correcte

### Problème : Les données d'API ne chargent pas

**Solution :**
1. Vérifie que tu as **Internet**
2. Attends **quelques secondes** (première fois plus lente)
3. Ouvre la console (`F12`) et cherche les erreurs
4. Le serveur API peut être temporairement indisponible

### Problème : "Port 5500 already in use"

**Solution :**
1. Clique sur **"Port: 5500"** en bas à droite pour arrêter
2. Relance avec **"Go Live"**
3. Ou redémarre VS Code

---

## Ressources utiles

### Documentation
- [MDN - DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model)
- [MDN - fetch() API](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API)
- [MDN - Promises](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### Outils
- [Live Server GitHub](https://github.com/ritwickdey/vscode-live-server)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) (console pour déboguer)

### Raccourcis clavier utiles
| Action | Windows | Mac |
|---|---|---|
| Ouvrir console | `F12` | `Cmd + Option + I` |
| Sauvegarder | `Ctrl + S` | `Cmd + S` |
| Recharger page | `F5` ou `Ctrl + R` | `Cmd + R` |
| Recharger complet | `Ctrl + Shift + R` | `Cmd + Shift + R` |

---

## Conseils pour bien apprendre

### À faire

- **Teste chaque exercice** en ouvrant la page dans le navigateur
- **Utilise la console** (`F12`) pour déboguer
- **Modifie le code** et vois ce qui change
- **Essaie de créer tes propres exercices** après avoir compris

### À éviter

- Ne juste lis pas le code, **exécute-le**
- Ne saute pas les exercices, fais-les dans l'ordre
- Ne copie pas sans comprendre, **explique-toi** chaque ligne

---

## Besoin d'aide ?

1. **Console du navigateur** : `F12` → Onglet "Console"
2. **VS Code IntelliSense** : Hover sur les fonctions
3. **Documentation MDN** : Cherche la fonction sur MDN
4. **Relire les explications** : Elles contiennent tous les détails

---

## Bon apprentissage ! Happy coding!