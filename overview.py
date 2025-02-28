#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QPushButton
from PyQt6.QtGui import QFontDatabase, QFont, QBrush, QColor, QCursor
from PyQt6.QtCore import Qt
import bd

class Overview(QWidget):
    """Page d'overview"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_overview()

    def initialiser_page_overview(self):
        """Interface graphique"""
        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_40 = QFont("jersey 25", 40)
        self.jersey25_32 = QFont("jersey 25", 32)
        self.jersey25_16 = QFont("jersey 25", 16)

        categorie = 'B2'

        self.initialiser_page(categorie)

        label_sommaire_bg = QLabel(self)
        label_sommaire_bg.setGeometry(20, 10, 300, 40)
        label_sommaire_bg.setText("Sommaire")
        label_sommaire_bg.setFont(self.jersey25_40)
        label_sommaire_bg.setStyleSheet("color: #2f3038")

        label_sommaire = QLabel(self)
        label_sommaire.setGeometry(21, 9, 300, 40)
        label_sommaire.setText("Sommaire")
        label_sommaire.setFont(self.jersey25_40)
        label_sommaire.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        label_parties_bg = QLabel(self)
        label_parties_bg.setGeometry(50, 50, 300, 40)
        label_parties_bg.setText("Meilleures équipes")
        label_parties_bg.setFont(self.jersey25_32)
        label_parties_bg.setStyleSheet("color: #2f3038")

        label_parties = QLabel(self)
        label_parties.setGeometry(51, 49, 300, 40)
        label_parties.setText("Meilleures équipes")
        label_parties.setFont(self.jersey25_32)
        label_parties.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        parties_b2 = self.get_parties(categorie)

        list_equipes = QListWidget(self)
        list_equipes.setGeometry(50, 100, 350, 350)
        list_equipes.setWordWrap(True)
        list_equipes.setStyleSheet("""background-color: #bbbcc0""")

        for _, p in parties_b2.items():
            item_text = f"""{p['nom_equipe']} - {p['points']} points, {p['victoires_total']}
                         victoires, {p['defaites']} défaites, {p['nulles']} nulles"""
            item = QListWidgetItem(item_text)

            item.setBackground(QBrush(QColor("#d9d9d9")))
            item.setFont(self.jersey25_16)

            list_equipes.addItem(item)


    def initialiser_page(self, categorie):
        """Initialise la page basé sur la catégorie passée en paramètres"""
        btn_b2_bg = QPushButton(self)
        btn_b2_bg.setGeometry(670, 16, 40, 40)
        btn_b2_bg.setFont(self.jersey25_32)
        btn_b2_bg.setStyleSheet("background-color: #f2bd41;"
                                    "border-radius: 0px;")

        btn_b2 = QPushButton(self)
        btn_b2.setGeometry(667, 19, 46, 34)
        btn_b2.setFont(self.jersey25_32)
        btn_b2.setStyleSheet("background-color:#f2bd41;"
                                    "border-radius: 0px;"
                                    "color: #2F3038;")
        btn_b2.setText(categorie)

        btn_b3_bg = QPushButton(self)
        btn_b3_bg.setGeometry(730, 16, 40, 40)
        btn_b3_bg.setFont(self.jersey25_32)
        btn_b3_bg.setStyleSheet("background-color: #bbbcc0;"
                                    "border-radius: 0px;")
        btn_b3_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        btn_b3 = QPushButton(self)
        btn_b3.setGeometry(727, 19, 46, 34)
        btn_b3.setFont(self.jersey25_32)
        btn_b3.setStyleSheet("background-color:#bbbcc0;"
                                    "border-radius: 0px;"
                                    "color: #2F3038;")
        btn_b3.setText("B3")
        btn_b3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def get_parties(self, categorie):
        """Récupère les parties dans la base de données"""
        parties = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT nom_equipe, matchs_joues, points, victoires_total,
                               defaites, nulles FROM equipes WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

                for ligne in cursor:
                    parties[ligne["nom_equipe"]] = {
                        "nom_equipe": ligne["nom_equipe"],
                        "matchs_joues": ligne["matchs_joues"],
                        "points": ligne["points"],
                        "victoires_total": ligne["victoires_total"],
                        "defaites": ligne["defaites"],
                        "nulles": ligne["nulles"]
                    }

        return parties
