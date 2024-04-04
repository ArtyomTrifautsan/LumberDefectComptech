





from ui.controller import MainWindowController
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap

from src.board_displayer import BoardDisplayer
import sys

if __name__ == "__main__":
    board_displayer = BoardDisplayer()
    app = QApplication(sys.argv)
    w1 = MainWindowController(app_kernel=board_displayer)  # = QtWidgets.QMainWindow()
    w1.show()  # MainWindow.show()
    app.exec()

