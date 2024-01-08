import time

from PySide6.QtCore import QRunnable, Signal, QThreadPool, QThread, QObject, Slot
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication()


class Foo:
    i = 100


class WorkerSignals(QObject):
    finished = Signal(object)


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def run(self) -> None:
        print(f'runnable thread: {QThread.currentThread()}')
        time.sleep(1)
        obj = Foo()
        print(f'send obj: {obj}')
        self.signals.finished.emit(obj)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        print(f'main thread: {QThread.currentThread()}')
        self.thread_pool = QThreadPool()
        self.worker = Worker()
        self.worker.signals.finished.connect(lambda a: print(f'receive signal {a}'))
        self.thread_pool.start(self.worker)


window = Window()
window.show()
app.exec()
