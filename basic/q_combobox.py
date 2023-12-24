from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        comboBox = QComboBox()
        comboBox.setEditable(True)
        comboBox.insertItems(0, ["aa", "bb", "cc"])
        self.setCentralWidget(comboBox)


window = MainWindow()
window.show()

app.exec()
