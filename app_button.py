import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton

app = QApplication(sys.argv)

window = QPushButton("Click me!")
window.show()

app.exec()