#pylint: disable = no-name-in-module
#pylint: disable = attribute-defined-outside-init

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QFrame, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFontDatabase, QFont, QCursor, QIcon, QPixmap
from PyQt6.QtCore import Qt
import bd
import utils

class Comparaison(QWidget):
    """Page d'overview"""
    def __init__(self, main_window, equipe_1, equipe_2):
        super().__init__()
        self.main_window = main_window
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2

        self.initialiser_page_comparaison()
        self.montrer_page_equipes()

    def initialiser_page_comparaison(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 4)

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        label_comparaison_bg = QLabel(self)
        label_comparaison_bg.setGeometry(20, 20, 300, 40)
        label_comparaison_bg.setText("Face à face")
        label_comparaison_bg.setFont(self.jersey25_64)
        label_comparaison_bg.setStyleSheet("color: #2f3038")


        label_comparaison = QLabel(self)
        label_comparaison.setGeometry(22, 18, 300, 40)
        label_comparaison.setText("Face à face")
        label_comparaison.setFont(self.jersey25_64)
        label_comparaison.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        self.label_mode_bg = QLabel(self)
        self.label_mode_bg.setGeometry(40, 100, 350, 40)
        self.label_mode_bg.setFont(self.jersey25_32)
        self.label_mode_bg.setStyleSheet("color: #2f3038")

        self.label_mode = QLabel(self)
        self.label_mode.setGeometry(42, 98, 350, 40)
        self.label_mode.setFont(self.jersey25_32)
        self.label_mode.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        self.equipes_bg_noir = QPushButton(self)
        self.equipes_bg_noir_2 = QPushButton(self)
        self.equipes_bg_fg = QPushButton(self)
        self.equipes_bg_fg_2 = QPushButton(self)

        self.equipes_bg_noir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.equipes_bg_noir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.equipes_bg_fg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.equipes_bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.equipes_bg_fg_2.setToolTip("Équipes")

        self.equipes_bg_noir.setGeometry(670, 21, 40, 43)
        self.equipes_bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.equipes_bg_noir_2.setGeometry(667, 24, 46, 37)
        self.equipes_bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.equipes_bg_fg.setGeometry(673, 18, 40, 43)
        self.equipes_bg_fg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

        self.equipes_bg_fg_2.setGeometry(670, 21, 46, 37)
        self.equipes_bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
        self.equipes_bg_fg_2.setIcon(QIcon("resources/images/equipes.svg"))
        self.equipes_bg_fg_2.setIconSize(self.equipes_bg_fg_2.size())
        self.equipes_bg_fg_2.clicked.connect(self.btn_equipes_click)

        self.joueurs_bg_noir = QPushButton(self)
        self.joueurs_bg_noir_2 = QPushButton(self)
        self.joueurs_bg_fg = QPushButton(self)
        self.joueurs_bg_fg_2 = QPushButton(self)

        self.joueurs_bg_noir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.joueurs_bg_noir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.joueurs_bg_fg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.joueurs_bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.joueurs_bg_fg_2.setToolTip("Joueurs")

        self.joueurs_bg_noir.setGeometry(730, 21, 40, 43)
        self.joueurs_bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.joueurs_bg_noir_2.setGeometry(727, 24, 46, 37)
        self.joueurs_bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.joueurs_bg_fg.setGeometry(733, 18, 40, 43)
        self.joueurs_bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.joueurs_bg_fg_2.setGeometry(730, 21, 46, 37)
        self.joueurs_bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.joueurs_bg_fg_2.setIcon(QIcon("resources/images/joueur.svg"))
        self.joueurs_bg_fg_2.setIconSize(self.joueurs_bg_fg_2.size())
        self.joueurs_bg_fg_2.clicked.connect(self.btn_joueurs_click)

        self.list_equipe1 = QListWidget(self)
        self.list_equipe1.setGeometry(45, 150, 340, 203)
        self.list_equipe1.setWordWrap(True)
        self.list_equipe1.setStyleSheet("""background-color: #bbbcc0""")

        self.list_equipe2 = QListWidget(self)
        self.list_equipe2.setGeometry(410, 150, 340, 203)
        self.list_equipe2.setWordWrap(True)
        self.list_equipe2.setStyleSheet("""background-color: #bbbcc0""")

    def rechercher_joueur(self, text, liste):
        """Permet de rechercher un joueur"""
        joueurs = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_joueur, nom, equipe, position, matchs_joues, buts, passes,
                                        points, minutes_penalite, points_par_match, buts_avantage_numerique,
                                        points_avantage_numerique, buts_inferiorite_numerique,
                                        points_inferiorite_numerique, buts_gagnants
                                FROM joueurs
                                WHERE nom LIKE %(text)s""",
                            {
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
        self.populer_liste_joueurs(joueurs, liste)

    def populer_liste_joueurs(self, joueurs, liste):
        """Popule la liste de comparaison des joueurs"""
        liste.clear()

        if joueurs:
            _, first_player_data = next(iter(joueurs.items()))

            joueur_name = QListWidgetItem(f"{first_player_data['nom']}")
            joueur_name.setFont(self.jersey25_32)
            joueur_name.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            liste.addItem(joueur_name)

            stats_to_compare = [
                ("Matchs Joués", "matchs_joues"),
                ("Buts", "buts"),
                ("Passes", "passes"),
                ("Points", "points"),
                ("Minutes de Pénalité", "minutes_penalite"),
                ("Points par Match", "points_par_match"),
                ("Buts Avantage Numérique", "buts_avantage_numerique"),
                ("Points Avantage Numérique", "points_avantage_numerique"),
                ("Buts Infériorité Numérique", "buts_inferiorite_numerique"),
                ("Points Infériorité Numérique", "points_inferiorite_numerique"),
                ("Buts Gagnants", "buts_gagnants"),
            ]

            for label, key in stats_to_compare:
                frame = QFrame()
                frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px; }")
                layout = QHBoxLayout(frame)
                layout.setContentsMargins(10, 5, 10, 5)

                stat_value = first_player_data.get(key, 0)
                stat_label = QLabel(f"{label}: {stat_value}")
                stat_label.setFont(self.jersey25_16)

                layout.addWidget(stat_label)
                frame.setLayout(layout)

                item = QListWidgetItem()
                item.setSizeHint(frame.sizeHint())
                liste.addItem(item)
                liste.setItemWidget(item, frame)

    def populer_listes_comparaison(self, list_equipe1, list_equipe2):
        """Popule les listes de comparaison avec les stats des équipes"""
        list_equipe1.clear()
        list_equipe2.clear()

        equipe1_stats = self.get_equipe(self.equipe_1)
        equipe2_stats = self.get_equipe(self.equipe_2)

        team_name_item1 = QListWidgetItem(f"{self.equipe_1}")
        team_name_item1.setFont(self.jersey25_32)
        team_name_item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        list_equipe1.addItem(team_name_item1)

        team_name_item2 = QListWidgetItem(f"{self.equipe_2}")
        team_name_item2.setFont(self.jersey25_32)
        team_name_item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        list_equipe2.addItem(team_name_item2)

        stats_to_compare = [
            ("Position", "position", "lower"),
            ("Matchs Joués", "matchs_joues", "lower"),
            ("Points", "points", "higher"),
            ("Victoires Totales", "victoires_total", "higher"),
            ("Victoires Fusillades", "victoires_fusillades", "higher"),
            ("Défaites", "defaites", "lower"),
            ("Défaites Fusillades", "defaites_fusillades", "lower"),
            ("Nulles", "nulles", "higher"),
            ("Buts Pour", "buts_pour", "higher"),
            ("Buts Contre", "buts_contre", "lower"),
            ("Différentiel", "differentiel", "higher"),
            ("Points Période", "points_periode", "higher"),
            ("Points Partie", "points_partie", "higher"),
            ("Points Pénalités", "points_penalites", "higher"),
            ("Points par Match", "points_par_match", "higher"),
        ]

        for label, key, comparison in stats_to_compare:
            frame1 = QFrame()
            frame1.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px; }")
            layout1 = QHBoxLayout(frame1)
            layout1.setContentsMargins(10, 5, 10, 5)

            frame2 = QFrame()
            frame2.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px; }")
            layout2 = QHBoxLayout(frame2)
            layout2.setContentsMargins(10, 5, 10, 5)

            stat1 = equipe1_stats.get(key, 0)
            stat2 = equipe2_stats.get(key, 0)

            label1 = QLabel(f"{label}: {stat1}")
            label2 = QLabel(f"{label}: {stat2}")

            if comparison == "higher":
                if stat1 > stat2:
                    label1.setStyleSheet("color: #2bb537;")
                elif stat2 > stat1:
                    label2.setStyleSheet("color: #2bb537;")
            elif comparison == "lower":
                if stat1 < stat2:
                    label1.setStyleSheet("color: #2bb537;")
                elif stat2 < stat1:
                    label2.setStyleSheet("color: #2bb537;")

            label1.setFont(self.jersey25_16)
            label2.setFont(self.jersey25_16)

            layout1.addWidget(label1)
            layout2.addWidget(label2)

            frame1.setLayout(layout1)
            frame2.setLayout(layout2)

            item1 = QListWidgetItem()
            item1.setSizeHint(frame1.sizeHint())
            list_equipe1.addItem(item1)
            list_equipe1.setItemWidget(item1, frame1)

            item2 = QListWidgetItem()
            item2.setSizeHint(frame2.sizeHint())
            list_equipe2.addItem(item2)
            list_equipe2.setItemWidget(item2, frame2)

    def montrer_page_equipes(self):
        """Montre la page de comparaison de'équipes"""
        if hasattr(self, 'joueur1_recherche_bg2') and self.joueur1_recherche_bg2:
            self.joueur1_recherche_bg2.hide()
            self.joueur1_recherche_bg.hide()
            self.joueur1_recherche.hide()
            self.joueur1_recherche_loupe.hide()
            self.joueur2_recherche_bg2.hide()
            self.joueur2_recherche_bg.hide()
            self.joueur2_recherche.hide()
            self.joueur2_recherche_loupe.hide()

        self.label_mode_bg.setText("Comparaison d'équipes")
        self.label_mode.setText("Comparaison d'équipes")
        self.matchup = QLabel(self)
        self.matchup.show()
        self.matchup.setGeometry(45, 363, 705, 40)
        self.matchup.setStyleSheet("""background-color: #bbbcc0""")
        matchup_stats = self.get_matchup(self.equipe_1, self.equipe_2)
        self.matchup.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.matchup.setText(
            f"Cette saison: {self.equipe_1} - {matchup_stats['victoires_equipe_1']} victoire(s) | "
            f"{self.equipe_2} - {matchup_stats['victoires_equipe_2']} victoire(s) | "
            f"Matchs nuls: {matchup_stats['nulles']}"
        )
        self.matchup.setFont(QFont(self.jersey25_16))

        self.populer_listes_comparaison(self.list_equipe1, self.list_equipe2)

    def montrer_page_joueurs(self):
        """Montre la page de comparaison de'équipes"""
        self.label_mode_bg.setText("Comparaison de joueurs")
        self.label_mode.setText("Comparaison de joueurs")

        self.matchup.hide()

        self.joueur1_recherche_bg2 = QLabel(self)
        self.joueur1_recherche_bg2.setGeometry(45, 363, 337, 40)
        self.joueur1_recherche_bg2.setStyleSheet("""background-color: #2f3038""")
        self.joueur1_recherche_bg2.show()

        self.joueur1_recherche_bg = QLabel(self)
        self.joueur1_recherche_bg.setGeometry(48, 360, 337, 40)
        self.joueur1_recherche_bg.setStyleSheet("""background-color: #bbbcc0""")
        self.joueur1_recherche_bg.show()

        self.joueur1_recherche = QLineEdit(self)
        self.joueur1_recherche.setGeometry(53, 365, 293, 30)
        self.joueur1_recherche.setStyleSheet("""background-color: #d9d9d9;
                                                    border-radius: 0px;
                                                    padding-left: 5px;""")
        self.joueur1_recherche.setFont(self.jersey25_16)
        self.joueur1_recherche.setPlaceholderText("RECHERCHE JOUEUR 1")
        self.joueur1_recherche.show()

        self.joueur1_recherche_loupe = QLabel(self)
        self.joueur1_recherche_loupe.setStyleSheet("""background-color: #bbbcc0;
                                                        border-radius: 0px;""")
        self.joueur1_recherche_loupe.setGeometry(350, 365, 30, 30)
        self.loupe = QPixmap("resources/images/search.svg")
        self.joueur1_recherche_loupe.setPixmap(self.loupe)
        self.joueur1_recherche_loupe.setScaledContents(True)
        self.joueur1_recherche_loupe.show()

        self.joueur2_recherche_bg2 = QLabel(self)
        self.joueur2_recherche_bg2.setGeometry(410, 363, 337, 40)
        self.joueur2_recherche_bg2.setStyleSheet("""background-color: #2f3038""")
        self.joueur2_recherche_bg2.show()

        self.joueur2_recherche_bg = QLabel(self)
        self.joueur2_recherche_bg.setGeometry(413, 360, 337, 40)
        self.joueur2_recherche_bg.setStyleSheet("""background-color: #bbbcc0""")
        self.joueur2_recherche_bg.show()

        self.joueur2_recherche = QLineEdit(self)
        self.joueur2_recherche.setGeometry(418, 365, 293, 30)
        self.joueur2_recherche.setStyleSheet("""background-color: #d9d9d9;
                                                    border-radius: 0px;
                                                    padding-left: 5px;""")
        self.joueur2_recherche.setFont(self.jersey25_16)
        self.joueur2_recherche.setPlaceholderText("RECHERCHE JOUEUR 2")
        self.joueur2_recherche.show()

        self.joueur2_recherche_loupe = QLabel(self)
        self.joueur2_recherche_loupe.setStyleSheet("""background-color: #bbbcc0;
                                                        border-radius: 0px;""")
        self.joueur2_recherche_loupe.setGeometry(715, 365, 30, 30)
        self.loupe = QPixmap("resources/images/search.svg")
        self.joueur2_recherche_loupe.setPixmap(self.loupe)
        self.joueur2_recherche_loupe.setScaledContents(True)
        self.joueur2_recherche_loupe.show()


        self.joueur1_recherche.textChanged.connect(
            lambda: self.rechercher_joueur(self.joueur1_recherche.text(), self.list_equipe1)
            if len(self.joueur1_recherche.text()) >= 3 or len(self.joueur1_recherche.text()) == 0
            else None
        )

        self.joueur2_recherche.textChanged.connect(
            lambda: self.rechercher_joueur(self.joueur2_recherche.text(), self.list_equipe2)
            if len(self.joueur2_recherche.text()) >= 3 or len(self.joueur2_recherche.text()) == 0
            else None
        )

    def btn_equipes_click(self):
        """Action lors du click sur le bouton équipes"""
        self.joueurs_bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.joueurs_bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.equipes_bg_fg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
        self.equipes_bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

        self.montrer_page_equipes()

    def btn_joueurs_click(self):
        """Action lors du click sur le bouton joueurs"""
        self.equipes_bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.equipes_bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.joueurs_bg_fg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
        self.joueurs_bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

        self.montrer_page_joueurs()

    def get_matchup(self, equipe_1, equipe_2):
        """Récupère le nombre de matchs et les résultats entre deux équipes"""
        matchup_stats = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""
                SELECT
                    COUNT(*) AS matchs_joues,
                    SUM(CASE WHEN equipe_local = %(equipe_1)s AND score_local > score_visiteur THEN 1
                            WHEN equipe_visiteur = %(equipe_1)s AND score_visiteur > score_local THEN 1 ELSE 0 END) AS victoires_equipe_1,
                    SUM(CASE WHEN equipe_local = %(equipe_2)s AND score_local > score_visiteur THEN 1
                            WHEN equipe_visiteur = %(equipe_2)s AND score_visiteur > score_local THEN 1 ELSE 0 END) AS victoires_equipe_2,
                    SUM(CASE WHEN score_local = score_visiteur THEN 1 ELSE 0 END) AS nulles
                FROM parties
                WHERE (equipe_local = %(equipe_1)s AND equipe_visiteur = %(equipe_2)s)
                OR (equipe_local = %(equipe_2)s AND equipe_visiteur = %(equipe_1)s)
                """, {
                    "equipe_1": equipe_1,
                    "equipe_2": equipe_2
                })

                result = cursor.fetchone()
                if result:
                    matchup_stats = {
                        "matchs_joues": result["matchs_joues"],
                        "victoires_equipe_1": result["victoires_equipe_1"],
                        "victoires_equipe_2": result["victoires_equipe_2"],
                        "nulles": result["nulles"]
                    }

        return matchup_stats

    def get_equipe(self, equipe):
        """Récupère les stats d'une équipe spécifique par son nom"""
        equipe_data = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""
                    SELECT id_equipe, nom_equipe, position, matchs_joues, points,
                        victoires_total, victoires_fusillades, defaites,
                        defaites_fusillades, nulles, buts_pour, buts_contre,
                        differentiel, points_periode, points_partie,
                        points_penalites, points_par_match
                    FROM equipes
                    WHERE nom_equipe = %(nom_equipe)s
                """, {
                    "nom_equipe": equipe
                })

                result = cursor.fetchone()
                if result:
                    equipe_data = {
                        "id_equipe": result["id_equipe"],
                        "nom_equipe": result["nom_equipe"],
                        "position": result["position"],
                        "matchs_joues": result["matchs_joues"],
                        "points": result["points"],
                        "victoires_total": result["victoires_total"],
                        "victoires_fusillades": result["victoires_fusillades"],
                        "defaites": result["defaites"],
                        "defaites_fusillades": result["defaites_fusillades"],
                        "nulles": result["nulles"],
                        "buts_pour": result["buts_pour"],
                        "buts_contre": result["buts_contre"],
                        "differentiel": result["differentiel"],
                        "points_periode": result["points_periode"],
                        "points_partie": result["points_partie"],
                        "points_penalites": result["points_penalites"],
                        "points_par_match": result["points_par_match"]
                    }

        return equipe_data
