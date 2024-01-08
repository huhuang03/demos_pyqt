from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QTimer, QThread


app = QApplication()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        print(f'main thread: {QThread.currentThread()}')
        self.counter = 1
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self._update_counter_ui()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._count)
        self.timer.start()

    def _count(self):
        print(f'thread: {QThread.currentThread()}')
        self.counter += 1
        self._update_counter_ui()

    def _update_counter_ui(self):
        self.label.setText(f"Counter: {self.counter}")


print(f'out thread: {QThread.currentThread()}')
window = Window()
window.show()
app.exec()