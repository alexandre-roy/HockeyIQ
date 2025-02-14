#pylint: disable = no-name-in-module

"""Modules"""
import re
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
import bd

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

        self.erreur_email = QLabel(self)
        self.erreur_email.setGeometry(185, 290, 430, 20)
        self.erreur_email.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_email.setText("Cette adresse courriel n'est pas lié à un compte")
        self.erreur_email.hide()

        self.erreur_email_regex = QLabel(self)
        self.erreur_email_regex.setGeometry(185, 290, 430, 20)
        self.erreur_email_regex.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_email_regex.setText("Adresse courriel invalide")
        self.erreur_email_regex.hide()

        self.veuillez_remplir_email = QLabel(self)
        self.veuillez_remplir_email.setGeometry(185, 290, 430, 20)
        self.veuillez_remplir_email.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.veuillez_remplir_email.setText("Veuillez remplir ce champ")
        self.veuillez_remplir_email.hide()

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

        self.veuillez_remplir_pwd = QLabel(self)
        self.veuillez_remplir_pwd.setGeometry(185, 375, 200, 20)
        self.veuillez_remplir_pwd.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.veuillez_remplir_pwd.setText("Veuillez remplir ce champ")
        self.veuillez_remplir_pwd.hide()

        self.erreur_pwd = QLabel(self)
        self.erreur_pwd.setGeometry(185, 375, 200, 20)
        self.erreur_pwd.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_pwd.setText("Mot de passe incorrect")
        self.erreur_pwd.hide()

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
        btn_go.clicked.connect(lambda: self.btn_go_click(txt_email_connection.text(),
                                                         txt_pwd_connection.text()))


        logo = QPixmap("resources/logo.png")
        logo_label.setPixmap(logo)
        logo_label.setScaledContents(True)

    def btn_inscription_click(self):
        """Action lors du clique sur le bouton INSCRIPTION"""
        self.main_window.afficher_inscription()

    def btn_connection_click(self):
        """Action lors du clique sur le bouton CONNECTION"""

    def btn_go_click(self, email, pwd):
        """Action de cliquer sur le bouton GO"""
        valide = True

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        self.veuillez_remplir_email.hide()
        self.veuillez_remplir_pwd.hide()
        self.erreur_email.hide()
        self.erreur_email_regex.hide()
        self.erreur_pwd.hide()

        if not email or email.isspace():
            valide = False
            self.veuillez_remplir_email.show()
        elif not re.match(email_regex, email):
            valide = False
            self.erreur_email_regex.show()

        if not pwd or pwd.isspace():
            valide = False
            self.veuillez_remplir_pwd.show()

        utilisateur_dictionnaire = {
            "email" : email,
            "mot_de_passe" : pwd
        }

        with bd.creer_connexion() as connection:
            with connection.get_curseur() as c:
                c.execute("SELECT * FROM utilisateurs WHERE email = %(email)s",
                           utilisateur_dictionnaire)
                if not c.fetchone():
                    valide = False
                    self.erreur_email.show()

        with bd.creer_connexion() as connection:
            with connection.get_curseur() as c:
                c.execute("SELECT * FROM utilisateurs WHERE email = %(email)s " +
                          "AND mot_de_passe != (SHA2(%(mot_de_passe)s, 256))",
                           utilisateur_dictionnaire)
                if c.fetchone():
                    valide = False
                    self.erreur_pwd.show()

        with bd.creer_connexion() as connection:
            with connection.get_curseur() as c:
                c.execute("SELECT * FROM utilisateurs WHERE email = %(email)s " +
                          "AND mot_de_passe = (SHA2(%(mot_de_passe)s, 256))",
                           utilisateur_dictionnaire)
                if c.fetchone():
                    valide = True

        if valide:
            self.main_window.afficher_overview()
