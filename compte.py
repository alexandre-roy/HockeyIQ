#pylint: disable = no-name-in-module

"""Modules"""
import hashlib
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QLineEdit
from PyQt6.QtGui import QFontDatabase, QFont, QIcon, QCursor
from PyQt6.QtCore import Qt
import bd
import utils
from connection import Connection
import main_window

class Compte(QWidget):
    """Page de compte"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

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
        self.bg_fg_2.clicked.connect(lambda: self.save_info())

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
        self.label_email.setStyleSheet("color: #2bb537")

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
        self.txt_email.textChanged.connect(
            lambda: self.verifier_mot(self.txt_email.text(), self.get_user_info("email"), self.label_email)
        )

        self.label_nom = QLabel(self)
        self.label_nom.setGeometry(410, 160, 200, 50)
        self.label_nom.setText("Prénom")
        self.label_nom.setFont(self.jersey25_16)
        self.label_nom.setStyleSheet("color: #2bb537")

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
        self.txt_nom.textChanged.connect(lambda: self.verifier_mot(self.txt_nom.text(), self.get_user_info("prenom"), self.label_nom))

        label_pwd_current = QLabel(self)
        label_pwd_current.setGeometry(50, 280, 200, 50)
        label_pwd_current.setText("Nouveau mot de passe")
        label_pwd_current.setFont(self.jersey25_16)
        label_pwd_current.setStyleSheet("color: #2bb537")

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
        self.txt_pwd.setPlaceholderText("NOUVEAU MOT DE PASSE")
        self.txt_pwd.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.txt_pwd.setEchoMode(QLineEdit.EchoMode.Password)

        label_pwd_confirm = QLabel(self)
        label_pwd_confirm.setGeometry(410, 280, 250, 50)
        label_pwd_confirm.setText("Confirmation du nouveau mot de passe")
        label_pwd_confirm.setFont(self.jersey25_16)
        label_pwd_confirm.setStyleSheet("color: #2bb537")

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
        self.txt_pwd_confirm.setPlaceholderText("CONFIRMATION")
        self.txt_pwd_confirm.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.txt_pwd_confirm.setEchoMode(QLineEdit.EchoMode.Password)

        barre_mdp_bg2 = QLabel(self)
        barre_mdp_bg2.setGeometry(482, 103, 265, 40)
        barre_mdp_bg2.setStyleSheet("""background-color: #2f3038""")

        barre_mdp_bg = QLabel(self)
        barre_mdp_bg.setGeometry(485, 100, 265, 40)
        barre_mdp_bg.setStyleSheet("""background-color: #bbbcc0""")

        self.barre_mdp = QLineEdit(self)
        self.barre_mdp.setGeometry(490, 105, 220, 30)
        self.barre_mdp.setStyleSheet("""background-color: #d9d9d9;
                                        border-radius: 0px;
                                        padding-left: 5px;""")
        self.barre_mdp.setFont(self.jersey25_16)
        self.barre_mdp.setPlaceholderText("ANCIEN MOT DE PASSE")
        self.barre_mdp.setEchoMode(QLineEdit.EchoMode.Password)

        barre_mdp_square = QLabel(self)
        barre_mdp_square.setStyleSheet("""background-color: #bbbcc0;
                                            border-radius: 0px;""")
        barre_mdp_square.setGeometry(715, 105, 30, 30)

        self.square = QLabel(self)
        self.square.setStyleSheet("""background-color: #cc1d10;
                                border-radius: 0px;""")
        self.square.setGeometry(715, 105, 30, 30)

        self.barre_mdp.textChanged.connect(
            lambda: self.verifier_mdp(self.barre_mdp.text(), self.get_user_info("mot_de_passe"))
        )

    def verifier_mot(self, mot, mot_db, label):
        """Vérifie le mot de passe"""
        if mot == mot_db:
            label.setStyleSheet("color: #2bb537;")
        else:
            label.setStyleSheet("color: #cc1d10;")

    def verifier_mdp(self, mdp, mdp_db):
        """Véfifie le mot de passe"""
        mdp_hash = hashlib.sha256(mdp.encode()).hexdigest()
        if mdp_hash == mdp_db:
            self.square.setStyleSheet("""background-color: #2bb537;
                                border-radius: 0px;""")
            return True
        else:
            self.square.setStyleSheet("""background-color: #cc1d10;
                                border-radius: 0px;""")
            return False


    def save_info(self):
        """Sauvegarde les informations"""
        print("Sauvegarde des informations")

    def supprimer_profil(self):
        """Supprime le profil"""
        if self.verifier_mdp(self.barre_mdp.text(), self.get_user_info("mot_de_passe")):
            with bd.creer_connexion() as connection:
                with connection.get_curseur() as cursor:
                    cursor.execute("""DELETE FROM utilisateurs WHERE email = %(email)s""",
                                {
                                    "email": Connection.email
                                })
            self.main_window.afficher_connection()
        else:
            print("Mot de passe incorrect")

    def get_user_info(self, element):
        """Récupère les informations de l'utilisateur"""
        user_info = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT id_utilisateur, prenom, email, mot_de_passe
                                FROM utilisateurs
                                WHERE email = %(email)s""",
                            {"email": Connection.email})
                for ligne in cursor:
                    user_info[ligne["id_utilisateur"]] = {
                        "prenom": ligne["prenom"],
                        "email": ligne["email"],
                        "mot_de_passe": ligne["mot_de_passe"]
                    }

        if not user_info:
            print("No user info found for email:", Connection.email)
            return None

        if element:
            for _, info in user_info.items():
                return info.get(element, None)

        return user_info
