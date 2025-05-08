# HockeyIQ

## Nature et Objectif du Projet

HockeyIQ est une application interactive conçue pour les amateurs de dek hockey et les joueurs. Elle vise à fournir des statistiques détaillées, des classements, des comparaisons d'équipes et de joueurs, ainsi que des prédictions basées sur des données réelles. L'objectif est d'offrir une plateforme intuitive pour analyser les performances des équipes et des joueurs, tout en permettant aux utilisateurs de suivre les matchs et de gérer leurs comptes.

### Clientèle Cible
- **Amateurs de dek hockey** : Pour suivre les performances de leurs équipes et joueurs préférés. Il est aussi possible d'entrer des prédictions.
- **Joueurs** : Pour analyser ses propres statistiques et améliorer les stratégies.

---

## Technologies Utilisées

- **Langage principal** : Python 3.13
- **Framework GUI** : PyQt6
- **Base de données** : MySQL
- **Web scraping** : Selenium, BeautifulSoup
- **Autres bibliothèques** : Requests, mysql.connector, mysql-connector-python

---

## Fonctionnalités

1. **Statistiques des joueurs** : Affichage des performances détaillées des joueurs.
2. **Classements des équipes** : Classements basés sur les performances des équipes.
3. **Comparaison** : Comparaison des statistiques entre deux équipes ou joueurs.
4. **Prédictions** : Prédictions des résultats des matchs.
5. **Gestion des comptes utilisateurs** : Création, modification et suppression de comptes.
6. **Calendriers** : Affichage de l'horraire présente et passée des matchs

---

## Degré de Complétion

Le projet est complété, mais avec certainnes fonctionnalités qui pourraient être amméliorés pour augmenter l'expérience de l'utilisateur. Par rapport au document initial, toutes les fonctionnalités prévues de base sont complètes et fonctionnelles. Bref, c'est finit, mais certaines parties nécessitent encore des améliorations ou des ajouts. Le code est un peu pèle-mèle, il pourrait être plus clean.

---

## Bogues Persistants

- **Problèmes de scraping** : Desfois, le scraping ne marche pas, il n'est pas 100% fiable.

---

## Possibles Améliorations

1. **Comparaison de joueurs** : La recherche pour la comparaison des joueurs pourrait défénitivement être améliorée, pour prendre en compte les calibres et avoir une liste qui montre les joueurs que l'on recherche.
3. **Optimisation du scraping** : Le scraping est un peu lent et non consistent.
4. **Ajout de graphiques interactifs** : pour visualiser les statistiques des équipes et des joueurs d'une façon plaisante.

---

## Procédure d'Installation

### Installation Client
- 🐍 **[Python 3.13](https://www.python.org/downloads/)**
    > Une fois que python est installé, veuillez taper ces commandes dans un terminal pour installer les modules nésséssaires :
```bash
    python3 -m venv venv
```
```bash
    venv\Scripts\activate
```
```bash
    pip install -r requirements.txt
```
```bash
    pip install pyinstaller
```

### Comment exécuter le projet:
- 🚀 **Visual Studio Code**
    > Si vous rencontrez des problèmes, vérifiez que tous les modules nécessaires sont installés et que l'environnement Python est correctement configuré.
1. Ouvrez le projet dans **Visual Studio Code**.
2. Assurez-vous que le fichier principal (par exemple, `main.py`) est ouvert dans l'éditeur.
3. Cliquez sur l'onglet **Run and Debug** dans la barre latérale ou appuyez sur `Ctrl+Shift+D` (ou `Cmd+Shift+D` sur Mac).
4. Cliquez sur **Create a launch.json file** si ce n'est pas déjà configuré.
   - Sélectionnez **Python** comme environnement.
   - Assurez-vous que le chemin du fichier principal (`main.py`) est correctement configuré dans le fichier `launch.json`.
5. Appuyez sur **F5** pour lancer le projet.