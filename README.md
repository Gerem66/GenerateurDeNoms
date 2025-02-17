# Générateur de Noms/Pseudos

Un générateur de pseudos intelligent pour créer des noms cohérents dans différents styles (humain, fantaisie, etc.).

## 🚀 Fonctionnalités

- Génération de noms basée sur des chaînes de Markov
- Plusieurs catégories : Humain, World of Warcraft, Skyrim
- Interface web simple et intuitive (Fake API)
- Filtre de noms avec conditions (commence par, termine par, contient, etc)

## 💻 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Gerem66/GenerateurDeNoms.git
cd GenerateurDeNoms
```

2. Installation des dépendances Python (aucune dépendance externe requise, uniquement Python 3)

## 🎯 Utilisation

### Ligne de commande
```bash
python3 FindBestName.py
```

### Conditions de filtrage
Dans le fichier `main.py`, vous pouvez définir des conditions pour filtrer les noms générés :
- `x` : Le nom doit contenir 'x'
- `!x` : Le nom doit contenir 'x' (obligatoire)
- `x*` : Le nom doit commencer par 'x'
- `*x` : Le nom doit se terminer par 'x'

Exemple :
```python
generator.conditions = ['a*', '*i']  # Noms commençant par 'a' et finissant par 'i'
```

## 📚 Sources des données

- [Base de données de prénoms humains](https://www.data.gouv.fr/fr/datasets/liste-de-prenoms-et-patronymes/)
- [Noms de Skyrim](https://elderscrolls.fandom.com/wiki/Category:Skyrim:_Characters)
- [Personnages de Warcraft](https://fr.wikipedia.org/wiki/Personnages_de_Warcraft)
