# 🍏 Création de l'éxécutable (macos):

> Dans la ligne de commande à la location du projet :

```bash
    pyinstaller --onefile --windowed main.py --add-data "resources:resources" --add-data ".env:.env"
```

## 📢 Autres informations importantes

- L'éxécutable fonctionne sur mon mac, mais je n'ai malheureusement pas été capable de le faire fonctionner sur windows.

- J'ai aussi essayé de créer un docker, mais il ne fonctionnais pas, je manque un peu d'expertise sur ce type de logiciel.

- Si vous voulez tester l'app, veuillez la démmarer avec un éditeur de texte comme VsCode en mode Debug.

- Vous devez configurer la base de données avant de partir le projet.

> Voir le README.md pour plus d'infos.
