#pylint: disable = no-name-in-module
#pylint: disable = unused-import

"""Modules"""
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    """Fenêtre d'accueil / login"""
    def __init__(self):
        super().__init__()
        self.setGeometry(335, 250, 800, 500)
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setFixedSize(800, 500)
        self.init_ui()

    def btn_go_click(self):
        """Action de cliquer sur le boutton GO"""

    def init_ui(self):
        """Interface graphique"""
        logo_label = QLabel(self)
        logo_label.setGeometry((self.width() - 447) // 2, 40, 447, 67)

        carre_1 = QLabel(self)
        carre_1.setGeometry(180, 230, 440, 60)
        carre_1.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        carre_2 = QLabel(self)
        carre_2.setGeometry(180, 150, 210, 100)
        carre_2.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        btn_connection = QPushButton(self)
        btn_connection.setGeometry(180, 150, 210, 60)
        btn_connection.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;"
                              "color: #2F3038;"
                              "font-family: Futura;"
                              "font-size: 24px;"
                              "font-weight: Bold;")
        btn_connection.setText("CONNECTION")
        btn_connection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        btn_inscription = QPushButton(self)
        btn_inscription.setGeometry(410, 150, 210, 60)
        btn_inscription.setStyleSheet("background-color: #7A97B8;"
                              "border-radius: 5px;"
                              "color: #F5F5F5;"
                              "font-family: Futura;"
                              "font-size: 24px;"
                              "font-weight: Bold;")
        btn_inscription.setText("INSCRIPTION")
        btn_inscription.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        carre_4 = QLabel(self)
        carre_4.setGeometry(180, 315, 440, 60)
        carre_4.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        btn_go = QPushButton(self)
        btn_go.setGeometry(180, 400, 440, 60)
        btn_go.setStyleSheet("background-color: #8C322D;"
                              "border-radius: 5px;"
                              "font-size: 24px;"
                              "color: #F5F5F5;"
                              "font-family: Futura;"
                              "font-weight: Bold;")
        btn_go.setText("GO")
        btn_go.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_go.clicked.connect(self.btn_go_click)


        logo = QPixmap("resources/logo.png")
        logo_label.setPixmap(logo)
        logo_label.setScaledContents(True)
