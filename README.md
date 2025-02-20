# PseudoForge - Générateur de Noms

Un générateur de pseudos intelligent pour créer des noms cohérents dans différents styles (humain, fantaisie, etc.).

## 🚀 Fonctionnalités

- Génération de noms basée sur des chaînes de Markov
- Plusieurs bases de données : Prénoms humains, World of Warcraft, Skyrimk, Harry Potter
- Système d'apprentissage via une base de données personnalisée
- Filtre de noms avec conditions (commence par, termine par, contient, ...)

## 💻 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Gerem66/PseudoForge.git
cd PseudoForge
```

2. Prérequis : Python 3 (aucune dépendance externe requise)

## 🎯 Utilisation

### Génération rapide (mode console)
```bash
python3 generator.py
```
Affiche en continu plusieurs colonnes de noms générés à partir de toutes les bases de données disponibles. Idéal pour explorer rapidement différents styles de noms.

### Génération précise (mode API)
```bash
python3 get-names.py <type_db> [nombres_de_noms]
```
Génère des noms "purs" sans formatage supplémentaire.

### Mode interactif avec apprentissage
```bash
python3 find-best-name.py
```
Interface interactive permettant de :
- Générer des noms à partir des bases de données existantes
- Sélectionner vos noms préférés
- Créer une base de données personnalisée
- Générer de nouveaux noms basés sur vos sélections

### Filtres de génération
Les noms peuvent être filtrés avec les conditions suivantes :
- `x` : Contient 'x'
- `!x` : Doit contenir 'x'
- `x*` : Commence par 'x'
- `*x` : Se termine par 'x'

## 📚 Sources des données

- Prénoms humains : data.gouv.fr
- Noms Skyrim : Elder Scrolls Wiki
- Noms Warcraft : Wikipedia
