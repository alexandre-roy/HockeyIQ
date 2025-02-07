#pylint: disable = no-name-in-module
#pylint: disable = unused-import

"""Modules"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
from Interface.connection import Connection
from Interface.inscription import Inscription

class MainWindow(QMainWindow):
    """Fenêtre d'accueil / login"""
    def __init__(self):
        super().__init__()
        self.setGeometry(335, 250, 800, 500)
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setFixedSize(800, 500)
        self.stacked_widget = QStackedWidget()

        self.connection = Connection(self)
        self.inscription = Inscription(self)

        self.setCentralWidget(self.connection)

    def afficher_connection(self):
        """Affiche la page de connection"""
        self.connection = Connection(self)
        self.setCentralWidget(self.connection)

    def afficher_inscription(self):
        """Affiche la page d'inscription"""
        self.inscription = Inscription(self)
        self.setCentralWidget(self.inscription)
