#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QCursor, QPixmap
from PyQt6.QtCore import Qt

def show_boutons_categories(parent, active):
    """Affiche les boutons pour changer de catégorie"""
    spacing = 60
    start_x = 670

    liens = [btn_b2_click, btn_b3_click]

    parent.bg_noir_1 = QPushButton(parent)
    parent.bg_noir_1.setGeometry(start_x, 21, 40, 43)
    parent.bg_noir_1.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

    parent.bg_noir_1_2 = QPushButton(parent)
    parent.bg_noir_1_2.setGeometry(start_x - 3, 24, 46, 37)
    parent.bg_noir_1_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

    parent.bg_fg_1 = QPushButton(parent)
    parent.bg_fg_1.setGeometry(start_x + 3, 18, 40, 43)
    parent.bg_fg_1.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

    parent.bg_fg_1_2 = QPushButton(parent)
    parent.bg_fg_1_2.setGeometry(start_x, 21, 46, 37)
    parent.bg_fg_1_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
    parent.bg_fg_1_2.setFont(parent.jersey25_32)
    parent.bg_fg_1_2.setText('B2')
    parent.bg_fg_1_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    parent.bg_fg_1_2.clicked.connect(lambda _, p=parent: liens[0](p))

    parent.bg_noir_2 = QPushButton(parent)
    parent.bg_noir_2.setGeometry(start_x + spacing, 21, 40, 43)
    parent.bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

    parent.bg_noir_2_2 = QPushButton(parent)
    parent.bg_noir_2_2.setGeometry(start_x - 3 + spacing, 24, 46, 37)
    parent.bg_noir_2_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

    parent.bg_fg_2 = QPushButton(parent)
    parent.bg_fg_2.setGeometry(start_x + 3 + spacing, 18, 40, 43)
    parent.bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

    parent.bg_fg_2_2 = QPushButton(parent)
    parent.bg_fg_2_2.setGeometry(start_x + spacing, 21, 46, 37)
    parent.bg_fg_2_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
    parent.bg_fg_2_2.setFont(parent.jersey25_32)
    parent.bg_fg_2_2.setText('B3')
    parent.bg_fg_2_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    parent.bg_fg_2_2.clicked.connect(lambda _, p=parent: liens[1](p))



def show_menu_icons(parent, active):
    """Affiche les icônes du menu"""
    spacing = 100
    start_x = 75

    icons = ["resources/images/calendar.svg", "resources/images/graph.svg", "resources/images/list.svg", "resources/images/eye.svg", "resources/images/comp.svg", "resources/images/table.svg", "resources/images/account.svg"]

    liens = [btn_calendrier_clicked, btn_stats_clicked, btn_classement_clicked, btn_overview_clicked, btn_comp_clicked, btn_predict_clicked, btn_account_clicked]

    titres = ["Caldndriers", "Statistiques", "Classements", "Sommaire", "Face à face", "Mes prédictions", "Mon compte"]

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

            bg_fg_2.setToolTip(titres[i])

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

def show_barre_recherche(parent):
    """Affiche la barre de recherche"""
    barre_recherche_bg2 = QLabel(parent)
    barre_recherche_bg2.setGeometry(482, 103, 265, 40)
    barre_recherche_bg2.setStyleSheet("""background-color: #2f3038""")

    barre_recherche_bg = QLabel(parent)
    barre_recherche_bg.setGeometry(485, 100, 265, 40)
    barre_recherche_bg.setStyleSheet("""background-color: #bbbcc0""")

    barre_recherche = QLineEdit(parent)
    barre_recherche.setGeometry(490, 105, 220, 30)
    barre_recherche.setStyleSheet("""background-color: #d9d9d9;
                                    border-radius: 0px;
                                    padding-left: 5px;""")
    barre_recherche.setFont(parent.jersey25_16)
    barre_recherche.setPlaceholderText("RECHERCHE")

    barre_recherche_loupe = QLabel(parent)
    barre_recherche_loupe.setStyleSheet("""background-color: #bbbcc0;
                                        border-radius: 0px;""")
    barre_recherche_loupe.setGeometry(715, 105, 30, 30)

    loupe = QPixmap("resources/images/search.svg")
    barre_recherche_loupe.setPixmap(loupe)
    barre_recherche_loupe.setScaledContents(True)

    return barre_recherche

