#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFontDatabase, QFont, QCursor, QIcon
from PyQt6.QtCore import Qt
import bd
import utils


class Calendrier(QWidget):
    """Page d'overview"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_calendrier()

    def initialiser_page_calendrier(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 0)

        self.categorie = 'B2'
        self.counter_all_games = 0

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        utils.show_boutons_categories(self, 0)

        label_calendrier_bg = QLabel(self)
        label_calendrier_bg.setGeometry(20, 20, 300, 40)
        label_calendrier_bg.setText("Calendrier")
        label_calendrier_bg.setFont(self.jersey25_64)
        label_calendrier_bg.setStyleSheet("color: #2f3038")

        label_calendrier = QLabel(self)
        label_calendrier.setGeometry(22, 18, 300, 40)
        label_calendrier.setText("Calendrier")
        label_calendrier.setFont(self.jersey25_64)
        label_calendrier.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        self.label_parties_bg = QLabel(self)
        self.label_parties_bg.setGeometry(40, 100, 300, 40)
        self.label_parties_bg.setText("Parties à venir")
        self.label_parties_bg.setFont(self.jersey25_32)
        self.label_parties_bg.setStyleSheet("color: #2f3038")

        self.label_parties = QLabel(self)
        self.label_parties.setGeometry(42, 98, 300, 40)
        self.label_parties.setText("Parties à venir")
        self.label_parties.setFont(self.jersey25_32)
        self.label_parties.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        self.liste_parties = QListWidget(self)
        self.liste_parties.setGeometry(45, 150, 705, 243)
        self.liste_parties.setWordWrap(True)
        self.liste_parties.setStyleSheet("""background-color: #bbbcc0""")

        parties = self.get_parties(self.categorie)

        self.populer_liste(parties, self.liste_parties, False)

        self.text_recherche = utils.show_barre_recherche(self)

        self.text_recherche.textChanged.connect(
            lambda: self.rechercher_match(self.categorie, self.text_recherche.text(), self.liste_parties)
            if len(self.text_recherche.text()) >= 3 or len(self.text_recherche.text()) == 0
            else None
        )

        bg_noir = QPushButton(self)
        bg_noir_2 = QPushButton(self)
        self.bg_fgg = QPushButton(self)
        self.bg_fgg_2 = QPushButton(self)

        bg_noir.setGeometry(434, 107, 30, 33)
        bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2.setGeometry(431, 110, 36, 27)
        bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.bg_fgg.setGeometry(437, 104, 30, 33)
        self.bg_fgg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.bg_fgg_2.setGeometry(434, 107, 36, 27)
        self.bg_fgg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.bg_fgg_2.setFont(self.jersey25_32)
        self.bg_fgg_2.setIcon(QIcon("resources/images/switch.svg"))
        self.bg_fgg_2.setIconSize(self.bg_fgg_2.size())
        self.bg_fgg_2.setToolTip("Filtrer les parties")
        self.bg_fgg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bg_fgg_2.clicked.connect(lambda: self.populer_liste(parties, self.liste_parties, True))
        self.bg_fgg_2.clicked.connect(lambda: self.toggle_parties_label(self.label_parties, self.label_parties_bg, parties, self.liste_parties))

    def toggle_parties_label(self, label_parties, label_parties_bg, parties, liste_parties):
        """Change le label pour le titre"""
        if label_parties.text() == "Parties à venir":
            label_parties.setText("Toutes les parties")
            label_parties_bg.setText("Toutes les parties")
            self.bg_fgg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
            self.bg_fgg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
            parties = self.get_parties(self.categorie)
            self.populer_liste(parties, liste_parties, True)
        else:
            label_parties.setText("Parties à venir")
            label_parties_bg.setText("Parties à venir")
            self.bg_fgg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
            self.bg_fgg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
            parties = self.get_parties(self.categorie)
            self.populer_liste(parties, liste_parties, False)

    def get_parties(self, categorie):
        """Récupère les joueurs dans la base de données"""
        parties = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_partie, equipe_visiteur, equipe_local, score_visiteur, score_local, fusillades, date, heure FROM parties WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

                for ligne in cursor:
                    parties[ligne["id_partie"]] = {
                        "equipe_visiteur": ligne["equipe_visiteur"],
                        "equipe_local": ligne["equipe_local"],
                        "score_visiteur": ligne["score_visiteur"],
                        "score_local": ligne["score_local"],
                        "fusillades": ligne["fusillades"],
                        "date": ligne["date"],
                        "heure": ligne["heure"]
                    }
        return parties

    def populer_liste(self, parties, liste, is_all):
        """Popule la liste du calendrier"""
        liste.clear()

        for _, p in parties.items():
            if is_all is False and p['score_local'] is not None:
                continue

            if p['score_local'] is None:
                if p["equipe_visiteur"] == "Aucun résultat":
                    match_label = QLabel(f"{p['equipe_visiteur']}")
                else:
                    match_label = QLabel(f"{p['equipe_visiteur']} @ {p['equipe_local']}")

                date_label = QLabel(f"{p['date']} {p['heure']}")
            else:
                match_label = QLabel(f"{p['equipe_visiteur']} ({p['score_visiteur']}) @ {p['equipe_local']} ({p['score_local']})")
                date_label = QLabel(f"{p['date']} {p['heure']} ")

            frame = QFrame()
            frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")

            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 10, 0, 10)
            layout.setSpacing(0)

            h_layout = QHBoxLayout()
            h_layout.addWidget(match_label)
            h_layout.addStretch()
            h_layout.addWidget(date_label)

            match_label.setFont(self.jersey25_16)
            date_label.setFont(self.jersey25_16)

            layout.addLayout(h_layout)

            frame.setLayout(layout)
            frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            item = QListWidgetItem()
            item.setSizeHint(frame.sizeHint())

            liste.addItem(item)
            liste.setItemWidget(item, frame)

    def rechercher_match(self, categorie, text, liste_parties):
        """Permet de rechercher une partie"""
        parties = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_partie, equipe_visiteur, equipe_local, score_visiteur, score_local, fusillades, date, heure FROM parties WHERE categorie = %(categorie)s AND (equipe_visiteur LIKE %(text)s OR equipe_local LIKE %(text)s)""",
                                {
                                    "categorie": categorie,
                                    "text": f"%{text}%"
                                })

                for ligne in cursor:
                    parties[ligne["id_partie"]] = {
                        "equipe_visiteur": ligne["equipe_visiteur"],
                        "equipe_local": ligne["equipe_local"],
                        "score_visiteur": ligne["score_visiteur"],
                        "score_local": ligne["score_local"],
                        "fusillades": ligne["fusillades"],
                        "date": ligne["date"],
                        "heure": ligne["heure"]
                    }

                if not parties:
                    parties["0"] = {
                        "equipe_visiteur": "Aucun résultat",
                        "equipe_local": "",
                        "score_visiteur": None,
                        "score_local": None,
                        "fusillades": None,
                        "date": "",
                        "heure": ""
                    }

        self.populer_liste(parties, liste_parties, True)
