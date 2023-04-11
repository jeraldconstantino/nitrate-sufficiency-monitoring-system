from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic, QtCore
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		
		# Load the ui file
		uic.loadUi("main.ui", self)
		
        # Make the main window frameless
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		

		self.show()

# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()