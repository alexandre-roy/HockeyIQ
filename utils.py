#pylint: disable = no-name-in-module

"""Modules"""
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon

def show_menu_icons(parent, active):
    """Affiche les icônes du menu"""
    spacing = 100
    start_x = 80

    icons = ["resources/images/calendar.svg", "resources/images/graph.svg", "resources/images/list.svg", "resources/images/eye.svg", "resources/images/comp.svg", "resources/images/table.svg", "resources/images/account.svg"]


    for i in range(7):
        offset = i * spacing

        color = "#bbbcc0"

        if i == active:
            color = "#62a1a6"

        bg_noir = QPushButton(parent)
        bg_noir.setGeometry(start_x + offset, 430, 40, 43)
        bg_noir.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_noir_2 = QPushButton(parent)
        bg_noir_2.setGeometry(start_x - 3 + offset, 433, 46, 37)
        bg_noir_2.setStyleSheet("background-color: #2f3038; border-radius: 0px;")

        bg_fg = QPushButton(parent)
        bg_fg.setGeometry(start_x + 3 + offset, 427, 40, 43)
        bg_fg.setStyleSheet(f"background-color: {color}; border-radius: 0px;")

        bg_fg_2 = QPushButton(parent)
        bg_fg_2.setGeometry(start_x + offset, 430, 46, 37)
        bg_fg_2.setStyleSheet(f"background-color: {color}; border-radius: 0px;")
        bg_fg_2.setIcon(QIcon(icons[i]))
        bg_fg_2.setIconSize(bg_fg_2.size())
