#pylint: disable = no-name-in-module

"""Modules"""
import re
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QCursor
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

        self.erreur_email = QLabel(self)
        self.erreur_email.setGeometry(185, 290, 440, 20)
        self.erreur_email.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_email.setText("Adresse courriel invalide")
        self.erreur_email.hide()

        self.veuillez_remplir_email = QLabel(self)
        self.veuillez_remplir_email.setGeometry(185, 290, 440, 20)
        self.veuillez_remplir_email.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.veuillez_remplir_email.setText("Veuillez remplir ce champ")
        self.veuillez_remplir_email.hide()

        self.email_deja_utilise = QLabel(self)
        self.email_deja_utilise.setGeometry(185, 290, 440, 20)
        self.email_deja_utilise.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.email_deja_utilise.setText("Courriel déjà utilisé")
        self.email_deja_utilise.hide()

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

        self.erreur_nom = QLabel(self)
        self.erreur_nom.setGeometry(415, 290, 440, 20)
        self.erreur_nom.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_nom.setText("2 caractères minimum")
        self.erreur_nom.hide()

        self.veuillez_remplir_nom = QLabel(self)
        self.veuillez_remplir_nom.setGeometry(415, 290, 440, 20)
        self.veuillez_remplir_nom.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.veuillez_remplir_nom.setText("Veuillez remplir ce champ")
        self.veuillez_remplir_nom.hide()

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

        self.erreur_pwd = QLabel(self)
        self.erreur_pwd.setGeometry(185, 375, 200, 20)
        self.erreur_pwd.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_pwd.setText("5 caractères et un chiffre minimum")
        self.erreur_pwd.hide()

        self.veuillez_remplir_pwd = QLabel(self)
        self.veuillez_remplir_pwd.setGeometry(185, 375, 200, 20)
        self.veuillez_remplir_pwd.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.veuillez_remplir_pwd.setText("Veuillez remplir ce champ")
        self.veuillez_remplir_pwd.hide()

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

        self.erreur_pwd_confirm = QLabel(self)
        self.erreur_pwd_confirm.setGeometry(415, 375, 200, 20)
        self.erreur_pwd_confirm.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.erreur_pwd_confirm.setText("Doit être identique au premier")
        self.erreur_pwd_confirm.hide()

        self.veuillez_remplir_pwd_2 = QLabel(self)
        self.veuillez_remplir_pwd_2.setGeometry(415, 375, 200, 20)
        self.veuillez_remplir_pwd_2.setStyleSheet("color: #e8873d;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.veuillez_remplir_pwd_2.setText("Veuillez remplir ce champ")
        self.veuillez_remplir_pwd_2.hide()

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
        btn_go.clicked.connect(lambda: self.btn_go_click(txt_email_inscription.text(),
                                                txt_nom_inscription.text(),
                                                txt_pwd_inscription.text(),
                                                txt_pwd_inscription_confirm.text()))

        self.creation_success = QLabel(self)
        self.creation_success.setGeometry(330, 460, 200, 20)
        self.creation_success.setStyleSheet("color: #2bb537;"
                                   "font-size: 11px;"
                                   "font-weight: Bold;")
        self.creation_success.setText("Compte créé avec succès!")
        self.creation_success.hide()

        logo = QPixmap("resources/logo.png")
        logo_label.setPixmap(logo)
        logo_label.setScaledContents(True)

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
