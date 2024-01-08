from PySide6.QtWidgets import QApplication, \
    QWidget, QPushButton, QDialog, QMainWindow, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPainter

import sys

app = QApplication(sys.argv)


class CustomWidget(QWidget):
    def sizeHint(self):
        return QSize(300, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawLine(0, 50, 100, 50)


custom_widget = CustomWidget()
window = QMainWindow()
window.setCentralWidget(custom_widget)
window.show()

app.exec()
