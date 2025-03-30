#pylint: disable = no-name-in-module
#pylint: disable = unused-import

"""Modules"""
import sys
from io import StringIO
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QFontDatabase, QFont, QPixmap, QTransform, QCursor
from PyQt6.QtCore import QTimer, pyqtSignal, Qt

class Loading(QWidget):
    """Fenêtre qui s'afciche pendant le chargement"""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.rotation_angle = 0
        self.initialiser_page_loading()

    def initialiser_page_loading(self):
        """Interface graphique"""

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        jersey25_32 = QFont("jersey 25", 32)

        logo_label = QLabel(self)
        logo_label.setGeometry(100, 20, 600, 140)

        logo = QPixmap("resources/images/logo.png")
        logo_label.setPixmap(logo)
        logo_label.setScaledContents(True)

        label_load = QLabel(self)
        label_load.setGeometry(230, 200, 335, 40)
        label_load.setText("Chargement des données ...")
        label_load.setStyleSheet("Color: #2f3038;")
        label_load.setFont(QFont(jersey25_32))

        self.load_img = QPushButton(self)
        self.load_img.setGeometry(375, 310, 40, 40)
        self.load_img.setStyleSheet("border-radius: 0px;")
        self.load_img.setIcon(QIcon("Resources/Images/loading.svg"))
        self.load_img.setIconSize(self.load_img.size())

        self.console_output = StringIO()
        sys.stdout = self.console_output

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate_icon)
        self.timer.timeout.connect(self.check_console_message)
        self.timer.start(500)

    def check_console_message(self):
        """Check if a specific message has been printed to the console"""
        console_output = sys.stdout.getvalue()
        if "La base de données est maintenant à jour !" in console_output:
            self.main_window.afficher_overview()

    def rotate_icon(self):
        """Animation de chargement"""
        original_pixmap = QPixmap("Resources/Images/loading.svg")

        self.rotation_angle = (self.rotation_angle + 90) % 360

        transform = QTransform().rotate(self.rotation_angle)
        rotated_pixmap = original_pixmap.transformed(transform)

        self.load_img.setIcon(QIcon(rotated_pixmap))