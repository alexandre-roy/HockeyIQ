#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QFrame, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFontDatabase, QFont, QCursor, QIcon
from PyQt6.QtCore import Qt
import bd
import utils

class Predictions(QWidget):
    """Page des prédictions"""
    def __init__(self, main_window, stats, user_correct_count, computer_correct_count):
        super().__init__()
        self.main_window = main_window
        self.stats = stats
        self.user_correct_count = user_correct_count
        self.computer_correct_count = computer_correct_count

        self.initialiser_page_predictions()
        self.update_predictions()

    def initialiser_page_predictions(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 5)

        self.matchup = QLabel(self)
        self.label_user_number = QLabel(self)
        self.label_computer_number = QLabel(self)
        self.label_user_correct = QLabel(self)
        self.label_computer_correct = QLabel(self)
        self.liste_historique = QListWidget(self)

        QFontDatabase.addApplicationFont(utils.resource_path("resources/fonts/Jersey25-Regular.ttf"))
        QFontDatabase.addApplicationFont(utils.resource_path("resources/fonts/Inter-VariableFont_opsz,wght.ttf"))

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        label_predictions_bg = QLabel(self)
        label_predictions_bg.setGeometry(20, 20, 300, 40)
        label_predictions_bg.setText("Prédictions")
        label_predictions_bg.setFont(self.jersey25_64)
        label_predictions_bg.setStyleSheet("color: #2f3038")

        label_predictions = QLabel(self)
        label_predictions.setGeometry(22, 18, 300, 40)
        label_predictions.setText("Prédictions")
        label_predictions.setFont(self.jersey25_64)
        label_predictions.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        self.label_user_bg = QLabel(self)
        self.label_user_bg.setGeometry(40, 100, 300, 40)

        self.label_user_bg.setFont(self.jersey25_32)
        self.label_user_bg.setStyleSheet("color: #2f3038")

        self.label_user = QLabel(self)
        self.label_user.setGeometry(42, 98, 300, 40)

        self.label_user.setFont(self.jersey25_32)
        self.label_user.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        self.montrer_page_stats()

        self.stats_bg_noir = QPushButton(self)
        self.stats_bg_noir_2 = QPushButton(self)
        self.stats_bg_fg = QPushButton(self)
        self.stats_bg_fg_2 = QPushButton(self)

        self.stats_bg_noir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stats_bg_noir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stats_bg_fg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stats_bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.stats_bg_fg_2.setToolTip("Statistiques")

        self.stats_bg_noir.setGeometry(670, 21, 40, 43)
        self.stats_bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.stats_bg_noir_2.setGeometry(667, 24, 46, 37)
        self.stats_bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.stats_bg_fg.setGeometry(673, 18, 40, 43)
        self.stats_bg_fg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

        self.stats_bg_fg_2.setGeometry(670, 21, 46, 37)
        self.stats_bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
        self.stats_bg_fg_2.setIcon(QIcon(utils.resource_path("resources/images/analyse.svg")))
        self.stats_bg_fg_2.setIconSize(self.stats_bg_fg_2.size())
        self.stats_bg_fg_2.clicked.connect(self.btn_stats_click)

        self.historique_bg_noir = QPushButton(self)
        self.historique_bg_noir_2 = QPushButton(self)
        self.historique_bg_fg = QPushButton(self)
        self.historique_bg_fg_2 = QPushButton(self)

        self.historique_bg_noir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historique_bg_noir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historique_bg_fg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historique_bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.historique_bg_fg_2.setToolTip("Historique")

        self.historique_bg_noir.setGeometry(730, 21, 40, 43)
        self.historique_bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.historique_bg_noir_2.setGeometry(727, 24, 46, 37)
        self.historique_bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.historique_bg_fg.setGeometry(733, 18, 40, 43)
        self.historique_bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.historique_bg_fg_2.setGeometry(730, 21, 46, 37)
        self.historique_bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.historique_bg_fg_2.setIcon(QIcon(utils.resource_path("resources/images/historique.svg")))
        self.historique_bg_fg_2.setIconSize(self.historique_bg_fg_2.size())
        self.historique_bg_fg_2.clicked.connect(self.btn_historique_click)

    def make_green(self):
        """Change le plus haut score en vert"""
        user_number = self.label_user_number.text()
        computer_number = self.label_computer_number.text()

        if user_number > computer_number:
            self.label_user_number.setStyleSheet("color: #2bb537; background-color: #bbbcc0")
            self.label_computer_number.setStyleSheet("color: #2f3038; background-color: #bbbcc0")
        elif computer_number > user_number:
            self.label_computer_number.setStyleSheet("color: #2bb537; background-color: #bbbcc0")
            self.label_user_number.setStyleSheet("color: #2f3038; background-color: #bbbcc0")
        else:
            self.label_user_number.setStyleSheet("color: #2f3038; background-color: #bbbcc0")
            self.label_computer_number.setStyleSheet("color: #2f3038; background-color: #bbbcc0")

    def btn_stats_click(self):
        """Action lors du click sur le bouton stats"""
        self.historique_bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.historique_bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.stats_bg_fg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
        self.stats_bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

        self.montrer_page_stats()

    def btn_historique_click(self):
        """Action lors du click sur le bouton historique"""
        self.stats_bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.stats_bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.historique_bg_fg.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
        self.historique_bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

        self.montrer_page_historique()

    def montrer_page_stats(self):
        """Montre la page des stats des prédictions"""
        self.label_user_bg.setText("Statistiques")
        self.label_user.setText("Statistiques")
        self.liste_historique.hide()

        self.matchup.show()
        self.matchup.setGeometry(45, 318, 705, 85)
        self.matchup.setStyleSheet("""background-color: #bbbcc0; padding-left: 5px;""")
        self.matchup.setWordWrap(True)
        self.matchup.setText("Les prédictions générées par l'ordinateur reposent sur une analyse des statistiques des deux équipes en compétition. Elles prennent en compte les performances lors des matchs précédents, ainsi que des statistiques avancées cumulées tout au long de la saison. Grâce à une mise à jour automatique des données après chaque rencontre, les prédictions restent toujours précises, fiables et adaptées à l'évolution des équipes.")
        self.matchup.setFont(QFont(self.jersey25_16))

        self.label_user_number.show()
        self.label_user_number.setGeometry(72, 150, 300, 100)
        self.label_user_number.setText(f"{self.user_correct_count}")
        self.label_user_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_user_number.setFont(QFont("jersey 25", 96))
        self.label_user_number.setStyleSheet("color: #2f3038; background-color: #bbbcc0")

        self.label_computer_number.show()
        self.label_computer_number.setGeometry(427, 150, 300, 100)
        self.label_computer_number.setText(f"{self.computer_correct_count}")
        self.label_computer_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_computer_number.setFont(QFont("jersey 25", 96))
        self.label_computer_number.setStyleSheet("color: #2f3038; background-color: #bbbcc0")

        self.label_user_correct.show()
        self.label_user_correct.setGeometry(120, 240, 200, 80)
        self.label_user_correct.setText("prédictions correctes de l'utilisateur")
        self.label_user_correct.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_user_correct.setWordWrap(True)
        self.label_user_correct.setFont(QFont("jersey 25", 24))
        self.label_user_correct.setStyleSheet("color: #2f3038; background-color: transparent")

        self.label_computer_correct.show()
        self.label_computer_correct.setGeometry(480, 240, 200, 80)
        self.label_computer_correct.setText("prédictions correctes de l'ordinateur")
        self.label_computer_correct.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_computer_correct.setWordWrap(True)
        self.label_computer_correct.setFont(QFont("jersey 25", 24))
        self.label_computer_correct.setStyleSheet("color: #2f3038; background-color: transparent")

        self.make_green()

    def montrer_page_historique(self):
        """Montre la page de l'historique des prédictions"""
        self.label_user_bg.setText("Historique")
        self.label_user.setText("Historique")

        self.label_user_number.hide()
        self.label_computer_number.hide()
        self.label_user_correct.hide()
        self.label_computer_correct.hide()
        self.matchup.hide()

        self.liste_historique.setGeometry(45, 150, 705, 243)
        self.liste_historique.setWordWrap(True)
        self.liste_historique.setStyleSheet("""background-color: #bbbcc0""")

        predictions = self.get_user_predictions()

        self.populer_liste_historique(predictions, self.liste_historique)

        self.liste_historique.show()

    def get_user_predictions(self):
        """Va chercher les prédictions de l'utilisateur dans la base de données"""
        predictions = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""
                    SELECT p.prediction_id, p.user_prediction, p.computer_prediction, p.user_correct, p.computer_correct, g.equipe_visiteur, g.equipe_local
                    FROM predictions p
                    JOIN parties g ON p.game_id = g.id_partie
                    WHERE p.user_id = %(user_id)s
                """, {
                    "user_id": self.main_window.connection.id_utilisateur
                })

                for row in cursor:
                    predictions[row["prediction_id"]] = {
                        "equipe_visiteur": row["equipe_visiteur"],
                        "equipe_local": row["equipe_local"],
                        "user_prediction": row["user_prediction"],
                        "computer_prediction": row["computer_prediction"],
                        "user_correct": row["user_correct"],
                        "computer_correct": row["computer_correct"]
                    }
        return predictions

    def populer_liste_historique(self, predictions, liste):
        """Popule la liste historique avec les prédictions"""
        liste.clear()

        for _, prediction in predictions.items():
            frame = QFrame()
            frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")
            frame_layout = QHBoxLayout(frame)
            frame_layout.setContentsMargins(10, 5, 10, 5)

            match_label = QLabel(f"{prediction['equipe_visiteur']} @ {prediction['equipe_local']}")
            if prediction['user_correct'] is None:
                user_result_label = QLabel("En attente")
                user_result_label.setStyleSheet("color: #2f3038;")
            elif prediction['user_correct']:
                user_result_label = QLabel("Prédiction correcte")
                user_result_label.setStyleSheet("color: #2bb537;")
            else:
                user_result_label = QLabel("Prédiction incorrecte")
                user_result_label.setStyleSheet("color: #cc1d10;")

            match_label.setFont(self.jersey25_16)
            user_result_label.setFont(self.jersey25_16)

            match_label.setStyleSheet("color: #2f3038;")

            frame_layout.addWidget(match_label)
            frame_layout.addStretch()
            frame_layout.addWidget(user_result_label, alignment=Qt.AlignmentFlag.AlignRight)

            item = QListWidgetItem()
            item.setSizeHint(frame.sizeHint())
            liste.insertItem(0, item)
            liste.setItemWidget(item, frame)

    def update_predictions(self):
        """Mets les prédictionss à jour dans la base de données en fonction des résultats"""
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""
                    SELECT id_partie, equipe_local, equipe_visiteur, score_local, score_visiteur
                    FROM parties
                    WHERE score_local IS NOT NULL AND score_visiteur IS NOT NULL
                """)
                results = {}
                for row in cursor:
                    if row["score_local"] > row["score_visiteur"]:
                        results[row["id_partie"]] = row["equipe_local"]
                    elif row["score_visiteur"] > row["score_local"]:
                        results[row["id_partie"]] = row["equipe_visiteur"]
                    else:
                        results[row["id_partie"]] = None

                cursor.execute("""
                    SELECT prediction_id, game_id, user_prediction, computer_prediction
                    FROM predictions
                    WHERE user_id = %(user_id)s
                """, {
                    "user_id": self.main_window.connection.id_utilisateur
                })
                predictions = cursor.fetchall()

                user_correct_count = 0
                computer_correct_count = 0

                for prediction in predictions:
                    game_id = prediction["game_id"]
                    if game_id in results:
                        actual_winner = results[game_id]
                        user_correct = (prediction["user_prediction"] == actual_winner)
                        computer_correct = (prediction["computer_prediction"] == actual_winner)

                        if user_correct:
                            user_correct_count += 1
                        if computer_correct:
                            computer_correct_count += 1

                        cursor.execute("""
                            UPDATE predictions
                            SET user_correct = %(user_correct)s,
                                computer_correct = %(computer_correct)s
                            WHERE prediction_id = %(prediction_id)s
                        """, {
                            "user_correct": user_correct,
                            "computer_correct": computer_correct,
                            "prediction_id": prediction["prediction_id"]
                        })

            connection.commit()

        self.user_correct_count = user_correct_count
        self.computer_correct_count = computer_correct_count

        self.label_user_number.setText(f"{self.user_correct_count}")
        self.label_computer_number.setText(f"{self.computer_correct_count}")
        self.make_green()