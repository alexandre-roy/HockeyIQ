#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QLineEdit, QListWidgetItem, QFrame, QVBoxLayout
from PyQt6.QtGui import QFontDatabase, QFont, QCursor
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

        categorie = 'B2'

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

        label_parties_bg = QLabel(self)
        label_parties_bg.setGeometry(40, 100, 300, 40)
        label_parties_bg.setText("Parties à venir")
        label_parties_bg.setFont(self.jersey25_32)
        label_parties_bg.setStyleSheet("color: #2f3038")

        label_parties = QLabel(self)
        label_parties.setGeometry(42, 98, 300, 40)
        label_parties.setText("Parties à venir")
        label_parties.setFont(self.jersey25_32)
        label_parties.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        liste_parties = QListWidget(self)
        liste_parties.setGeometry(45, 150, 705, 243)
        liste_parties.setWordWrap(True)
        liste_parties.setStyleSheet("""background-color: #bbbcc0""")

        self.populer_liste(categorie, liste_parties)

        barre_recherche_bg = QLabel(self)
        barre_recherche_bg.setGeometry(470, 100, 280, 40)
        barre_recherche_bg.setStyleSheet("""background-color: #bbbcc0""")

        barre_recherche = QLineEdit(self)
        barre_recherche.setGeometry(495, 105, 250, 30)
        barre_recherche.setStyleSheet("""background-color: #d9d9d9;
                                        border-radius: 0px;""")
        barre_recherche.setFont(self.jersey25_16)
        barre_recherche.setPlaceholderText("RECHERCHE")

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

    def populer_liste(self, categorie, liste):
        """Popule la liste du calendrier"""
        parties = self.get_parties(categorie)
        label = None

        for _, p in parties.items():
            if p['score_local'] is None:
                label = QLabel(f"{p['equipe_visiteur']} @ {p['equipe_local']} - ({p['date']} {p['heure']})")

                frame = QFrame()
                frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")

                layout = QVBoxLayout(frame)
                layout.setContentsMargins(0, 10, 0, 10)
                layout.setSpacing(0)

                label.setFont(self.jersey25_16)
                layout.addWidget(label)

                frame.setLayout(layout)
                frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

                item = QListWidgetItem()
                item.setSizeHint(frame.sizeHint())

                liste.addItem(item)
                liste.setItemWidget(item, frame)


