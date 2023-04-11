from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		
		# Load the ui file
		uic.loadUi("main.ui", self)

		self.show()

# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()