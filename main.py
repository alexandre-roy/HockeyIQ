import scrape
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HockeyIQ")
        self.setGeometry(325, 225, 800, 500)

        label = QLabel("Hello World", self)
        label.setFont(QFont("JetBrains Mono", 12))
        label.margin()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys .exit(app.exec())

if __name__ == "__main__":
    main()
    scrape()

