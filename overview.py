#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QPushButton, QFrame, QVBoxLayout
from PyQt6.QtGui import QFontDatabase, QFont, QCursor
from PyQt6.QtCore import Qt
import bd
import utils

class Overview(QWidget):
    """Page d'overview"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_overview()

    def initialiser_page_overview(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 3)

        categorie = 'B2'

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        self.btn_b2_bg = QPushButton(self)
        self.btn_b2 = QPushButton(self)
        self.btn_b3_bg = QPushButton(self)
        self.btn_b3 = QPushButton(self)

        self.initialiser_page(categorie)

        label_sommaire_bg = QLabel(self)
        label_sommaire_bg.setGeometry(20, 20, 300, 40)
        label_sommaire_bg.setText("Sommaire")
        label_sommaire_bg.setFont(self.jersey25_64)
        label_sommaire_bg.setStyleSheet("color: #2f3038")


        label_sommaire = QLabel(self)
        label_sommaire.setGeometry(22, 18, 300, 40)
        label_sommaire.setText("Sommaire")
        label_sommaire.setFont(self.jersey25_64)
        label_sommaire.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        label_equipes_bg = QLabel(self)
        label_equipes_bg.setGeometry(40, 100, 300, 40)
        label_equipes_bg.setText("Top 5 équipes")
        label_equipes_bg.setFont(self.jersey25_32)
        label_equipes_bg.setStyleSheet("color: #2f3038")

        label_equipes = QLabel(self)
        label_equipes.setGeometry(42, 98, 300, 40)
        label_equipes.setText("Top 5 équipes")
        label_equipes.setFont(self.jersey25_32)
        label_equipes.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        label_joueurs_bg = QLabel(self)
        label_joueurs_bg.setGeometry(405, 100, 300, 40)
        label_joueurs_bg.setText("Top 5 joueurs")
        label_joueurs_bg.setFont(self.jersey25_32)
        label_joueurs_bg.setStyleSheet("color: #2f3038")

        label_joueurs = QLabel(self)
        label_joueurs.setGeometry(407, 98, 300, 40)
        label_joueurs.setText("Top 5 joueurs")
        label_joueurs.setFont(self.jersey25_32)
        label_joueurs.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        list_equipes = QListWidget(self)
        list_equipes.setGeometry(45, 150, 340, 243)
        list_equipes.setWordWrap(True)
        list_equipes.setStyleSheet("""background-color: #bbbcc0""")

        list_joueurs = QListWidget(self)
        list_joueurs.setGeometry(410, 150, 340, 243)
        list_joueurs.setWordWrap(True)
        list_joueurs.setStyleSheet("""background-color: #bbbcc0""")

        self.populer_listes(categorie, list_equipes, list_joueurs)


    def initialiser_page(self, categorie):
        """Initialise la page basé sur la catégorie passée en paramètres"""

        self.btn_b2_bg.setGeometry(670, 21, 40, 43)
        self.btn_b2_bg.setFont(self.jersey25_32)
        self.btn_b2_bg.setStyleSheet("background-color: #f2bd41;"
                                    "border-radius: 0px;")

        self.btn_b2.setGeometry(667, 24, 46, 37)
        self.btn_b2.setFont(self.jersey25_32)
        self.btn_b2.setStyleSheet("background-color:#f2bd41;"
                                    "border-radius: 0px;"
                                    "color: #2F3038;")
        self.btn_b2.setText('B2')

        self.btn_b3_bg.setGeometry(730, 21, 40, 43)
        self.btn_b3_bg.setFont(self.jersey25_32)
        self.btn_b3_bg.setStyleSheet("background-color: #bbbcc0;"
                                    "border-radius: 0px;")
        self.btn_b3_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.btn_b3.setGeometry(727, 24, 46, 37)
        self.btn_b3.setFont(self.jersey25_32)
        self.btn_b3.setStyleSheet("background-color:#bbbcc0;"
                                    "border-radius: 0px;"
                                    "color: #2F3038;")
        self.btn_b3.setText("B3")
        self.btn_b3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        if categorie == 'B2':
            self.btn_b2_bg.clicked.connect(self.btn_b2_click)
            self.btn_b2.clicked.connect(self.btn_b2_click)

            self.btn_b3_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.btn_b3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        else:
            self.btn_b3_bg.clicked.connect(self.btn_b3_click)
            self.btn_b3.clicked.connect(self.btn_b3_click)

            self.btn_b2_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.btn_b2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def get_equipes(self, categorie):
        """Récupère les équipes dans la base de données"""
        equipes = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT nom_equipe, matchs_joues, points, victoires_total,
                               defaites, nulles FROM equipes WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

                for ligne in cursor:
                    equipes[ligne["nom_equipe"]] = {
                        "nom_equipe": ligne["nom_equipe"],
                        "matchs_joues": ligne["matchs_joues"],
                        "points": ligne["points"],
                        "victoires_total": ligne["victoires_total"],
                        "defaites": ligne["defaites"],
                        "nulles": ligne["nulles"]
                    }
        return equipes

    def get_joueurs(self, categorie):
        """Récupère les joueurs dans la base de données"""
        joueurs = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT nom, equipe, matchs_joues, points FROM joueurs WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

                for ligne in cursor:
                    joueurs[ligne["nom"]] = {
                        "nom" : ligne["nom"],
                        "equipe": ligne["equipe"],
                        "matchs_joues": ligne["matchs_joues"],
                        "points": ligne["points"]
                    }
        return joueurs

    def populer_listes(self, categorie, list_equipes, list_joueurs):
        """Popule les listes du sommaire"""
        equipes = self.get_equipes(categorie)

        position = 0
        for _, e in equipes.items():
            position += 1

            frame = QFrame()
            frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")

            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 10, 0, 10)
            layout.setSpacing(0)

            label = QLabel(f"{position}. {e['nom_equipe']} - {e['points']} PTS ({e['victoires_total']} - {e['defaites']} - {e['nulles']})")
            label.setFont(self.jersey25_16)
            layout.addWidget(label)

            frame.setLayout(layout)
            frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            item = QListWidgetItem()
            item.setSizeHint(frame.sizeHint())

            list_equipes.addItem(item)
            list_equipes.setItemWidget(item, frame)

            if position == 5:
                break

        joueurs = self.get_joueurs(categorie)

        position = 0
        for _, j in joueurs.items():
            position += 1

            frame = QFrame()
            frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")

            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 10, 0, 10)
            layout.setSpacing(0)

            label = QLabel(f"{position}. {j['nom']} - {j['equipe']} - {j['points']} PTS ({j['matchs_joues']} MJ)")
            label.setFont(self.jersey25_16)
            layout.addWidget(label)

            frame.setLayout(layout)
            frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            item = QListWidgetItem()
            item.setSizeHint(frame.sizeHint())

            list_joueurs.addItem(item)
            list_joueurs.setItemWidget(item, frame)

            if position == 5:
                break

    def btn_b2_click(self):
        """Action lors du click sur le bouton B2"""
        print("B2")

    def btn_b3_click(self):
        """Action lors du click sur le bouton B3"""
        pass
