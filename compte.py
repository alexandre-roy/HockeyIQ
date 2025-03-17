#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QFontDatabase, QFont, QColor, QBrush, QIcon, QCursor
from PyQt6.QtCore import Qt
import bd
import utils

class Compte(QWidget):
    """Page de compte"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_compte()

    def initialiser_page_compte(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 6)

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        carre_bg = QLabel(self)
        carre_bg.setGeometry(45, 150, 705, 203)
        carre_bg.setStyleSheet("background-color: #bbbcc0;")

        label_compte_bg = QLabel(self)
        label_compte_bg.setGeometry(20, 10, 300, 60)
        label_compte_bg.setText("Mon compte")
        label_compte_bg.setFont(self.jersey25_64)
        label_compte_bg.setStyleSheet("color: #2f3038")

        label_compte = QLabel(self)
        label_compte.setGeometry(22, 8, 300, 60)
        label_compte.setText("Mon compte")
        label_compte.setFont(self.jersey25_64)
        label_compte.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        label_modif_bg = QLabel(self)
        label_modif_bg.setGeometry(40, 100, 320, 40)
        label_modif_bg.setText("Modification du profil")
        label_modif_bg.setFont(self.jersey25_32)
        label_modif_bg.setStyleSheet("color: #2f3038")

        label_modif = QLabel(self)
        label_modif.setGeometry(42, 98, 320, 40)
        label_modif.setText("Modification du profil")
        label_modif.setFont(self.jersey25_32)
        label_modif.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        bg_noir = QPushButton(self)
        bg_noir_2 = QPushButton(self)
        self.bg_fg = QPushButton(self)
        self.bg_fg_2 = QPushButton(self)

        bg_noir.setGeometry(714, 107, 30, 33)
        bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2.setGeometry(711, 110, 36, 27)
        bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.bg_fg.setGeometry(717, 104, 30, 33)
        self.bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.bg_fg_2.setGeometry(714, 107, 36, 27)
        self.bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.bg_fg_2.setFont(self.jersey25_32)
        self.bg_fg_2.setIcon(QIcon("resources/images/save.svg"))
        self.bg_fg_2.setIconSize(self.bg_fg_2.size())
        self.bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bg_fg_2.clicked.connect(lambda: self.save_info())

        bg_noir_supprimer = QPushButton(self)
        bg_noir_2_supprimer = QPushButton(self)
        self.bg_fg_supprimer = QPushButton(self)
        self.bg_fg_2_supprimer = QPushButton(self)

        bg_noir_supprimer.setGeometry(604, 372, 140, 33)
        bg_noir_supprimer.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2_supprimer.setGeometry(601, 375, 146, 27)
        bg_noir_2_supprimer.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.bg_fg_supprimer.setGeometry(607, 369, 140, 33)
        self.bg_fg_supprimer.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.bg_fg_2_supprimer.setGeometry(604, 372, 146, 27)
        self.bg_fg_2_supprimer.setStyleSheet("background-color: #bbbcc0; border-radius: 0px; color: #cc1d10")
        self.bg_fg_2_supprimer.setFont(self.jersey25_16)
        self.bg_fg_2_supprimer.setText("Supprimer mon profil")
        self.bg_fg_2_supprimer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bg_fg_2_supprimer.clicked.connect(lambda: self.supprimer_profil())

    def save_info(self):
        """Sauvegarde les informations"""
        print("Sauvegarde des informations")

    def supprimer_profil(self):
        """Supprime le profil"""
        print("Suppression du profil")
