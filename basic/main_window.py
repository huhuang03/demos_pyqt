from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

import sys

app = QApplication(sys.argv)


# window = QMainWindow()
# window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.setChecked(self.button_is_checked)
        self.button.released.connect(self.the_button_was_released)
        self.setCentralWidget(self.button)
        self.setFixedSize(QSize(400, 300))

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


window = MainWindow()
window.show()

app.exec()
