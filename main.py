from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("practice.ui", self)

        self.textEdit = self.findChild(QLabel, "message")
        self.button = self.findChild(QPushButton, "pressMe")
        self.button.clicked.connect(self.pressed)


        self.show()

    def pressed(self):
        self.textEdit.setText("Press me")

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()