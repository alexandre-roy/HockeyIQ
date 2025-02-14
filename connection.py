#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt

class Connection(QWidget):
    """Page de connection"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initialiser_page_connection()

    def initialiser_page_connection(self):
        """Interface graphique"""
        logo_label = QLabel(self)
        logo_label.setGeometry(177, 40, 447, 67)

        carre_1 = QLabel(self)
        carre_1.setGeometry(180, 150, 210, 100)
        carre_1.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        carre_dessous = QLabel(self)
        carre_dessous.setGeometry(200, 200, 210, 30)
        carre_dessous.setStyleSheet("background-color: #BBBCC0;")

        carre_rond = QLabel(self)
        carre_rond.setGeometry(390, 190, 210, 40)
        carre_rond.setStyleSheet("background-color: #F5F5F5;"
                              "border-radius: 8px;")

        btn_connection = QPushButton(self)
        btn_connection.setGeometry(180, 150, 210, 60)
        btn_connection.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;"
                              "color: #2F3038;"
                              "font-family: Futura;"
                              "font-size: 24px;"
                              "font-weight: Bold;")
        btn_connection.setText("CONNECTION")

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
        btn_inscription.clicked.connect(self.btn_inscription_click)

        carre_email = QLabel(self)
        carre_email.setGeometry(180, 230, 440, 60)
        carre_email.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        txt_email_connection = QLineEdit(self)
        txt_email_connection.setGeometry(185, 235, 430, 50)
        txt_email_connection.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 5px;"
                              "padding: 5px;"
                              "color: #2F3038;"
                              "font-weight: Bold;")
        txt_email_connection.setPlaceholderText("ADRESSE COURRIEL")
        txt_email_connection.setFocusPolicy(Qt.FocusPolicy.ClickFocus)


        carre_pwd = QLabel(self)
        carre_pwd.setGeometry(180, 315, 440, 60)
        carre_pwd.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        txt_pwd_connection = QLineEdit(self)
        txt_pwd_connection.setGeometry(185, 320, 430, 50)
        txt_pwd_connection.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 5px;"
                              "padding: 5px;"
                              "color: #2F3038;"
                              "font-weight: Bold;")
        txt_pwd_connection.setPlaceholderText("MOT DE PASSE")
        txt_pwd_connection.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        txt_pwd_connection.setEchoMode(QLineEdit.EchoMode.Password)

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

    def btn_inscription_click(self):
        """Action lors du clique sur le bouton INSCRIPTION"""
        self.main_window.afficher_inscription()

    def btn_connection_click(self):
        """Action lors du clique sur le bouton CONNECTION"""

    def btn_go_click(self):
        """Action de cliquer sur le bouton GO"""
