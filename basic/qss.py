from PySide6.QtWidgets import QApplication, \
    QWidget, QPushButton, QDialog, QLabel

import sys


app = QApplication(sys.argv)
app.setStyleSheet("QLabel {background-color: yellow}")

window = QLabel("hello")
window.show()

app.exec()
