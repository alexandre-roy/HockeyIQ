#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFontDatabase, QFont, QColor, QBrush
from PyQt6.QtCore import Qt
import bd
import utils

class Statistiques(QWidget):
    """Page de statistiques"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_statistiques()

    def initialiser_page_statistiques(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 1)

        categorie = 'B2'

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        utils.show_boutons_categories(self, 0)

        label_classement_bg = QLabel(self)
        label_classement_bg.setGeometry(20, 20, 300, 40)
        label_classement_bg.setText("Statistiques")
        label_classement_bg.setFont(self.jersey25_64)
        label_classement_bg.setStyleSheet("color: #2f3038")

        label_classement = QLabel(self)
        label_classement.setGeometry(22, 18, 300, 40)
        label_classement.setText("Statistiques")
        label_classement.setFont(self.jersey25_64)
        label_classement.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        label_parties_bg = QLabel(self)
        label_parties_bg.setGeometry(40, 100, 300, 40)
        label_parties_bg.setText("Détails des joueurs")
        label_parties_bg.setFont(self.jersey25_32)
        label_parties_bg.setStyleSheet("color: #2f3038")

        label_parties = QLabel(self)
        label_parties.setGeometry(42, 98, 300, 40)
        label_parties.setText("Détails des joueurs")
        label_parties.setFont(self.jersey25_32)
        label_parties.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        joueurs = self.get_joueurs(categorie)

        table = QTableWidget(self)
        self.populer_table(joueurs, table)
        table.setStyleSheet("""background-color: #bbbcc0""")
        table.setGeometry(45, 150, 705, 243)
        table.show()

        text_recherche = utils.show_barre_recherche(self)

        text_recherche.textChanged.connect(
            lambda: self.rechercher_joueur(categorie, text_recherche.text(), table)
            if len(text_recherche.text()) >= 3 or len(text_recherche.text()) == 0
            else None
        )

    def get_joueurs(self, categorie):
        """Récupère les joueurs dans la base de données"""
        joueurs = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_joueur, nom, equipe, matchs_joues, buts, passes, points, minutes_penalite, points_par_match, buts_avantage_numerique, points_avantage_numerique, buts_inferiorite_numerique, points_inferiorite_numerique, buts_gagnants, position FROM joueurs WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

        for ligne in cursor:
            joueurs[ligne["id_joueur"]] = {
                "nom": ligne["nom"],
                "equipe": ligne["equipe"],
                "position": ligne["position"],
                "matchs_joues": ligne["matchs_joues"],
                "buts": ligne["buts"],
                "passes": ligne["passes"],
                "points": ligne["points"],
                "minutes_penalite": ligne["minutes_penalite"],
                "points_par_match": ligne["points_par_match"],
                "buts_avantage_numerique": ligne["buts_avantage_numerique"],
                "points_avantage_numerique": ligne["points_avantage_numerique"],
                "buts_inferiorite_numerique": ligne["buts_inferiorite_numerique"],
                "points_inferiorite_numerique": ligne["points_inferiorite_numerique"],
                "buts_gagnants": ligne["buts_gagnants"]
                }

        return joueurs

    def populer_table(self, joueurs, table):
        """Popule le tableau du classement"""
        table.clear()

        headers = [
        "", "", "Équipe", "MJ", "B", "A", "PTS", "PUN",
        "PPG", "BAN", "PAN", "BIN", "PIN", "BG"
    ]

        headers_keys = [
        "position", "nom", "equipe", "matchs_joues", "buts",
        "passes", "points", "minutes_penalite", "points_par_match",
        "buts_avantage_numerique", "points_avantage_numerique",
        "buts_inferiorite_numerique", "points_inferiorite_numerique",
        "buts_gagnants"
    ]

        num_rows = len(joueurs)
        num_cols = len(headers)

        table.setRowCount(num_rows)
        table.setColumnCount(num_cols)
        table.setHorizontalHeaderLabels(headers)

        table.horizontalHeader().setFont(self.jersey25_16)

        table.setStyleSheet("""QTableWidget::item { padding: 7px; }""")

        for row, (_, equipe_data) in enumerate(joueurs.items()):
            for col, key in enumerate(headers_keys):
                item = QTableWidgetItem(str(equipe_data[key]))
                item.setFont(self.jersey25_16)
                item.setBackground(QBrush(QColor("#d9d9d9")))

                if key == "nom":
                    item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                else:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                table.setItem(row, col, item)

        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.verticalHeader().setVisible(False)

    def rechercher_joueur(self, categorie, text, table):
        """Permet de rechercher un joueur"""
        joueurs = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_joueur, nom, equipe, position, matchs_joues, buts, passes,
                                        points, minutes_penalite, points_par_match, buts_avantage_numerique,
                                        points_avantage_numerique, buts_inferiorite_numerique,
                                        points_inferiorite_numerique, buts_gagnants
                                FROM joueurs
                                WHERE categorie = %(categorie)s
                                AND nom LIKE %(text)s""",
                            {
                                "categorie": categorie,
                                "text": f"%{text}%"
                            })

                for ligne in cursor:
                    joueurs[ligne["id_joueur"]] = {
                        "nom": ligne["nom"],
                        "equipe": ligne["equipe"],
                        "position": ligne["position"],
                        "matchs_joues": ligne["matchs_joues"],
                        "buts": ligne["buts"],
                        "passes": ligne["passes"],
                        "points": ligne["points"],
                        "minutes_penalite": ligne["minutes_penalite"],
                        "points_par_match": ligne["points_par_match"],
                        "buts_avantage_numerique": ligne["buts_avantage_numerique"],
                        "points_avantage_numerique": ligne["points_avantage_numerique"],
                        "buts_inferiorite_numerique": ligne["buts_inferiorite_numerique"],
                        "points_inferiorite_numerique": ligne["points_inferiorite_numerique"],
                        "buts_gagnants": ligne["buts_gagnants"]
                    }

        self.populer_table(joueurs, table)
        table.setStyleSheet("""background-color: #bbbcc0""")
