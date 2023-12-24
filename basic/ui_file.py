import sys
from PySide6 import QtWidgets
from pathlib import Path
from PySide6.QtUiTools import QUiLoader

root_path = Path(__file__).parent.parent.resolve()

loader = QUiLoader()


app = QtWidgets.QApplication(sys.argv)
window = loader.load(root_path / 'demo_ui.ui')
window.show()

app.exec()