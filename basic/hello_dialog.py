from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PySide6.QtCore import QSize

import sys

app = QApplication(sys.argv)


# window = QMainWindow()
# window.show()

class ConfirmDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel |
                                          QDialogButtonBox.StandardButton.Abort)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_released)
        self.setCentralWidget(self.button)
        self.setFixedSize(QSize(400, 300))

    def the_button_was_released(self):
        dialog = ConfirmDialog(self)
        rst = dialog.exec()
        print('rst: ', rst)


window = MainWindow()
window.show()

app.exec()
