import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        label = QLabel("Hello, World!", self)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        button = QPushButton("OK")
        self.setMenuWidget(button)

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec()