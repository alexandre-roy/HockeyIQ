#pylint: disable = no-name-in-module

"""Modules"""
import re
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor, QFontDatabase, QFont, QShortcut, QKeySequence
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
        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        jersey25_40 = QFont("jersey 25", 40)
        jersey25_16 = QFont("jersey 25", 16)

        logo_label = QLabel(self)
        logo_label.setGeometry(100, 20, 600, 140)

        btn_connection_bg = QPushButton(self)
        btn_connection_bg.setGeometry(175, 170, 220, 50)
        btn_connection_bg.setStyleSheet("background-color: #f2bd41;"
                              "border-radius: 0px;")

        btn_connection = QPushButton(self)
        btn_connection.setGeometry(180, 165, 210, 60)
        btn_connection.setFont(jersey25_40)
        btn_connection.setStyleSheet("background-color: #f2bd41;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        btn_connection.setText("CONNECTION")

        btn_inscription_bg = QPushButton(self)
        btn_inscription_bg.setGeometry(405, 170, 220, 50)
        btn_inscription_bg.setStyleSheet("background-color: #bbbcc0;"
                              "border-radius: 0px;")
        btn_inscription_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_inscription_bg.clicked.connect(self.btn_inscription_click)

        btn_inscription = QPushButton(self)
        btn_inscription.setGeometry(410, 165, 210, 60)
        btn_inscription.setFont(jersey25_40)
        btn_inscription.setStyleSheet("background-color: #bbbcc0;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        btn_inscription.setText("INSCRIPTION")
        btn_inscription.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_inscription.clicked.connect(self.btn_inscription_click)

        self.erreur_email = QLabel(self)
        self.erreur_email.setGeometry(185, 302, 430, 20)
        self.erreur_email.setFont(jersey25_16)
        self.erreur_email.setStyleSheet("color: #cc1d10;")
        self.erreur_email.setText("* Cette adresse courriel n'est pas lié à un compte")
        self.erreur_email.hide()

        self.erreur_email_regex = QLabel(self)
        self.erreur_email_regex.setGeometry(185, 302, 430, 20)
        self.erreur_email_regex.setFont(jersey25_16)
        self.erreur_email_regex.setStyleSheet("color: #cc1d10;")
        self.erreur_email_regex.setText("* Adresse courriel invalide")
        self.erreur_email_regex.hide()

        self.veuillez_remplir_email = QLabel(self)
        self.veuillez_remplir_email.setGeometry(185, 302, 430, 20)
        self.veuillez_remplir_email.setFont(jersey25_16)
        self.veuillez_remplir_email.setStyleSheet("color: #cc1d10;")
        self.veuillez_remplir_email.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_email.hide()

        carre_email_bg = QLabel(self)
        carre_email_bg.setGeometry(175, 250, 450, 50)
        carre_email_bg.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        carre_email = QLabel(self)
        carre_email.setGeometry(180, 245, 440, 60)
        carre_email.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        txt_email_connection_bg = QLabel(self)
        txt_email_connection_bg.setGeometry(180, 255, 440, 40)
        txt_email_connection_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        txt_email_connection = QLineEdit(self)
        txt_email_connection.setGeometry(185, 250, 430, 50)
        txt_email_connection.setFont(jersey25_16)
        txt_email_connection.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        txt_email_connection.setPlaceholderText("ADRESSE COURRIEL")
        txt_email_connection.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.erreur_pwd = QLabel(self)
        self.erreur_pwd.setGeometry(185, 382, 200, 20)
        self.erreur_pwd.setFont(jersey25_16)
        self.erreur_pwd.setStyleSheet("color: #cc1d10;")
        self.erreur_pwd.setText("* Mot de passe incorrect")
        self.erreur_pwd.hide()

        self.veuillez_remplir_pwd = QLabel(self)
        self.veuillez_remplir_pwd.setGeometry(185, 382, 200, 20)
        self.veuillez_remplir_pwd.setFont(jersey25_16)
        self.veuillez_remplir_pwd.setStyleSheet("color: #cc1d10;")
        self.veuillez_remplir_pwd.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_pwd.hide()

        carre_pwd_bg = QLabel(self)
        carre_pwd_bg.setGeometry(175, 330, 450, 50)
        carre_pwd_bg.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        carre_pwd = QLabel(self)
        carre_pwd.setGeometry(180, 325, 440, 60)
        carre_pwd.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        txt_pwd_connection = QLabel(self)
        txt_pwd_connection.setGeometry(180, 335, 440, 40)
        txt_pwd_connection.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        txt_pwd_connection = QLineEdit(self)
        txt_pwd_connection.setGeometry(185, 330, 430, 50)
        txt_pwd_connection.setFont(jersey25_16)
        txt_pwd_connection.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        txt_pwd_connection.setPlaceholderText("MOT DE PASSE")
        txt_pwd_connection.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        txt_pwd_connection.setEchoMode(QLineEdit.EchoMode.Password)

        btn_go_bg = QPushButton(self)
        btn_go_bg.setGeometry(175, 415, 450, 50)
        btn_go_bg.setStyleSheet("background-color: #62a1a6;"
                              "border-radius: 0px;")
        btn_go_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_go_bg.clicked.connect(lambda: self.btn_go_click(txt_email_connection.text(),
                                                         txt_pwd_connection.text()))

        btn_go = QPushButton(self)
        btn_go.setGeometry(180, 410, 440, 60)
        btn_go.setFont(jersey25_40)
        btn_go.setStyleSheet("background-color: #62a1a6;"
                              "border-radius: 0px;"
                              "color: #2F3038")
        btn_go.setText("GO")
        btn_go.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_go.clicked.connect(lambda: self.btn_go_click(txt_email_connection.text(),
                                                         txt_pwd_connection.text()))


        logo = QPixmap("resources/images/logo.png")
        logo_label.setPixmap(logo)
        logo_label.setScaledContents(True)

        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(lambda: self.btn_go_click(txt_email_connection.text(),
                                                         txt_pwd_connection.text()))

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
