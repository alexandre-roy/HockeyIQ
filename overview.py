#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QLabel, QWidget, QListWidget, QListWidgetItem, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QDialog
from PyQt6.QtGui import QFontDatabase, QFont, QCursor
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl
import bd
import utils

class VideoPopup(QDialog):
    """Popup window to play the video"""
    def __init__(self, video_path, parent=None):
        super().__init__(parent)
        self.setGeometry(435, 300, 600, 400)

        self.border_label = QLabel(self)
        self.border_label.setGeometry(0,0,0,0)
        self.border_label.setStyleSheet("background-color: #f2bd41;")

        self.media_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.media_player.setAudioOutput(self.audio_output)

        self.video_widget = QVideoWidget(self)
        self.video_widget.setGeometry(30, 30, 555, 365)
        self.media_player.setVideoOutput(self.video_widget)

        layout = QVBoxLayout(self)
        layout.addWidget(self.video_widget)

        self.media_player.setSource(QUrl.fromLocalFile(video_path))
        self.media_player.play()

class Overview(QWidget):
    """Page d'overview"""
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.initialiser_page_overview()

    def initialiser_page_overview(self):
        """Interface graphique"""
        utils.show_menu_icons(self, 3)

        categorie = 'B2'

        QFontDatabase.addApplicationFont("Resources/Fonts/Jersey25-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/Fonts/Inter-VariableFont_opsz,wght.ttf")

        self.jersey25_64 = QFont("jersey 25", 64)
        self.jersey25_32 = QFont("jersey 25", 38)
        self.jersey25_16 = QFont("jersey 25", 16)

        utils.show_boutons_categories(self, 0)

        label_sommaire_bg = QLabel(self)
        label_sommaire_bg.setGeometry(20, 20, 300, 40)
        label_sommaire_bg.setText("Sommaire")
        label_sommaire_bg.setFont(self.jersey25_64)
        label_sommaire_bg.setStyleSheet("color: #2f3038")

        self.video_button_bg_1 = QPushButton(self)
        self.video_button_bg_1.setGeometry(530, 21, 120, 43)
        self.video_button_bg_1.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.video_button_bg_2 = QPushButton(self)
        self.video_button_bg_2.setGeometry(527, 24, 126, 37)
        self.video_button_bg_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        self.video_button_fg_1 = QPushButton(self)
        self.video_button_fg_1.setGeometry(533, 18, 120, 43)
        self.video_button_fg_1.setStyleSheet("background-color: #62a1a6; border-radius: 0px;")

        self.video_button_fg_2 = QPushButton(self)
        self.video_button_fg_2.setGeometry(530, 21, 126, 37)
        self.video_button_fg_2.setStyleSheet("background-color: #62a1a6; border-radius: 0px;")
        self.video_button_fg_2.clicked.connect(self.open_video_popup)
        self.video_button_fg_2.setFont(self.jersey25_32)
        self.video_button_fg_2.setText("Tutoriel")
        self.video_button_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        label_sommaire = QLabel(self)
        label_sommaire.setGeometry(22, 18, 300, 40)
        label_sommaire.setText("Sommaire")
        label_sommaire.setFont(self.jersey25_64)
        label_sommaire.setStyleSheet("color: #62a1a6;"
                               "background-color: transparent")

        label_equipes_bg = QLabel(self)
        label_equipes_bg.setGeometry(40, 100, 300, 40)
        label_equipes_bg.setText("Top 5 équipes")
        label_equipes_bg.setFont(self.jersey25_32)
        label_equipes_bg.setStyleSheet("color: #2f3038")

        label_equipes = QLabel(self)
        label_equipes.setGeometry(42, 98, 300, 40)
        label_equipes.setText("Top 5 équipes")
        label_equipes.setFont(self.jersey25_32)
        label_equipes.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        label_joueurs_bg = QLabel(self)
        label_joueurs_bg.setGeometry(405, 100, 300, 40)
        label_joueurs_bg.setText("Top 5 joueurs")
        label_joueurs_bg.setFont(self.jersey25_32)
        label_joueurs_bg.setStyleSheet("color: #2f3038")

        label_joueurs = QLabel(self)
        label_joueurs.setGeometry(407, 98, 300, 40)
        label_joueurs.setText("Top 5 joueurs")
        label_joueurs.setFont(self.jersey25_32)
        label_joueurs.setStyleSheet("color: #f2bd41;"
                               "background-color: transparent")

        self.list_equipes = QListWidget(self)
        self.list_equipes.setGeometry(45, 150, 340, 243)
        self.list_equipes.setWordWrap(True)
        self.list_equipes.setStyleSheet("""background-color: #bbbcc0""")

        self.list_joueurs = QListWidget(self)
        self.list_joueurs.setGeometry(410, 150, 340, 243)
        self.list_joueurs.setWordWrap(True)
        self.list_joueurs.setStyleSheet("""background-color: #bbbcc0""")

        self.populer_listes(categorie, self.list_equipes, self.list_joueurs)

    def open_video_popup(self):
        """Ouvre le vidéo"""
        chemin = "Resources/Videos/tutoriel.mov"
        video_popup = VideoPopup(chemin, self)
        video_popup.exec()

    def get_equipes(self, categorie):
        """Récupère les équipes dans la base de données"""
        equipes = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT nom_equipe, matchs_joues, points, victoires_total,
                               defaites, nulles FROM equipes WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

                for ligne in cursor:
                    equipes[ligne["nom_equipe"]] = {
                        "nom_equipe": ligne["nom_equipe"],
                        "matchs_joues": ligne["matchs_joues"],
                        "points": ligne["points"],
                        "victoires_total": ligne["victoires_total"],
                        "defaites": ligne["defaites"],
                        "nulles": ligne["nulles"]
                    }
        return equipes

    def get_joueurs(self, categorie):
        """Récupère les joueurs dans la base de données"""
        joueurs = {}
        with bd.creer_connexion() as connection:
            with connection.get_curseur() as cursor:
                cursor.execute("""SELECT nom, equipe, matchs_joues, points FROM joueurs WHERE categorie = %(categorie)s""",
                                {
                                    "categorie": categorie
                                })

                for ligne in cursor:
                    joueurs[ligne["nom"]] = {
                        "nom" : ligne["nom"],
                        "equipe": ligne["equipe"],
                        "matchs_joues": ligne["matchs_joues"],
                        "points": ligne["points"]
                    }
        return joueurs

    def populer_listes(self, categorie, list_equipes, list_joueurs):
        """Popule les listes du sommaire"""
        list_equipes.clear()
        list_joueurs.clear()

        equipes = self.get_equipes(categorie)

        position = 0

        for _, e in equipes.items():
            position += 1
            frame = QFrame()
            frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")

            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 10, 0, 10)
            layout.setSpacing(0)

            team_label = QLabel(f"{e['nom_equipe']}")
            stats_label = QLabel(f"{e['points']} PTS ({e['victoires_total']} - {e['defaites']} - {e['nulles']})")

            team_label.setFont(self.jersey25_16)
            stats_label.setFont(self.jersey25_16)

            h_layout = QHBoxLayout()
            h_layout.addWidget(team_label)
            h_layout.addStretch()
            h_layout.addWidget(stats_label)

            layout.addLayout(h_layout)

            frame.setLayout(layout)
            frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            item = QListWidgetItem()
            item.setSizeHint(frame.sizeHint())

            list_equipes.addItem(item)
            list_equipes.setItemWidget(item, frame)

            if position == 5:
                break

        joueurs = self.get_joueurs(categorie)

        position = 0
        for _, j in joueurs.items():
            position += 1

            frame = QFrame()
            frame.setStyleSheet("QFrame { background-color: #d9d9d9; margin: 3px;}")

            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 10, 0, 10)
            layout.setSpacing(0)

            player_label = QLabel(f"{j['nom']} - {j['equipe']}")
            stats_label = QLabel(f"{j['points']} PTS ({j['matchs_joues']} MJ)")

            player_label.setFont(self.jersey25_16)
            stats_label.setFont(self.jersey25_16)

            h_layout = QHBoxLayout()
            h_layout.addWidget(player_label)
            h_layout.addStretch()
            h_layout.addWidget(stats_label)

            layout.addLayout(h_layout)

            frame.setLayout(layout)
            frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            item = QListWidgetItem()
            item.setSizeHint(frame.sizeHint())

            list_joueurs.addItem(item)
            list_joueurs.setItemWidget(item, frame)

            if position == 5:
                break