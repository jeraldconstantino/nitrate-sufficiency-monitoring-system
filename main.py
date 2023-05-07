######################################################################################################
# TODO: 
#       - Set Time btn should store the edited time to the local database.
#       - Fish feeding btns should color in red pastel when the inference result is deficient.
#       - Go Live! btn can be removed, and the capture should automatically turned to live detection.
#       - Live detection.
#
#		If there's more time:
#			FEATURES: Add settings for dropdown list of camera available
#
######################################################################################################

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog, QMessageBox, QTimeEdit, QFrame, QFileDialog
from PyQt5.QtCore import QTime, QTimer, QThread, Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QImage, QPixmap, QDesktopServices
from RPiDevices.fishFeeder import feedNow
from PyQt5 import uic, QtCore
from datetime import datetime
import sys
import cv2
import os

# Declaration of the UI files.
mainWindowUI = "main.ui"
feedingScheduleDialogUI = "feedingScheduleDialog.ui"

# Detection of the location of camera connection.
# Must be modified or calibrated to make it work with other device.
cameraLocation = 0
cameraHorizontalResolution = 1080
cameraVerticalResolution = 720
directory = 'C:/Users/jeral/OneDrive/Desktop/capture/'

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi(mainWindowUI, self)
		
		# Make the main window frameless
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.showFullScreen()

		# QLabel widget
		self.timeLabel = self.findChild(QLabel, "timeLabel")
		self.dateLabel = self.findChild(QLabel, "dateLabel")
		self.firstSchedResult = self.findChild(QLabel, "firstSchedResult")
		self.secondSchedResult = self.findChild(QLabel, "secondSchedResult")
		self.class_result = self.findChild(QLabel, "classificationResultLabel")
		self.fishFeedingStatusResult = self.findChild(QLabel, "fishFeedingStatusResult")
		self.cameraPreview = self.findChild(QLabel, "cameraPreviewHolder")

		# QPushButtons widget
		self.feedNowBtn = self.findChild(QPushButton, "feedNowBtn")
		self.setTimeBtn = self.findChild(QPushButton, "setTimeBtn")
		self.captureBtn = self.findChild(QPushButton, "captureBtn")
		self.liveFeedBtn = self.findChild(QPushButton, "liveFeedBtn")
		self.showFolderBtn = self.findChild(QPushButton, "showFolderBtn")
		self.minimizeBtn = self.findChild(QPushButton, "minimizeBtn")
		self.exitBtn = self.findChild(QPushButton, "exitBtn")

		# Customized button styles
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

		self.captureBtn.setStyleSheet("""
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

		self.liveFeedBtn.setStyleSheet("""
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

		self.showFolderBtn.setStyleSheet("""
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

		self.minimizeBtn.setStyleSheet("""
			QPushButton {
				background-color: #193D4D;
				color: #fff;
				border-radius: 15px;
				padding: 5px 15px;
				font: bold 10pt "Poppins";
			}

			QPushButton:hover {
				background-color: #1F5773;
			}

			QPushButton:pressed {
				background-color: #287194;
			}
		""")

		self.exitBtn.setStyleSheet("""
			QPushButton {
				background-color: #193D4D;
				color: #fff;
				border-radius: 15px;
				padding: 5px 15px;
				font: bold 10pt "Poppins";
			}

			QPushButton:hover {
				background-color: #CD160D;
			}

			QPushButton:pressed {
				background-color: #F45952;
			}
		""")

		# Change the time stamp display per second
		self.timer = QTimer()
		self.timer.timeout.connect(self.fishFeedingSchedCounter)
		self.timer.start(1000) # Timer updates every 1 second
		self.fishFeedingSchedCounter()

		# Trigger the Fish Feeding Device to operate
		self.feedNowBtn.clicked.connect(feedNow)

		# Open the dialog when "SET TIME" button is clicked.
		self.setTimeBtn.clicked.connect(self.openFeedingScheduleDialog)

		self.exitBtn.clicked.connect(QApplication.quit) # Close the App when clicked
		self.minimizeBtn.clicked.connect(self.showMinimized) # Minimize the App when clicked

		# Initialize camera
		self.camera = CameraWidget()
		self.camera.imageUpdate.connect(self.imageUpdateSlot)
		self.camera.start()

		self.captureBtn.clicked.connect(self.saveImage)
		self.showFolderBtn.clicked.connect(self.openFileDialog)
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

		mainFrame = self.findChild(QFrame, "mainFrame")

		# Updates the fish feeding status based on the inference result.
		class_result = self.classificationResultLabel.text()
		if (class_result.lower() == "deficient"):
			self.fishFeedingStatusResult.setText("Four times a day")
			mainFrame.setStyleSheet("""
				QFrame {
					background-color: rgb(250, 160, 160);
					border-top-left-radius: 20px;
					border-top-right-radius: 20px;
				}
			""")
		else:
			self.fishFeedingStatusResult.setText("Twice a day") 
			mainFrame.setStyleSheet("""
				QFrame {
					background-color: rgb(211, 212, 206);
					border-top-left-radius: 20px;
					border-top-right-radius: 20px;
				}
			""")

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

		setTimeBtn = self.dialog.findChild(QPushButton, "setTimeDialogBtn")
		setTimeBtn.setStyleSheet("""
			QPushButton {
				background-color: #287194;
				color: #fff;
				border-radius: 15px;
				padding: 5px 40px;
				font: bold 12pt "Poppins";
			}

			QPushButton:hover {
				background-color: #1F5773;
			}

			QPushButton:pressed {
				background-color: #193D4D;
			}
		""")

		setTimeBtn.clicked.connect(self.setTime)

		# Close the SET TIME dialog
		cancelTimeBtn = self.dialog.findChild(QPushButton, "cancelTimeBtn")
		cancelTimeBtn.clicked.connect(self.dialog.reject)

		# Disabled all buttons while this dialog is open
		self.setTimeBtn.setEnabled(False)
		self.feedNowBtn.setEnabled(False)
		self.captureBtn.setEnabled(False)
		self.liveFeedBtn.setEnabled(False)
		self.showFolderBtn.setEnabled(False)

		self.dialog.exec_() # Show the dialog

		# Enabled all buttons when the dialog is close
		self.setTimeBtn.setEnabled(True)
		self.feedNowBtn.setEnabled(True)
		self.captureBtn.setEnabled(True)
		self.liveFeedBtn.setEnabled(True)
		self.showFolderBtn.setEnabled(True)

	def setTime(self):
		# Get the time from the QTimeEdit widget as a QTime object and converted to String.	
		editted_first_sched = self.firstSchedTime.time()
		editted_first_sched_str = editted_first_sched.toString('h:mm AP')

		editted_second_sched = self.secondSchedTime.time()
		editted_second_sched_str = editted_second_sched.toString('h:mm AP')
		
		# Set the editted time to the Time Schedule display.
		self.firstSchedResult.setText(editted_first_sched_str)
		self.secondSchedResult.setText(editted_second_sched_str)
		self.dialog.reject()

	def successDialog(self):
		self.successMessageDialog = QMessageBox(self)
		icon = QPixmap("icon/success.svg")
		self.successMessageDialog.setIconPixmap(icon)
		self.successMessageDialog.setText("<b>SUCCESS!!</b> <br>Image successfully saved.")
		self.successMessageDialog.setGeometry(700, 480, 300, 300) # set the position of  the dialog
		
		# Customized QMessageBox() 
		font = QFont('Poppins', 12)
		self.successMessageDialog.setFont(font)
		self.successMessageDialog.setStyleSheet("""
				QMessageBox {
						background-color: rgba(25, 255, 96, 0.85);
						border-radius: 12px;
				}
				QMessageBox QLabel {
						background-color: transparent;
				}
		""")

		self.successMessageDialog.setStandardButtons(QMessageBox.NoButton)
		self.successMessageDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

		self.successMessageDialog.show()

		# Set a timer to close the message box after 2 seconds
		timer = QTimer()
		timer.singleShot(5000, self.successMessageDialog.accept)

	def imageUpdateSlot(self, image):
		self.cameraPreview.setPixmap(QPixmap.fromImage(image))
		
	def saveImage(self):
		current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		filename = f'{self.classificationResultLabel.text()}-{current_datetime}.png'
		filepath = os.path.join(directory, filename)
		
		# turn it if user wants to decide to manually enter the directory and the file extension
		# filepath = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]

		pixmap = self.cameraPreview.pixmap() # Get the current pixmap from the camera preview
		img = pixmap.toImage() # Get the pixel data from the pixmap
		img.save(filepath)

		self.successDialog()
	
	def openFileDialog(self):
		options = QFileDialog.Options()
		filetypes = "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
		filename, _ = QFileDialog.getOpenFileName(self, "Open File", directory, filetypes, options=options)
		if filename:
			url = QUrl.fromLocalFile(filename)
			QDesktopServices.openUrl(url)

class CameraWidget(QThread):
	imageUpdate = pyqtSignal(QImage)

	def run(self):
		self.ThreadActive = True
		capture = cv2.VideoCapture(cameraLocation)
		while self.ThreadActive:
			ret, frame = capture.read()
			if ret:
				image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				flippedImage = cv2.flip(image, 1)
				convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
				imageData = convertToQtFormat.scaled(cameraVerticalResolution, cameraHorizontalResolution, Qt.KeepAspectRatio)

				self.imageUpdate.emit(imageData)

	def stop(self):
		self.ThreadActive = False
		self.quit()

# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()