def btn_calendrier_clicked(parent):
    """Affiche le calendrier"""
    parent.main_window.afficher_calendrier()

def btn_stats_clicked(parent):
    """Affiche les stats"""
    parent.main_window.afficher_stats()

def btn_classement_clicked(parent):
    """Affiche le classement"""
    parent.main_window.afficher_classement()

def btn_overview_clicked(parent):
    """Affiche l'overview"""
    parent.main_window.afficher_overview()

def btn_comp_clicked(parent):
    """Affiche la comparaison"""
    print("Comparaison")

def btn_predict_clicked(parent):
    """Affiche les prédictions"""
    print("Prédictions")

def btn_account_clicked(parent):
    """Affiche le compte"""
    parent.main_window.afficher_compte()

def btn_b2_click(parent):
    """Action lors du click sur le bouton B2"""
    parent.bg_fg_1.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
    parent.bg_fg_1_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
    parent.bg_fg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
    parent.bg_fg_2_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")

    if hasattr(parent, 'table_classement') and parent.table_classement:
        parent.populer_table(parent.get_equipes('B2'), parent.table_classement)
        parent.table_classement.setStyleSheet("""background-color: #bbbcc0""")
        parent.text_recherche.setText("")
    elif hasattr(parent, 'table_stats') and parent.table_stats:
        parent.populer_table(parent.get_joueurs('B2'), parent.table_stats)
        parent.table_stats.setStyleSheet("""background-color: #bbbcc0""")
        parent.text_recherche.setText("")
    elif hasattr(parent, 'populer_liste') and parent.liste_parties:
        parent.populer_liste(parent.get_parties('B2'), parent.liste_parties, False)
        parent.label_parties.setText("Parties à venir")
        parent.label_parties_bg.setText("Parties à venir")
        parent.bg_fgg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        parent.bg_fgg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        parent.text_recherche.setText("")
    elif hasattr(parent, 'populer_listes') and parent.list_equipes:
        parent.populer_listes('B2', parent.list_equipes, parent.list_joueurs)
        parent.text_recherche.setText("")


def btn_b3_click(parent):
    """Action lors du click sur le bouton B3"""
    parent.bg_fg_1.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
    parent.bg_fg_1_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
    parent.bg_fg_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")
    parent.bg_fg_2_2.setStyleSheet("background-color: #f2bd41; border-radius: 0px;")

    if hasattr(parent, 'table_classement') and parent.table_classement:
        parent.populer_table(parent.get_equipes('B3'), parent.table_classement)
        parent.table_classement.setStyleSheet("""background-color: #bbbcc0""")
        parent.text_recherche.setText("")
    elif hasattr(parent, 'table_stats') and parent.table_stats:
        parent.populer_table(parent.get_joueurs('B3'), parent.table_stats)
        parent.table_stats.setStyleSheet("""background-color: #bbbcc0""")
        parent.text_recherche.setText("")
    elif hasattr(parent, 'populer_liste') and parent.liste_parties:
        parent.populer_liste(parent.get_parties('B3'), parent.liste_parties, False)
        parent.label_parties.setText("Parties à venir")
        parent.label_parties_bg.setText("Parties à venir")
        parent.bg_fgg.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        parent.bg_fgg_2.setStyleSheet("background-color: #bbbcc0; border-radius: 0px;")
        parent.text_recherche.setText("")
    elif hasattr(parent, 'populer_listes') and parent.list_equipes:
        parent.populer_listes('B3', parent.list_equipes, parent.list_joueurs)
        parent.text_recherche.setText("")
