#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
from bd import sql

class Overview(QWidget):
    """Page d'overview"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_overview()

    def initialiser_page_overview(self):
        """Interface graphique"""
        label = QLabel(self)
        label.setText("overview")
