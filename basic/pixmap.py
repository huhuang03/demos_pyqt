from PySide6.QtWidgets import QApplication, \
    QWidget, QPushButton, QDialog, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.label.setPixmap(self.canvas)


window = MainWindow()
window.show()

app.exec()
