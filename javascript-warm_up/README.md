# JavaScript - Warm Up

Premiers pas en JavaScript : syntaxe de base et concepts fondamentaux.

---

## Table des matières

1. [À propos](#à-propos)
2. [Concepts étudiés](#concepts-étudiés)
3. [Syntaxe de base](#syntaxe-de-base)
4. [Liste des exercices](#liste-des-exercices)

---

## À propos

Ce dossier contient des exercices pour débuter en JavaScript. Vous apprendrez la syntaxe, les variables, les opérateurs et les fonctions de base.

---

## Concepts étudiés

- Variables : `var`, `let`, `const`
- Types de données : Number, String, Boolean, Array, Object
- Opérateurs arithmétiques et logiques
- Conditions if/else
- Boucles for et while
- Fonctions et arguments
- Console.log pour déboguer
- Conversion de types

---

## Syntaxe de base

### Variables

```javascript
// var (ancien, éviter)
var name = "Alice";

// let (bloqué au scope)
let age = 30;

// const (immutable)
const PI = 3.14159;

// Types de données
let number = 42;
let text = "Bonjour";
let boolean = true;
let array = [1, 2, 3];
let object = { name: "Alice", age: 30 };
```

### Affichage

```javascript
// Log à la console
console.log("Bonjour");
console.log(5 + 3);

// Log avec template literals
let name = "Alice";
console.log(`Bonjour ${name}`);
```

### Opérateurs

```javascript
// Arithmétiques
console.log(5 + 3);    // 8
console.log(5 - 3);    // 2
console.log(5 * 3);    // 15
console.log(5 / 2);    // 2.5
console.log(5 % 2);    // 1
console.log(2 ** 3);   // 8 (puissance)

// Comparaison
console.log(5 == 5);   // true
console.log(5 === "5"); // false (strict)
console.log(5 != 5);   // false
console.log(5 < 10);   // true

// Logiques
console.log(true && false);  // false
console.log(true || false);  // true
console.log(!true);          // false
```

### Conditions

```javascript
let age = 15;

if (age < 13) {
    console.log("Enfant");
} else if (age < 18) {
    console.log("Adolescent");
} else {
    console.log("Adulte");
}

// Opérateur ternaire
let category = age < 18 ? "Mineur" : "Adulte";
```

### Boucles

```javascript
// for
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// while
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

// forEach sur un array
let numbers = [1, 2, 3, 4, 5];
numbers.forEach(function(num) {
    console.log(num);
});
```

### Fonctions

```javascript
// Définir une fonction
function greet(name) {
    return "Bonjour " + name;
}

console.log(greet("Alice"));

// Fonction avec plusieurs paramètres
function add(a, b) {
    return a + b;
}

console.log(add(5, 3));

// Arrow function (ES6)
const multiply = (a, b) => a * b;
console.log(multiply(5, 3));

// Fonction avec arguments variables
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}

console.log(sum(1, 2, 3, 4, 5));
```

---

## Entrée/Sortie

### Depuis Node.js

```javascript
// Accéder aux arguments de ligne de commande
console.log(process.argv);

// Le premier argument est process.argv[2]
let value = process.argv[2];
```

### Exemple

```javascript
#!/usr/bin/node

// Convertir l'argument en nombre
let number = parseInt(process.argv[2]);

if (number > 0) {
    console.log("Positif");
} else if (number < 0) {
    console.log("Négatif");
} else {
    console.log("Zéro");
}
```

---

## Exécuter les scripts

```bash
node script.js
node script.js argument1
node script.js 42
```

---

## Liste des exercices

| # | Titre | Concepts |
|---|---|---|
| 0 | amazing.js | Afficher du texte |
| 1 | multi_languages.js | Boucles et affichage |
| 2 | arguments.js | Accéder aux arguments |
| 3 | value_argument.js | Récupérer l'argument 2 |
| 4 | concat.js | Concaténer les arguments |
| 5 | to_integer.js | Convertir en nombre |
| 6 | multi_languages_loop.js | Boucle avec arguments |
| 7 | multi_c.js | Répéter un caractère |
| 8 | square.js | Afficher un carré |
| 9 | add.js | Additionner les arguments |
| 10 | factorial.js | Calcul récursif |
| 11 | second_biggest.js | Trouver le 2e plus grand |
| 12 | object.js | Créer un objet |
| 13 | add.js | Exporter une fonction |

---

## Points importants

- Utilisez `let` et `const` au lieu de `var`
- Les template literals facilitent l'insertion de variables
- Les arrow functions sont plus concises
- Les arguments du programme sont dans process.argv
- Testez vos scripts avec console.log

---

## Conseils pour bien apprendre

- Testez chaque exercice dans Node.js
- Modifiez les valeurs et observez les résultats
- Utilisez console.log pour déboguer
- Comprenez la différence entre `==` et `===`
- Pratiquez les fonctions flèches
- Explorez l'aide de Node.js avec `node --help`

---

## Ressources

- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Node.js Documentation](https://nodejs.org/en/docs/)

---

## Bon apprentissage !
