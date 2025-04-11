#pylint: disable = no-name-in-module
#pylint: disable = unused-import

"""Modules"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from connection import Connection
from inscription import Inscription
from overview import Overview
from calendrier import Calendrier
from classement import Classement
from stats import Statistiques
from compte import Compte
from loading import Loading
from comparaison import Comparaison
from predictions import Predictions
import bd

class MainWindow(QMainWindow):
    """Fenêtre d'accueil / login"""
    def __init__(self):
        super().__init__()
        self.setGeometry(335, 250, 800, 500)
        self.setStyleSheet("background-color: #C9E1F7;")
        self.setFixedSize(800, 500)
        self.stacked_widget = QStackedWidget()

        self.connection = Connection(self, "")
        self.inscription = Inscription(self)
        self.overview = Overview(self)
        self.calendrier = Calendrier(self)
        self.classement = Classement(self)
        self.stats = Statistiques(self)
        self.compte = None
        self.loading = None
        self.comparaison = Comparaison(self, None, None, None, None)

        self.setCentralWidget(self.connection)

        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile("resources/sounds/nhl94.mp3"))
        self.player.mediaStatusChanged.connect(self.redemarrer_musique)
        self.player.play()

    def redemarrer_musique(self, statut):
        """Redémarre la musique quand elle est terminée"""
        if statut == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()

    def afficher_connection(self):
        """Affiche la page de connection"""
        message = self.compte.message if self.compte else ""
        self.connection = Connection(self, message)
        self.setCentralWidget(self.connection)

    def afficher_inscription(self):
        """Affiche la page d'inscription"""
        self.inscription = Inscription(self)
        self.setCentralWidget(self.inscription)

    def afficher_overview(self):
        """Affiche la page d'overview"""
        self.overview = Overview(self)
        self.setCentralWidget(self.overview)

    def afficher_calendrier(self):
        """Affiche la page du calendrier"""
        self.calendrier = Calendrier(self)
        self.setCentralWidget(self.calendrier)

    def afficher_classement(self):
        """Affiche la page du classement"""
        self.classement = Classement(self)
        self.setCentralWidget(self.classement)

    def afficher_stats(self):
        """Affiche la page des statistiques"""
        self.stats = Statistiques(self)
        self.setCentralWidget(self.stats)

    def afficher_compte(self):
        """Affiche la page du compte"""
        email = self.connection.email
        self.compte = Compte(self, email)
        self.setCentralWidget(self.compte)

    def afficher_loading(self):
        """Affiche la page de chargement"""
        self.loading = Loading(self)
        self.setCentralWidget(self.loading)

    def afficher_comparaison(self, equipe_1, equipe_2, game_id):
        """Affiche la page de comparaison"""
        user_id = self.connection.id_utilisateur
        self.comparaison = Comparaison(self, equipe_1, equipe_2, game_id, user_id)
        self.setCentralWidget(self.comparaison)

    def afficher_predictions(self):
        """Affiche la page des prédictions"""
        user_id = self.connection.id_utilisateur
        print(f"{user_id}")
        stats = []
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""
                    SELECT
                        user_id,
                        game_id,
                        user_prediction,
                        computer_prediction,
                        user_correct,
                        computer_correct
                    FROM predictions
                    WHERE user_id = %(user_id)s
                """, {
                    "user_id": user_id
                })

                for ligne in cursor:
                    stats.append({
                        "user_id": ligne["user_id"],
                        "game_id": ligne["game_id"],
                        "user_prediction": ligne["user_prediction"],
                        "computer_prediction": ligne["computer_prediction"],
                        "user_correct": ligne["user_correct"],
                        "computer_correct": ligne["computer_correct"]
                    })

                cursor.execute("""
                SELECT
                    COUNT(CASE WHEN user_correct = 1 THEN 1 END) AS user_correct_count,
                    COUNT(CASE WHEN computer_correct = 1 THEN 1 END) AS computer_correct_count
                FROM predictions
                WHERE user_id = %(user_id)s
            """, {
                "user_id": user_id
            })
            result = cursor.fetchone()
            user_correct_count = 0
            computer_correct_count = 0

            if result:
                user_correct_count = result["user_correct_count"]
                computer_correct_count = result["computer_correct_count"]

        predictions = Predictions(self, stats, user_correct_count, computer_correct_count)
        self.setCentralWidget(predictions)
