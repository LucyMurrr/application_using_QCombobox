import sys
from PyQt5.QtWidgets import QApplication
from views import MainView
from config import create_connection

def main():
    create_connection()
    if not create_connection():
        sys.exit(-1)

    app = QApplication(sys.argv)
    main_window = MainView()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()