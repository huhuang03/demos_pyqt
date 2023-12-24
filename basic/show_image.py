from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        label = QLabel()
        label.setPixmap(QPixmap('11.png'))
        self.setCentralWidget(label)


window = MainWindow()
window.show()

app.exec()
