import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()