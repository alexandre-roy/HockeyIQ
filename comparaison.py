#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFontDatabase, QFont, QCursor, QIcon
from PyQt6.QtCore import Qt
import bd
import utils

class Comparaison(QWidget):
    """Page d'overview"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

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

    def montrer_page_equipes(self):
        """Montre la page de comparaison de'équipes"""
        self.label_mode_bg.setText("Comparaison d'équipes")
        self.label_mode.setText("Comparaison d'équipes")

    def montrer_page_joueurs(self):
        """Montre la page de comparaison de'équipes"""
        self.label_mode_bg.setText("Comparaison de joueurs")
        self.label_mode.setText("Comparaison de joueurs")

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
