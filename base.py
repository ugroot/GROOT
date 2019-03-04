from PyQt5.QtWidgets import QApplication
import sys

from Gui import Groot_Ui


if __name__ == '__main__':
    app = QApplication(sys.argv)
    groot = Groot_Ui()   #! Groot UI defined in the ui.py file
    sys.exit(app.exec_())
