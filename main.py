"""Modules"""
import sys
import scrape
import main_window

def main():
    """Démmarage de l'application"""
    app = main_window.QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    scrape.run()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
