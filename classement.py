#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFontDatabase, QFont, QColor, QBrush
from PyQt6.QtCore import Qt
import bd
import utils

class Classement(QWidget):
    """Page de classement"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_classement()

    def initialiser_page_classement(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 2)

        categorie = 'B3'

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        utils.show_boutons_categories(self, 0)

        label_classement_bg = QLabel(self)
        label_classement_bg.setGeometry(20, 20, 300, 40)
        label_classement_bg.setText("Classement")
        label_classement_bg.setFont(self.jersey25_64)
        label_classement_bg.setStyleSheet("color: #2f3038")

        label_classement = QLabel(self)
        label_classement.setGeometry(22, 18, 300, 40)
        label_classement.setText("Classement")
        label_classement.setFont(self.jersey25_64)
        label_classement.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        label_parties_bg = QLabel(self)
        label_parties_bg.setGeometry(40, 100, 300, 40)
        label_parties_bg.setText("Détails des équipes")
        label_parties_bg.setFont(self.jersey25_32)
        label_parties_bg.setStyleSheet("color: #2f3038")

        label_parties = QLabel(self)
        label_parties.setGeometry(42, 98, 300, 40)
        label_parties.setText("Détails des équipes")
        label_parties.setFont(self.jersey25_32)
        label_parties.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        equipes = self.get_equipes(categorie)

        table = QTableWidget(self)
        self.populer_table(equipes, table)
        table.setStyleSheet("""background-color: #bbbcc0""")
        table.setGeometry(45, 150, 705, 243)
        table.show()

        text_recherche = utils.show_barre_recherche(self)

        text_recherche.textChanged.connect(
            lambda: self.rechercher_equipe(categorie, text_recherche.text(), table)
            if len(text_recherche.text()) >= 3 or len(text_recherche.text()) == 0
            else None
        )

    def get_equipes(self, categorie):
        """Récupère les équipes dans la base de données"""
        equipes = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_equipe, nom_equipe, position, matchs_joues, points, victoires_total, victoires_fusillades, defaites, defaites_fusillades, nulles, buts_pour, buts_contre, differentiel, points_periode, points_partie, points_penalites, points_par_match FROM equipes WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

        for ligne in cursor:
            equipes[ligne["id_equipe"]] = {
                "nom_equipe": ligne["nom_equipe"],
                "position": ligne["position"],
                "matchs_joues": ligne["matchs_joues"],
                "points": ligne["points"],
                "victoires_total": ligne["victoires_total"],
                "victoires_fusillades": ligne["victoires_fusillades"],
                "defaites": ligne["defaites"],
                "defaites_fusillades": ligne["defaites_fusillades"],
                "nulles": ligne["nulles"],
                "buts_pour": ligne["buts_pour"],
                "buts_contre": ligne["buts_contre"],
                "differentiel": ligne["differentiel"],
                "points_periode": ligne["points_periode"],
                "points_partie": ligne["points_partie"],
                "points_penalites": ligne["points_penalites"],
                "points_par_match": ligne["points_par_match"]
            }

        return equipes

    def populer_table(self, equipes, table):
        """Popule le tableau du classement"""
        table.clear()

        headers = [
            "", "", "MJ", "PTS", "V",
            "VF", "D", "DF", "N", "BP",
            "BC", "DIF", "PER", "PAR",
            "PUN", "PPG"
        ]

        headers_keys = [
            "position","nom_equipe", "matchs_joues", "points", "victoires_total",
            "victoires_fusillades", "defaites", "defaites_fusillades", "nulles",
            "buts_pour", "buts_contre", "differentiel", "points_periode",
            "points_partie", "points_penalites", "points_par_match"
        ]

        num_rows = len(equipes)
        num_cols = len(headers)

        table.setRowCount(num_rows)
        table.setColumnCount(num_cols)
        table.setHorizontalHeaderLabels(headers)

        table.horizontalHeader().setFont(self.jersey25_16)

        table.setStyleSheet("""QTableWidget::item { padding: 7px; }""")

        for row, (_, equipe_data) in enumerate(equipes.items()):
            for col, key in enumerate(headers_keys):
                item = QTableWidgetItem(str(equipe_data[key]))
                item.setFont(self.jersey25_16)
                item.setBackground(QBrush(QColor("#d9d9d9")))

                if key == "nom_equipe":
                    item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                else:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                table.setItem(row, col, item)

        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.verticalHeader().setVisible(False)

    def rechercher_equipe(self, categorie, text, table):
        """Permet de rechercher une éqquipe"""
        equipes = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_equipe, nom_equipe, position, matchs_joues, points, victoires_total, victoires_fusillades, defaites, defaites_fusillades, nulles, buts_pour, buts_contre, differentiel, points_periode, points_partie, points_penalites, points_par_match FROM equipes WHERE categorie = %(categorie)s AND nom_equipe LIKE %(text)s""",
                                {
                                    "categorie": categorie,
                                    "text": f"%{text}%"
                                })

                for ligne in cursor:
                    equipes[ligne["id_equipe"]] = {
                        "nom_equipe": ligne["nom_equipe"],
                        "position": ligne["position"],
                        "matchs_joues": ligne["matchs_joues"],
                        "points": ligne["points"],
                        "victoires_total": ligne["victoires_total"],
                        "victoires_fusillades": ligne["victoires_fusillades"],
                        "defaites": ligne["defaites"],
                        "defaites_fusillades": ligne["defaites_fusillades"],
                        "nulles": ligne["nulles"],
                        "buts_pour": ligne["buts_pour"],
                        "buts_contre": ligne["buts_contre"],
                        "differentiel": ligne["differentiel"],
                        "points_periode": ligne["points_periode"],
                        "points_partie": ligne["points_partie"],
                        "points_penalites": ligne["points_penalites"],
                        "points_par_match": ligne["points_par_match"]
                    }
        self.populer_table(equipes, table)
        table.setStyleSheet("""background-color: #bbbcc0""")