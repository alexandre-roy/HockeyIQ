#pylint: disable = no-name-in-module

"""Modules"""
import re
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor, QFontDatabase, QFont, QShortcut, QKeySequence
from PyQt6.QtCore import Qt
import bd

class Inscription(QWidget):
    """Page d'inscription"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initialiser_page_inscription()

    def initialiser_page_inscription(self):
        """Interface graphique"""
        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        jersey25_40 = QFont("jersey 25", 40)
        jersey25_16 = QFont("jersey 25", 16)

        logo_label = QLabel(self)
        logo_label.setGeometry(100, 20, 600, 140)

        btn_connection_bg = QPushButton(self)
        btn_connection_bg.setGeometry(175, 170, 220, 50)
        btn_connection_bg.setFont(jersey25_40)
        btn_connection_bg.setStyleSheet("background-color: #bbbcc0;"
                                    "border-radius: 0px;")
        btn_connection_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_connection_bg.clicked.connect(self.btn_connection_click)

        btn_connection = QPushButton(self)
        btn_connection.setGeometry(180, 165, 210, 60)
        btn_connection.setFont(jersey25_40)
        btn_connection.setStyleSheet("background-color: #bbbcc0;"
                                    "border-radius: 0px;"
                                    "color: #2F3038;")
        btn_connection.setText("CONNECTION")
        btn_connection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_connection.clicked.connect(self.btn_connection_click)


        btn_inscription_bg = QPushButton(self)
        btn_inscription_bg.setGeometry(405, 170, 220, 50)
        btn_inscription_bg.setStyleSheet("background-color: #f2bd41;"
                              "border-radius: 0px;")
        btn_inscription_bg.setText("INSCRIPTION")

        btn_inscription = QPushButton(self)
        btn_inscription.setGeometry(410, 165, 210, 60)
        btn_inscription.setFont(jersey25_40)
        btn_inscription.setStyleSheet("background-color: #f2bd41;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        btn_inscription.setText("INSCRIPTION")

        self.erreur_email = QLabel(self)
        self.erreur_email.setGeometry(185, 302, 440, 20)
        self.erreur_email.setFont(jersey25_16)
        self.erreur_email.setStyleSheet("color: #8C322D;")
        self.erreur_email.setText("* Adresse courriel invalide")
        self.erreur_email.hide()

        self.veuillez_remplir_email = QLabel(self)
        self.veuillez_remplir_email.setGeometry(185, 302, 440, 20)
        self.veuillez_remplir_email.setFont(jersey25_16)
        self.veuillez_remplir_email.setStyleSheet("color: #8C322D;")
        self.veuillez_remplir_email.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_email.hide()

        self.email_deja_utilise = QLabel(self)
        self.email_deja_utilise.setGeometry(185, 302, 440, 20)
        self.email_deja_utilise.setFont(jersey25_16)
        self.email_deja_utilise.setStyleSheet("color: #8C322D;")
        self.email_deja_utilise.setText("* Adresse courriel déjà utilisée")
        self.email_deja_utilise.hide()

        carre_email_bg = QLabel(self)
        carre_email_bg.setGeometry(175, 250, 220, 50)
        carre_email_bg.setStyleSheet("background-color: #BBBCC0;"
                            "border-radius: 0px;")

        carre_email = QLabel(self)
        carre_email.setGeometry(180, 245, 210, 60)
        carre_email.setStyleSheet("background-color: #BBBCC0;"
                            "border-radius: 0px;")

        txt_email_inscription_bg = QLabel(self)
        txt_email_inscription_bg.setGeometry(180, 255, 210, 40)
        txt_email_inscription_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;")

        txt_email_inscription = QLineEdit(self)
        txt_email_inscription.setGeometry(185, 250, 200, 50)
        txt_email_inscription.setFont(jersey25_16)
        txt_email_inscription.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "padding: 0px;"
                              "color: #2F3038;")
        txt_email_inscription.setPlaceholderText("ADRESSE COURRIEL")
        txt_email_inscription.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.erreur_nom = QLabel(self)
        self.erreur_nom.setGeometry(415, 302, 440, 20)
        self.erreur_nom.setFont(jersey25_16)
        self.erreur_nom.setStyleSheet("color: #8C322D;")
        self.erreur_nom.setText("* 2 caractères minimum")
        self.erreur_nom.hide()

        self.veuillez_remplir_nom = QLabel(self)
        self.veuillez_remplir_nom.setGeometry(415, 302, 440, 20)
        self.veuillez_remplir_nom.setFont(jersey25_16)
        self.veuillez_remplir_nom.setStyleSheet("color: #8C322D;")
        self.veuillez_remplir_nom.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_nom.hide()

        carre_nom_bg = QLabel(self)
        carre_nom_bg.setGeometry(405, 250, 220, 50)
        carre_nom_bg.setStyleSheet("background-color: #BBBCC0;"
                                    "border-radius: 0px;")

        carre_nom = QLabel(self)
        carre_nom.setGeometry(410, 245, 210, 60)
        carre_nom.setStyleSheet("background-color: #BBBCC0;"
                                    "border-radius: 0px;")

        txt_nom_inscription_bg = QLabel(self)
        txt_nom_inscription_bg.setGeometry(410, 255, 210, 40)
        txt_nom_inscription_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;")

        txt_nom_inscription = QLineEdit(self)
        txt_nom_inscription.setGeometry(415, 250, 200, 50)
        txt_nom_inscription.setFont(jersey25_16)
        txt_nom_inscription.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        txt_nom_inscription.setPlaceholderText("PRÉNOM")
        txt_nom_inscription.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.erreur_pwd = QLabel(self)
        self.erreur_pwd.setGeometry(185, 382, 200, 20)
        self.erreur_pwd.setFont(jersey25_16)
        self.erreur_pwd.setStyleSheet("color: #8C322D;")
        self.erreur_pwd.setText("* 5 caractères et un chiffre min.")
        self.erreur_pwd.hide()

        self.veuillez_remplir_pwd = QLabel(self)
        self.veuillez_remplir_pwd.setGeometry(185, 382, 200, 20)
        self.veuillez_remplir_pwd.setFont(jersey25_16)
        self.veuillez_remplir_pwd.setStyleSheet("color: #8C322D;")
        self.veuillez_remplir_pwd.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_pwd.hide()

        carre_pwd_bg = QLabel(self)
        carre_pwd_bg.setGeometry(175, 330, 220, 50)
        carre_pwd_bg.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        carre_pwd = QLabel(self)
        carre_pwd.setGeometry(180, 325, 210, 60)
        carre_pwd.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        txt_pwd_inscription_bg = QLabel(self)
        txt_pwd_inscription_bg.setGeometry(180, 335, 210, 40)
        txt_pwd_inscription_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        txt_pwd_inscription = QLineEdit(self)
        txt_pwd_inscription.setGeometry(185, 330, 200, 50)
        txt_pwd_inscription.setFont(jersey25_16)
        txt_pwd_inscription.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "padding: 0px;"
                              "color: #2F3038;")
        txt_pwd_inscription.setPlaceholderText("MOT DE PASSE")
        txt_pwd_inscription.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        txt_pwd_inscription.setEchoMode(QLineEdit.EchoMode.Password)


        self.erreur_pwd_confirm = QLabel(self)
        self.erreur_pwd_confirm.setGeometry(415, 382, 200, 20)
        self.erreur_pwd_confirm.setFont(jersey25_16)
        self.erreur_pwd_confirm.setStyleSheet("color: #8C322D;")
        self.erreur_pwd_confirm.setText("* Doit être identique au premier")
        self.erreur_pwd_confirm.hide()

        self.veuillez_remplir_pwd_2 = QLabel(self)
        self.veuillez_remplir_pwd_2.setGeometry(415, 382, 200, 20)
        self.veuillez_remplir_pwd_2.setFont(jersey25_16)
        self.veuillez_remplir_pwd_2.setStyleSheet("color: #8C322D;")
        self.veuillez_remplir_pwd_2.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_pwd_2.hide()

        carre_pwd_confirm_bg = QLabel(self)
        carre_pwd_confirm_bg.setGeometry(405, 330, 220, 50)
        carre_pwd_confirm_bg.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        carre_pwd_confirm = QLabel(self)
        carre_pwd_confirm.setGeometry(410, 325, 210, 60)
        carre_pwd_confirm.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        txt_pwd_inscription_confirm_bg = QLabel(self)
        txt_pwd_inscription_confirm_bg.setGeometry(410, 335, 210, 40)
        txt_pwd_inscription_confirm_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        txt_pwd_inscription_confirm = QLineEdit(self)
        txt_pwd_inscription_confirm.setGeometry(415, 330, 200, 50)
        txt_pwd_inscription_confirm.setFont(jersey25_16)
        txt_pwd_inscription_confirm.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")
        txt_pwd_inscription_confirm.setPlaceholderText("MOT DE PASSE x2")
        txt_pwd_inscription_confirm.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        txt_pwd_inscription_confirm.setEchoMode(QLineEdit.EchoMode.Password)

        btn_go_bg = QPushButton(self)
        btn_go_bg.setGeometry(175, 415, 450, 50)
        btn_go_bg.setStyleSheet("background-color: #62a1a6;"
                              "border-radius: 0px;")
        btn_go_bg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_go_bg.clicked.connect(lambda: self.btn_go_click(txt_email_inscription.text(),
                                                txt_nom_inscription.text(),
                                                txt_pwd_inscription.text(),
                                                txt_pwd_inscription_confirm.text()))

        btn_go = QPushButton(self)
        btn_go.setGeometry(180, 410, 440, 60)
        btn_go.setFont(jersey25_40)
        btn_go.setStyleSheet("background-color: #62a1a6;"
                              "border-radius: 0px;"
                              "color: #2F3038")
        btn_go.setText("GO")
        btn_go.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_go.clicked.connect(lambda: self.btn_go_click(txt_email_inscription.text(),
                                                txt_nom_inscription.text(),
                                                txt_pwd_inscription.text(),
                                                txt_pwd_inscription_confirm.text()))

        self.creation_success = QLabel(self)
        self.creation_success.setGeometry(325, 473, 200, 20)
        self.creation_success.setFont(jersey25_16)
        self.creation_success.setStyleSheet("color: #2bb537;")
        self.creation_success.setText("Compte créé avec succès !")
        self.creation_success.hide()

        logo = QPixmap("resources/images/logo.png")
        logo_label.setPixmap(logo)
        logo_label.setScaledContents(True)

        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(lambda: self.btn_go_click(txt_email_connection.text(),
                                                         txt_pwd_connection.text()))

    def btn_connection_click(self):
        """Action lors du clique sur le bouton CONNECTION"""
        self.main_window.afficher_connection()

    def btn_go_click(self, email, prenom, pwd, pwd2):
        """Action de cliquer sur le bouton GO"""
        valide = True
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        pwd_regex = r'^(?=.*\d)[A-Za-z\d@#$%^&+=!]{5,}$'

        self.veuillez_remplir_email.hide()
        self.veuillez_remplir_nom.hide()
        self.veuillez_remplir_pwd.hide()
        self.veuillez_remplir_pwd_2.hide()

        self.erreur_email.hide()
        self.email_deja_utilise.hide()
        self.erreur_nom.hide()
        self.erreur_pwd.hide()
        self.erreur_pwd_confirm.hide()

        self.creation_success.hide()

        if not email or email.isspace():
            valide = False
            self.veuillez_remplir_email.show()
        elif not re.match(email_regex, email):
            valide = False
            self.erreur_email.show()

        if not prenom or prenom.isspace():
            valide = False
            self.veuillez_remplir_nom.show()
        elif len(prenom) < 2:
            valide = False
            self.erreur_nom.show()

        if not pwd or pwd.isspace():
            valide = False
            self.veuillez_remplir_pwd.show()
        elif not re.match(pwd_regex, pwd):
            valide = False
            self.erreur_pwd.show()

        if not pwd2 or pwd2.isspace():
            valide = False
            self.veuillez_remplir_pwd_2.show()
        elif pwd2 != pwd:
            valide = False
            self.erreur_pwd_confirm.show()

        utilisateur_dictionnaire = {
            "prenom" : prenom,
            "email" : email,
            "mot_de_passe" : pwd
        }

        with bd.creer_connexion() as connection:
            with connection.get_curseur() as c:
                c.execute("SELECT * FROM utilisateurs WHERE email = %(email)s",
                           utilisateur_dictionnaire)
                if c.fetchone():
                    valide = False
                    self.email_deja_utilise.show()

        if valide:
            bd.sql("INSERT INTO utilisateurs (prenom, email, mot_de_passe) VALUES" +
                "(%(prenom)s, %(email)s,  SHA2(%(mot_de_passe)s, 256))", utilisateur_dictionnaire)
            self.creation_success.show()
