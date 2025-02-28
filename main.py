"""Modules"""
import sys
import threading
import scrape
import main_window

def main():
    """Démmarage de l'application"""
    app = main_window.QApplication(sys.argv)
    window = main_window.MainWindow()

    window.show()

    #scrape_thread = threading.Thread(target=scrape.run)
    #scrape_thread.start()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
