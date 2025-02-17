#pylint: disable = no-name-in-module
#pylint: disable = unused-import

"""Modules"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
from connection import Connection
from inscription import Inscription
from overview import Overview

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

        self.setCentralWidget(self.connection)

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
