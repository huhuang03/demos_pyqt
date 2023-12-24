from PySide6.QtWidgets import QApplication, \
    QMainWindow, QPushButton, QLabel, QToolBar, QStatusBar
from PySide6.QtGui import QPixmap, QAction, QIcon, QKeySequence
from PySide6.QtCore import QSize, Qt

import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello")
        self.setCentralWidget(label)

        toolbar = QToolBar("main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon('bug.png'),
            'Your button', self)
        button_action.setCheckable(True)
        # ctrl + a not work, but alt + a works
        button_action.setShortcut(QKeySequence(Qt.Modifier.CTRL | Qt.Key_A))
        button_action.setShortcut(QKeySequence(Qt.Modifier.ALT | Qt.Key_A))
        button_action.setStatusTip('this is a action button')
        button_action.triggered.connect(lambda: print('hello'))
        toolbar.addAction(button_action)
        self.setStatusBar(QStatusBar())

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)


window = MainWindow()
window.show()

app.exec()
