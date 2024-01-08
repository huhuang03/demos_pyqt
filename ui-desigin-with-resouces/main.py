import sys
from pathlib import Path

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPixmap
root_path = Path(__file__).parent
loader = QUiLoader()
from gen_main_window import Ui_MainWindow


app = QApplication(sys.argv)
window: Ui_MainWindow = loader.load(root_path / 'main_window.ui')
window.lb.setPixmap(QPixmap(':/icons/11.png'))
print(f'window type: {type(window)}')
window.show()
app.exec()