#pylint: disable = no-name-in-module

"""Modules"""
import re
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QFontDatabase, QFont, QIcon, QCursor, QPixmap
from PyQt6.QtCore import Qt
import bd
import utils

class Compte(QWidget):
    """Page de compte"""
    def __init__(self, main_window, email):
        super().__init__()
        self.main_window = main_window
        self.message = ""
        self.email = email
        self.initialiser_page_compte()

    def initialiser_page_compte(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 6)

        self.counter_edit = 0

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

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

        bg_noir.setGeometry(670, 21, 40, 43)
        bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2.setGeometry(667, 24, 46, 37)
        bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.bg_fg.setGeometry(673, 18, 40, 43)
        self.bg_fg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.bg_fg_2.setGeometry(670, 21, 46, 37)
        self.bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.bg_fg_2.setFont(self.jersey25_32)
        self.bg_fg_2.setIcon(QIcon("resources/images/save.svg"))
        self.bg_fg_2.setIconSize(self.bg_fg_2.size())
        self.bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bg_fg_2.setToolTip("Sauvegarder")
        self.bg_fg_2.clicked.connect(lambda: self.save_info(self.txt_email.text(), self.txt_nom.text(), self.txt_pwd.text(), self.txt_pwd_confirm.text()))

        bg_noir_supprimer = QPushButton(self)
        bg_noir_2_supprimer = QPushButton(self)
        self.bg_fg_supprimer = QPushButton(self)
        self.bg_fg_2_supprimer = QPushButton(self)

        bg_noir_supprimer.setGeometry(730, 21, 40, 43)
        bg_noir_supprimer.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2_supprimer.setGeometry(727, 24, 46, 37)
        bg_noir_2_supprimer.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.bg_fg_supprimer.setGeometry(733, 18, 40, 43)
        self.bg_fg_supprimer.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

        self.bg_fg_2_supprimer.setGeometry(730, 21, 46, 37)
        self.bg_fg_2_supprimer.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        self.bg_fg_2_supprimer.setFont(self.jersey25_32)
        self.bg_fg_2_supprimer.setIcon(QIcon("resources/images/delete.svg"))
        self.bg_fg_2_supprimer.setIconSize(self.bg_fg_2.size())
        self.bg_fg_2_supprimer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bg_fg_2_supprimer.setToolTip("Supprimer")
        self.bg_fg_2_supprimer.clicked.connect(lambda: self.supprimer_profil())

        self.label_email = QLabel(self)
        self.label_email.setGeometry(50, 160, 200, 50)
        self.label_email.setText("Adresse courriel")
        self.label_email.setFont(self.jersey25_16)
        self.label_email.setStyleSheet("color: #2f3038")

        carre_email_bg = QLabel(self)
        carre_email_bg.setGeometry(45, 205, 345, 50)
        carre_email_bg.setStyleSheet("background-color: #BBBCC0;"
                            "border-radius: 0px;")

        carre_email = QLabel(self)
        carre_email.setGeometry(50, 200, 335, 60)
        carre_email.setStyleSheet("background-color: #BBBCC0;"
                            "border-radius: 0px;")

        txt_email_bg = QLabel(self)
        txt_email_bg.setGeometry(50, 210, 335, 40)
        txt_email_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        self.txt_email = QLineEdit(self)
        self.txt_email.setGeometry(55, 205, 325, 50)
        self.txt_email.setFont(self.jersey25_16)
        self.txt_email.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2f3038;")
        self.txt_email.setPlaceholderText("ADRESSE COURRIEL")
        self.txt_email.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.txt_email.setText(self.get_user_info("email"))
        self.txt_email.setPlaceholderText("COURRIEL")

        self.erreur_email = QLabel(self)
        self.erreur_email.setGeometry(50, 262, 440, 20)
        self.erreur_email.setFont(self.jersey25_16)
        self.erreur_email.setStyleSheet("color: #cc1d10;")
        self.erreur_email.setText("* Adresse courriel invalide")
        self.erreur_email.hide()

        self.veuillez_remplir_email = QLabel(self)
        self.veuillez_remplir_email.setGeometry(50, 262, 440, 20)
        self.veuillez_remplir_email.setFont(self.jersey25_16)
        self.veuillez_remplir_email.setStyleSheet("color: #cc1d10;")
        self.veuillez_remplir_email.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_email.hide()

        self.email_deja_utilise = QLabel(self)
        self.email_deja_utilise.setGeometry(50, 262, 440, 20)
        self.email_deja_utilise.setFont(self.jersey25_16)
        self.email_deja_utilise.setStyleSheet("color: #cc1d10;")
        self.email_deja_utilise.setText("* Adresse courriel déjà utilisée")
        self.email_deja_utilise.hide()

        self.label_nom = QLabel(self)
        self.label_nom.setGeometry(410, 160, 200, 50)
        self.label_nom.setText("Prénom")
        self.label_nom.setFont(self.jersey25_16)
        self.label_nom.setStyleSheet("color: #2f3038")

        carre_nom_bg = QLabel(self)
        carre_nom_bg.setGeometry(405, 205, 345, 50)
        carre_nom_bg.setStyleSheet("background-color: #BBBCC0;"
                                    "border-radius: 0px;")

        carre_nom = QLabel(self)
        carre_nom.setGeometry(410, 200, 335, 60)
        carre_nom.setStyleSheet("background-color: #BBBCC0;"
                                    "border-radius: 0px;")

        txt_nom_bg = QLabel(self)
        txt_nom_bg.setGeometry(410, 210, 335, 40)
        txt_nom_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;")

        self.txt_nom = QLineEdit(self)
        self.txt_nom.setGeometry(415, 205, 325, 50)
        self.txt_nom.setFont(self.jersey25_16)
        self.txt_nom.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2f3038;")
        self.txt_nom.setText(self.get_user_info("prenom"))
        self.txt_nom.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.txt_nom.setPlaceholderText("PRÉNOM")

        self.erreur_nom = QLabel(self)
        self.erreur_nom.setGeometry(410, 262, 440, 20)
        self.erreur_nom.setFont(self.jersey25_16)
        self.erreur_nom.setStyleSheet("color: #cc1d10;")
        self.erreur_nom.setText("* 2 caractères minimum")
        self.erreur_nom.hide()

        self.veuillez_remplir_nom = QLabel(self)
        self.veuillez_remplir_nom.setGeometry(410, 262, 440, 20)
        self.veuillez_remplir_nom.setFont(self.jersey25_16)
        self.veuillez_remplir_nom.setStyleSheet("color: #cc1d10;")
        self.veuillez_remplir_nom.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_nom.hide()

        label_pwd = QLabel(self)
        label_pwd.setGeometry(50, 280, 200, 50)
        label_pwd.setText("Nouveau mot de passe")
        label_pwd.setFont(self.jersey25_16)
        label_pwd.setStyleSheet("color: #2f3038")

        carre_pwd_bg = QLabel(self)
        carre_pwd_bg.setGeometry(45, 325, 345, 50)
        carre_pwd_bg.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        carre_pwd = QLabel(self)
        carre_pwd.setGeometry(50, 320, 335, 60)
        carre_pwd.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        txt_pwd_bg = QLabel(self)
        txt_pwd_bg.setGeometry(50, 330, 335, 40)
        txt_pwd_bg.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        self.txt_pwd = QLineEdit(self)
        self.txt_pwd.setGeometry(55, 325, 325, 50)
        self.txt_pwd.setFont(self.jersey25_16)
        self.txt_pwd.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "padding: 0px;"
                              "color: #2F3038;")
        self.txt_pwd.setPlaceholderText("MOT DE PASSE")
        self.txt_pwd.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.txt_pwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.erreur_pwd = QLabel(self)
        self.erreur_pwd.setGeometry(50, 382, 200, 20)
        self.erreur_pwd.setFont(self.jersey25_16)
        self.erreur_pwd.setStyleSheet("color: #cc1d10;")
        self.erreur_pwd.setText("* 5 caractères et un chiffre min.")
        self.erreur_pwd.hide()

        self.veuillez_remplir_pwd = QLabel(self)
        self.veuillez_remplir_pwd.setGeometry(50, 382, 200, 20)
        self.veuillez_remplir_pwd.setFont(self.jersey25_16)
        self.veuillez_remplir_pwd.setStyleSheet("color: #cc1d10;")
        self.veuillez_remplir_pwd.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_pwd.hide()

        label_pwd_confirm = QLabel(self)
        label_pwd_confirm.setGeometry(410, 280, 250, 50)
        label_pwd_confirm.setText("Confirmation du nouveau mot de passe")
        label_pwd_confirm.setFont(self.jersey25_16)
        label_pwd_confirm.setStyleSheet("color: #2f3038")

        carre_pwd_bg_confirm = QLabel(self)
        carre_pwd_bg_confirm.setGeometry(405, 325, 345, 50)
        carre_pwd_bg_confirm.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        carre_pwd_confirm = QLabel(self)
        carre_pwd_confirm.setGeometry(410, 320, 335, 60)
        carre_pwd_confirm.setStyleSheet("background-color: #BBBCC0;"
                              "border-radius: 0px;")

        txt_pwd_bg_confirm = QLabel(self)
        txt_pwd_bg_confirm.setGeometry(410, 330, 335, 40)
        txt_pwd_bg_confirm.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "color: #2F3038;")

        self.txt_pwd_confirm = QLineEdit(self)
        self.txt_pwd_confirm.setGeometry(415, 325, 325, 50)
        self.txt_pwd_confirm.setFont(self.jersey25_16)
        self.txt_pwd_confirm.setStyleSheet("background-color: #D9D9D9;"
                              "border-radius: 0px;"
                              "padding: 0px;"
                              "color: #2F3038;")
        self.txt_pwd_confirm.setPlaceholderText("MOT DE PASSE x2")
        self.txt_pwd_confirm.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.txt_pwd_confirm.setEchoMode(QLineEdit.EchoMode.Password)

        self.erreur_pwd_confirm = QLabel(self)
        self.erreur_pwd_confirm.setGeometry(410, 382, 200, 20)
        self.erreur_pwd_confirm.setFont(self.jersey25_16)
        self.erreur_pwd_confirm.setStyleSheet("color: #cc1d10;")
        self.erreur_pwd_confirm.setText("* Doit être identique au premier")
        self.erreur_pwd_confirm.hide()

        self.veuillez_remplir_pwd_2 = QLabel(self)
        self.veuillez_remplir_pwd_2.setGeometry(410, 382, 200, 20)
        self.veuillez_remplir_pwd_2.setFont(self.jersey25_16)
        self.veuillez_remplir_pwd_2.setStyleSheet("color: #cc1d10;")
        self.veuillez_remplir_pwd_2.setText("* Veuillez remplir ce champ")
        self.veuillez_remplir_pwd_2.hide()

        self.update_success = QLabel(self)
        self.update_success.setGeometry(315, 393, 200, 20)
        self.update_success.setFont(self.jersey25_16)
        self.update_success.setStyleSheet("color: #2bb537;")
        self.update_success.setText("Compte modifié avec succès !")
        self.update_success.hide()

    def save_info(self, email, prenom, pwd, pwd2):
        """Sauvegarde les informations"""
        confirmation = QMessageBox(self)
        confirmation.setWindowTitle("Confirmation")
        confirmation.setText("Sauvegarder les modifications ?")
        confirmation.setIconPixmap(QIcon("resources/images/save.svg").pixmap(40, 40))
        confirmation.setFont(QFont("jersey 25", 16))
        confirmation.setStyleSheet("color: #2f3038;")

        btn_oui = confirmation.addButton("Oui", QMessageBox.ButtonRole.YesRole)
        btn_oui.setFont(QFont("jersey 25", 16))
        btn_oui.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_oui.setStyleSheet("background-color: #bbbcc0; border-radius: 0px; margin-bottom: 0px;")
        btn_oui.setFixedSize(80, 30)


        btn_annuler = confirmation.addButton("Annuler", QMessageBox.ButtonRole.RejectRole)
        btn_annuler.setFont(QFont("jersey 25", 16))
        btn_annuler.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_annuler.setStyleSheet("background-color: #bbbcc0; border-radius: 0px; margin-bottom: 0px;")
        btn_annuler.setFixedSize(80, 30)

        confirmation.exec()

        if confirmation.clickedButton() == btn_oui:
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

            requete = ""
            utilisateur_dictionnaire = {}

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

            if not pwd and not pwd2:
                utilisateur_dictionnaire = {
                    "prenom": prenom,
                    "email": email,
                    "email2": self.get_user_info("email")
                }
                requete = """
                    UPDATE utilisateurs
                    SET prenom = %(prenom)s, email = %(email)s
                    WHERE email = %(email2)s
                """
            else:
                if not re.match(pwd_regex, pwd):
                    valide = False
                    self.erreur_pwd.show()
                elif pwd2 != pwd:
                    valide = False
                    self.erreur_pwd_confirm.show()
                else:
                    utilisateur_dictionnaire = {
                        "prenom": prenom,
                        "email": email,
                        "mot_de_passe": pwd,
                        "email2": self.get_user_info("email")
                    }
                    requete = """
                        UPDATE utilisateurs
                        SET prenom = %(prenom)s, email = %(email)s, mot_de_passe = SHA2(%(mot_de_passe)s, 256)
                        WHERE email = %(email2)s
                    """

            if valide:
                bd.sql(requete, utilisateur_dictionnaire)

                self.message = "Compte modifié avec succès !"
                self.main_window.afficher_connection()

                self.txt_email.clear()
                self.txt_nom.clear()
                self.txt_pwd.clear()
                self.txt_pwd_confirm.clear()
            else:
                return

    def supprimer_profil(self):
        """Supprime le profil"""
        confirmation = QMessageBox(self)
        confirmation.setWindowTitle("Confirmation")
        confirmation.setText("Supprimer le compte ?")
        confirmation.setIconPixmap(QIcon("resources/images/delete.svg").pixmap(40, 40))
        confirmation.setFont(QFont("jersey 25", 16))
        confirmation.setStyleSheet("color: #2f3038;")

        btn_oui = confirmation.addButton("Oui", QMessageBox.ButtonRole.YesRole)
        btn_oui.setFont(QFont("jersey 25", 16))
        btn_oui.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_oui.setStyleSheet("background-color: #bbbcc0; border-radius: 0px; margin-bottom: 0px;")
        btn_oui.setFixedSize(80, 30)


        btn_annuler = confirmation.addButton("Annuler", QMessageBox.ButtonRole.RejectRole)
        btn_annuler.setFont(QFont("jersey 25", 16))
        btn_annuler.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_annuler.setStyleSheet("background-color: #bbbcc0; border-radius: 0px; margin-bottom: 0px;")
        btn_annuler.setFixedSize(80, 30)

        confirmation.exec()

        if confirmation.clickedButton() == btn_oui:
            with bd.creer_connexion() as connection:
                with connection.get_curseur() as cursor:
                    cursor.execute("""DELETE FROM utilisateurs WHERE email = %(email)s""",
                                {
                                    "email": self.email
                                })
            self.message = "Compte supprimé avec succès !"
            self.main_window.afficher_connection()
        else:
            return

    def get_user_info(self, element):
        """Récupère les informations de l'utilisateur"""
        user_info = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_utilisateur, prenom, email, mot_de_passe
                                FROM utilisateurs
                                WHERE email = %(email)s""",
                            {"email": self.email})
                for ligne in cursor:
                    user_info[ligne["id_utilisateur"]] = {
                        "prenom": ligne["prenom"],
                        "email": ligne["email"],
                        "mot_de_passe": ligne["mot_de_passe"]
                    }

        if element:
            for _, info in user_info.items():
                return info.get(element, None)

        return user_info
