#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon, QCursor
from PyQt6.QtCore import Qt

def show_boutons_categories(parent, active):
    """Affiche les boutons pour changer de catégorie"""
    spacing = 60
    start_x = 670

    liens = [btn_b2_click, btn_b3_click]

    for i in range(2):
        offset = i * spacing

        bg_noir = QPushButton(parent)
        bg_noir_2 = QPushButton(parent)
        bg_fg = QPushButton(parent)
        bg_fg_2 = QPushButton(parent)

        color = "#bbbcc0"

        if i == active:
            color = "#f2bd41"
            bg_fg_2.setText('B2')
        else:
            bg_noir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_noir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_fg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_fg_2.clicked.connect(lambda _, i=i, p=parent: liens[i](p))
            bg_fg_2.setText('B3')

        bg_noir.setGeometry(start_x + offset, 21, 40, 43)
        bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2.setGeometry(start_x - 3 + offset, 24, 46, 37)
        bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_fg.setGeometry(start_x + 3 + offset, 18, 40, 43)
        bg_fg.setStyleSheet(f"background-color: {color}; border-radius: 0px;")

        bg_fg_2.setGeometry(start_x + offset, 21, 46, 37)
        bg_fg_2.setStyleSheet(f"background-color: {color}; border-radius: 0px;")
        bg_fg_2.setFont(parent.jersey25_32)



def show_menu_icons(parent, active):
    """Affiche les icônes du menu"""
    spacing = 100
    start_x = 75

    icons = ["resources/images/calendar.svg", "resources/images/graph.svg", "resources/images/list.svg", "resources/images/eye.svg", "resources/images/comp.svg", "resources/images/table.svg", "resources/images/account.svg"]

    liens = [btn_calendrier_clicked, btn_stats_clicked, btn_classement_clicked, btn_overview_clicked, btn_comp_clicked, btn_predict_clicked, btn_account_clicked]


    for i in range(7):
        offset = i * spacing

        color = "#bbbcc0"

        bg_noir = QPushButton(parent)
        bg_noir_2 = QPushButton(parent)
        bg_fg = QPushButton(parent)
        bg_fg_2 = QPushButton(parent)

        if i == active:
            color = "#62a1a6"
        else:
            bg_noir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_noir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_fg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_fg_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            bg_fg_2.clicked.connect(lambda _, i=i, p=parent: liens[i](p))

        bg_noir.setGeometry(start_x + offset, 430, 40, 43)
        bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2.setGeometry(start_x - 3 + offset, 433, 46, 37)
        bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_fg.setGeometry(start_x + 3 + offset, 427, 40, 43)
        bg_fg.setStyleSheet(f"background-color: {color}; border-radius: 0px;")

        bg_fg_2.setGeometry(start_x + offset, 430, 46, 37)
        bg_fg_2.setStyleSheet(f"background-color: {color}; border-radius: 0px;")
        bg_fg_2.setIcon(QIcon(icons[i]))
        bg_fg_2.setIconSize(bg_fg_2.size())


def btn_calendrier_clicked(parent):
    """Affiche le calendrier"""
    parent.main_window.afficher_calendrier()

def btn_stats_clicked(parent):
    """Affiche les stats"""
    print("Stats")

def btn_classement_clicked(parent):
    """Affiche le classement"""
    print("Classement")

def btn_overview_clicked(parent):
    """Affiche l'overview"""
    parent.main_window.afficher_overview()

def btn_comp_clicked(parent):
    """Affiche la comparaison"""
    print("Compétition")

def btn_predict_clicked(parent):
    """Affiche les prédictions"""
    print("Prédictions")

def btn_account_clicked(parent):
    """Affiche le compte"""
    print("Compte")

def btn_b2_click(parent):
    """Action lors du click sur le bouton B2"""
    print("B2")

def btn_b3_click(parent):
    """Action lors du click sur le bouton B3"""
    print("B3")