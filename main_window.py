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

class MainWindow(QMainWindow):
    """Fenêtre d'accueil / login"""
    def __init__(self):
        super().__init__()
        self.setGeometry(335, 250, 800, 500)
        self.setStyleSheet("background-color: #C9E1F7;")
        self.setFixedSize(800, 500)
        self.stacked_widget = QStackedWidget()

        self.connection = Connection(self)
        self.inscription = Inscription(self)
        self.overview = Overview(self)
        self.calendrier = Calendrier(self)
        self.classement = Classement(self)

        self.setCentralWidget(self.classement)

        # self.audio_output = QAudioOutput()
        # self.player = QMediaPlayer()
        # self.player.setAudioOutput(self.audio_output)
        # self.player.setSource(QUrl.fromLocalFile("resources/sounds/nhl94.mp3"))
        # self.player.mediaStatusChanged.connect(self.redemarrer_musique)
        # self.player.play()

    def redemarrer_musique(self, statut):
        """Redémarre la musique quand elle est terminée"""
        if statut == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()

    def afficher_connection(self):
        """Affiche la page de connection"""
        self.connection = Connection(self)
        self.setCentralWidget(self.connection)

    def afficher_inscription(self):
        """Affiche la page d'inscription"""
        self.inscription = Inscription(self)
        self.setCentralWidget(self.inscription)

    def afficher_overview(self):
        """Affiche la page d'overview"""
        self.overview = Overview(self)
        self.setCentralWidget(self.overview)
        #self.player.stop()

    def afficher_calendrier(self):
        """Affiche la page du calendrier"""
        self.calendrier = Calendrier(self)
        self.setCentralWidget(self.calendrier)

    def afficher_classement(self):
        """Affiche la page du classement"""
        self.classement = Classement(self)
        self.setCentralWidget(self.classement)