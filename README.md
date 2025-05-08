# HockeyIQ

## 📌 Nature et Objectif du Projet

HockeyIQ est une application interactive conçue pour les amateurs de dek hockey et les joueurs. Elle vise à fournir des statistiques détaillées, des classements, des comparaisons d'équipes et de joueurs, ainsi que des prédictions basées sur des données réelles. L'objectif est d'offrir une plateforme intuitive pour analyser les performances des équipes et des joueurs, tout en permettant aux utilisateurs de suivre les matchs et de gérer leurs comptes.

---

## 🎯 Clientèle Cible
- **Amateurs de dek hockey** : Pour suivre les performances de leurs équipes et joueurs préférés. Il est aussi possible d'entrer des prédictions.
- **Joueurs** : Pour analyser leurs propres statistiques et améliorer leurs stratégies.

---

## 🛠️ Technologies Utilisées

- **Langage principal** : Python 3.13
- **Framework GUI** : PyQt6
- **Base de données** : MySQL
- **Web scraping** : Selenium, BeautifulSoup
- **Autres bibliothèques** : Requests, mysql.connector, mysql-connector-python

---

## ✅ Fonctionnalités

1. **Statistiques des joueurs** : Affichage des performances détaillées des joueurs.
2. **Classements des équipes** : Classements basés sur les performances des équipes.
3. **Comparaison** : Comparaison des statistiques entre deux équipes ou joueurs.
4. **Prédictions** : Prédictions des résultats des matchs.
5. **Gestion des comptes utilisateurs** : Création, modification et suppression de comptes.
6. **Calendriers** : Affichage de l'horaire présent et passé des matchs.

---

## 🚧 Degré de Complétion

Le projet est complété, mais avec certaines fonctionnalités qui pourraient être améliorées pour augmenter l'expérience de l'utilisateur. Par rapport au document initial, toutes les fonctionnalités prévues de base sont complètes et fonctionnelles. Bref, c'est fini, mais certaines parties nécessitent encore des améliorations ou des ajouts. Le code est un peu pêle-mêle, il pourrait être plus propre.

---

## 🐞 Bogues Persistants

- **Problèmes de scraping** : Parfois, le scraping ne fonctionne pas, il n'est pas 100 % fiable.

---

## 🔧 Possibles Améliorations

1. **Comparaison de joueurs** : La recherche pour la comparaison des joueurs pourrait définitivement être améliorée, pour prendre en compte les calibres et avoir une liste qui montre les joueurs recherchés.
2. **Optimisation du scraping** : Le scraping est un peu lent et non consistant.
3. **Ajout de graphiques interactifs** : Pour visualiser les statistiques des équipes et des joueurs de manière plaisante.
4. **Base de données et exécutable** : L'exécutable du projet fonctionne uniquement quand l'utilisateur a déjà effectué le setup de la base de données. J'aurais aimé faire en sorte que tout fonctionne en un clic, mais j'ai rencontré plusieurs problèmes au cours de la fabrication de l'exécutable du projet.

---

## 📦 Procédure d'Installation

### Langage de programmation et modules
- **[Python 3.13](https://www.python.org/downloads/)**
    > Une fois que Python est installé, veuillez taper ces commandes dans un terminal pour installer les modules nécessaires :
```bash
    pip install -r requirements.txt
```
```bash
    pip install pyinstaller
```
```bash
    pyinstaller --onefile --windowed main.py --add-data "resources:resources"
```

### Configuration de la base de données / connexion
- **[MySQL](https://www.mysql.com/downloads/)**
    > Une fois que la partie précédente est terminée, veuillez passer à ces étapes pour la configuration de la base de données :
1. Changez les variables d'environnement dans le fichier `.env`, pour qu'elles correspondent à vos paramètres de gestionnaire de base de données.
2. Veuillez **copier-coller** les deux scripts dans le dossier `Data` dans une console MySQL.

### Comment exécuter le projet :
-  **[Visual Studio Code](https://code.visualstudio.com/download)**
    > Si vous rencontrez des problèmes, vérifiez que tous les modules nécessaires sont installés et que l'environnement Python est correctement configuré.
1. Ouvrez le projet dans **Visual Studio Code**.
2. Assurez-vous que le fichier principal (`main.py`) est ouvert dans l'éditeur.
3. Cliquez sur l'onglet **Run and Debug** dans la barre latérale ou appuyez sur `Ctrl+Shift+D` (ou `Cmd+Shift+D` sur Mac).
4. Cliquez sur **Create a launch.json file** si ce n'est pas déjà configuré.
   - Sélectionnez **Python** comme environnement.
   - Assurez-vous que le chemin du fichier principal (`main.py`) est correctement configuré dans le fichier `launch.json`.
5. Appuyez sur **F5** pour lancer le projet.