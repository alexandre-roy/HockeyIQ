#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt

class Inscription(QWidget):
    """Page d'inscription"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_inscription()

    def initialiser_page_inscription(self):
        """Interface graphique"""
        logo_label = QLabel(self)
        logo_label.setGeometry(177, 40, 447, 67)

        carre_dessous = QLabel(self)
        carre_dessous.setGeometry(410, 200, 210, 90)
        carre_dessous.setStyleSheet("background-color: #BBBCC0;"
                                    "border-radius: 5px;")

        carre_rond = QLabel(self)
        carre_rond.setGeometry(210, 190, 200, 40)
        carre_rond.setStyleSheet("background-color: #F5F5F5;"
                              "border-radius: 8px;")

        btn_connection = QPushButton(self)
        btn_connection.setGeometry(180, 150, 210, 60)
        btn_connection.setStyleSheet("background-color: #7A97B8;"
                              "border-radius: 5px;"
                              "color: #F5F5F5;"
                              "font-family: Futura;"
                              "font-size: 24px;"
                              "font-weight: Bold;")
        btn_connection.setText("CONNECTION")
        btn_connection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_connection.clicked.connect(self.btn_connection_click)

        btn_inscription = QPushButton(self)
        btn_inscription.setGeometry(410, 150, 210, 60)
        btn_inscription.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;"
                              "color: #2F3038;"
                              "font-family: Futura;"
                              "font-size: 24px;"
                              "font-weight: Bold;")
        btn_inscription.setText("INSCRIPTION")

        carre_email = QLabel(self)
        carre_email.setGeometry(180, 230, 210, 60)
        carre_email.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        txt_email_inscription = QLineEdit(self)
        txt_email_inscription.setGeometry(185, 235, 200, 50)
        txt_email_inscription.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 5px;"
                              "padding: 5px;"
                              "color: #2F3038;"
                              "font-weight: Bold;")
        txt_email_inscription.setPlaceholderText("ADRESSE COURRIEL")
        txt_email_inscription.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        txt_nom_inscription = QLineEdit(self)
        txt_nom_inscription.setGeometry(415, 235, 200, 50)
        txt_nom_inscription.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 5px;"
                              "padding: 5px;"
                              "color: #2F3038;"
                              "font-weight: Bold;")
        txt_nom_inscription.setPlaceholderText("PRÉNOM")
        txt_nom_inscription.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        carre_pwd = QLabel(self)
        carre_pwd.setGeometry(180, 315, 210, 60)
        carre_pwd.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        txt_pwd_inscription = QLineEdit(self)
        txt_pwd_inscription.setGeometry(185, 320, 200, 50)
        txt_pwd_inscription.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 5px;"
                              "padding: 5px;"
                              "color: #2F3038;"
                              "font-weight: Bold;")
        txt_pwd_inscription.setPlaceholderText("MOT DE PASSE")
        txt_pwd_inscription.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        txt_pwd_inscription.setEchoMode(QLineEdit.EchoMode.Password)

        carre_pwd_confirm = QLabel(self)
        carre_pwd_confirm.setGeometry(410, 315, 210, 60)
        carre_pwd_confirm.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 5px;")

        txt_pwd_inscription_confirm = QLineEdit(self)
        txt_pwd_inscription_confirm.setGeometry(415, 320, 200, 50)
        txt_pwd_inscription_confirm.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 5px;"
                              "padding: 5px;"
                              "color: #2F3038;"
                              "font-weight: Bold;")
        txt_pwd_inscription_confirm.setPlaceholderText("MOT DE PASSE x2")
        txt_pwd_inscription_confirm.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        txt_pwd_inscription_confirm.setEchoMode(QLineEdit.EchoMode.Password)


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

    def btn_connection_click(self):
        """Action lors du clique sur le bouton CONNECTION"""
        self.main_window.afficher_connection()

    def btn_go_click(self):
        """Action de cliquer sur le bouton GO"""
