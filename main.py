######################################################################################################
# TODO: 
#       - Set Time btn should store the edited time to the local database.
#       - Fish feeding section should color in red pastel when the inference result is deficient.
#       - Go Live! btn can be removed, and the capture should automatically turned to live detection.
#       - Live detection.
#       - Time schedule should display four schedules in case of deficient.
#       - Capture and Show folder btns.
#       - Add a Close btn.
######################################################################################################

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog, QMessageBox, QTimeEdit, QDesktopWidget
from PyQt5.QtGui import QFont
from RPiDevices.fishFeeder import feedNow
from PyQt5.QtCore import QTime, QTimer
from PyQt5 import uic, QtCore
from datetime import datetime
import sys

# Declaration of the UI files
mainWindowUI = "main.ui"
feedingScheduleDialogUI = "feedingScheduleDialog.ui"

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		
		# Load the ui file
		uic.loadUi(mainWindowUI, self)
		
		# Make the main window frameless
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		
		# QLabel widget
		self.timeLabel = self.findChild(QLabel, "timeLabel")
		self.dateLabel = self.findChild(QLabel, "dateLabel")
		self.firstSchedResult = self.findChild(QLabel, "firstSchedResult")
		self.secondSchedResult = self.findChild(QLabel, "secondSchedResult")
		self.class_result = self.findChild(QLabel, "classificationResultLabel")
		self.fishFeedingStatusResult = self.findChild(QLabel, "fishFeedingStatusResult")

		# QPushButtons widget
		self.feedNowBtn = self.findChild(QPushButton, "feedNowBtn")
		self.setTimeBtn = self.findChild(QPushButton, "setTimeBtn")

		self.feedNowBtn.setStyleSheet("""
			QPushButton {
				background-color: #287194;
				color: #fff;
				border-radius: 15px;
				padding: 10px 25px;
				font: bold 12pt "Poppins";
			}

			QPushButton:hover {
				background-color: #1F5773;
			}

			QPushButton:pressed {
				background-color: #193D4D;
			}
		""")

		self.setTimeBtn.setStyleSheet("""
			QPushButton {
				background-color: #287194;
				color: #fff;
				border-radius: 15px;
				padding: 10px 25px;
				font: bold 12pt "Poppins";
			}

			QPushButton:hover {
				background-color: #1F5773;
			}

			QPushButton:pressed {
				background-color: #193D4D;
			}
		""")

		#Change the time stamp display per second
		self.timer = QTimer()
		self.timer.timeout.connect(self.fishFeedingSchedCounter)
		self.timer.start(1000) # Timer updates every 1 second
		self.fishFeedingSchedCounter()

		# Trigger the Fish Feeding Device to operate
		self.feedNowBtn.clicked.connect(feedNow)

		# Open the dialog when "SET TIME" button is clicked.
		self.setTimeBtn.clicked.connect(self.openFeedingScheduleDialog)
		self.show()

	def fishFeedingSchedCounter(self):
		raw_current_datetime = datetime.now()
		formatted_current_date = raw_current_datetime.strftime("%B %d, %Y (%A)")
		formatted_current_time = raw_current_datetime.strftime("%I:%M:%S %p")
		
		self.dateLabel.setText(formatted_current_date)
		self.timeLabel.setText(formatted_current_time)

		# Acquired feeding time for morning and afternoon schedule
		raw_first_feeding_sched = datetime.strptime(self.firstSchedResult.text(), "%I:%M %p")
		raw_second_feeding_sched = datetime.strptime(self.secondSchedResult.text(), "%I:%M %p")

		first_feeding_sched = raw_first_feeding_sched.strftime("%I:%M:%S %p")
		second_feeding_sched = raw_second_feeding_sched.strftime("%I:%M:%S %p")
		
		if (formatted_current_time == first_feeding_sched or formatted_current_time == second_feeding_sched):
			feedNow()

		# Updates the fish feeding status based on the inference result.
		class_result = self.classificationResultLabel.text()
		if (class_result.lower() == "deficient"):
			self.fishFeedingStatusResult.setText("Four times a day")
		else:
			self.fishFeedingStatusResult.setText("Twice a day") 

	def openFeedingScheduleDialog(self):
		self.dialog = QDialog(self)
		uic.loadUi(feedingScheduleDialogUI, self.dialog)

		self.dialog.setGeometry(300, 150, 300, 300) # set the position of  the dialog

		self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Make the main window frameless 
		self.dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground) # make the background translucent

		# Access the QTimeEdit widget
		self.firstSchedTime = self.dialog.findChild(QTimeEdit, "firstSchedTime")
		self.secondSchedTime = self.dialog.findChild(QTimeEdit, "secondSchedTime")

		# Set the first QTime edit based on the current first schedule
		first_feeding_sched_edit = QTime.fromString(self.firstSchedResult.text(), 'h:mm AP')
		self.firstSchedTime.setTime(first_feeding_sched_edit)

		# Set the second QTime edit based on the current first schedule
		second_feeding_sched_edit = QTime.fromString(self.secondSchedResult.text(), 'h:mm AP')
		self.secondSchedTime.setTime(second_feeding_sched_edit)

		# self.setTimeBtn.clicked.connect(lambda: self.setTime(self, firstSchedTimeMW, secondSchedTimeMW))
		setTimeBtn = self.dialog.findChild(QPushButton, "setTimeBtn")
		setTimeBtn.clicked.connect(self.setTime)

		# Close the SET TIME dialog
		cancelTimeBtn = self.dialog.findChild(QPushButton, "cancelTimeBtn")
		cancelTimeBtn.clicked.connect(self.dialog.reject)

		# Show the dialog
		self.setTimeBtn.setEnabled(False)
		self.feedNowBtn.setEnabled(False)
		self.dialog.exec_()
		self.setTimeBtn.setEnabled(True)
		self.feedNowBtn.setEnabled(True)


	def setTime(self):
		# Get the time from the QTimeEdit widget as a QTime object and converted to String.	
		editted_first_sched = self.firstSchedTime.time()
		editted_first_sched_str = editted_first_sched.toString('h:mm AP')

		editted_second_sched = self.secondSchedTime.time()
		editted_second_sched_str = editted_second_sched.toString('h:mm AP')
		
		isValidTime = self.validateTime(editted_first_sched_str, editted_second_sched_str)

		if isValidTime == True:
			# Set the editted time to the Time Schedule display.
			self.firstSchedResult.setText(editted_first_sched_str)
			self.secondSchedResult.setText(editted_second_sched_str)
			self.dialog.reject()
		else:
			self.openInvalidInputDialog()
		
	def validateTime(self, firstSchedTime, secondSchedTime):
		if firstSchedTime == secondSchedTime:
			return False
		return True
	
	def openInvalidInputDialog(self):
		self.msg_box = QMessageBox()
		self.msg_box.setIcon(QMessageBox.Warning)
		self.msg_box.setText("WARNING:\n\n The first and second schedules must not be at the same time.")
		
		# Customized QMessageBox() 
		font = QFont('Poppins', 12)
		self.msg_box.setFont(font)
		self.msg_box.setStyleSheet("""
				QMessageBox {
						background-color: rgb(250, 160, 160);
				}
				QMessageBox QLabel {
						qproperty-alignment: AlignCenter;
				}
		""")

		ok_button = self.msg_box.addButton(QMessageBox.Ok)
		ok_button.setStyleSheet("""
				QPushButton {
						background-color: #F44336;
						color: #fff;
						border-radius: 15px;
						padding: 10px 25px;
						font: bold 10pt "Poppins";
				}
		""")
		self.msg_box.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.msg_box.exec_()

# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()