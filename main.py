from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog, QMessageBox, QTimeEdit, QFrame, QFileDialog, QWidget
from PyQt5.QtGui import QFont, QImage, QPixmap, QDesktopServices, QIcon, QMovie
from PyQt5.QtCore import QTime, QTimer, QThread, Qt, pyqtSignal, QUrl, QSettings
from datetime import datetime, timedelta
import RPiDevices.fishFeeder as fd
from PyQt5 import uic, QtCore
from ultralytics import YOLO
from time import sleep
import torch
import sys
import cv2
import os

# Must be modified or calibrated to make it work with other device.
cameraHorizontalResolution = 1024
cameraVerticalResolution = 700

# Path declaration
mainWindowUI = "main.ui"
feedingScheduleDialogUI = "feedingScheduleDialog.ui"
directory = 'C:/Users/jeral/OneDrive/Desktop/capture/'
model = YOLO("model/best.pt")
windowLogoPath = "icon/logo.svg"
successIconPath = "icon/success.svg"
loadingIndicatorPath = "gif/loading_indicator.gif"

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi(mainWindowUI, self)
		
		# Make the main window frameless
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		# self.showFullScreen()

		# Set the logo of the application
		self.setWindowIcon(QIcon(windowLogoPath))

		# QLabel widget
		self.timeLabel = self.findChild(QLabel, "timeLabel")
		self.dateLabel = self.findChild(QLabel, "dateLabel")
		self.firstSchedResult = self.findChild(QLabel, "firstSchedResult")
		self.secondSchedResult = self.findChild(QLabel, "secondSchedResult")
		self.thirdSchedResult = self.findChild(QLabel, "thirdSchedResult")
		self.fourthSchedResult = self.findChild(QLabel, "fourthSchedResult")
		self.secondSchedTitle = self.findChild(QLabel, "secondSchedTitle")
		self.thirdSchedTitle = self.findChild(QLabel, "thirdSchedTitle")
		self.fourthSchedTitle = self.findChild(QLabel, "fourthSchedTitle")
		self.classResult = self.findChild(QLabel, "classificationResultLabel")
		self.fishFeedingStatusResult = self.findChild(QLabel, "fishFeedingStatusResult")
		self.cameraPreview = self.findChild(QLabel, "cameraPreviewHolder")
		self.accuracyResult = self.findChild(QLabel, "accuracyResult")

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
				border-radius: 10px;
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
				border-radius: 10px;
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

		# Open the dialog when "SET TIME" button is clicked.
		self.setTimeBtn.clicked.connect(self.openFeedingScheduleDialog)

		self.exitBtn.clicked.connect(self.closeApp) # Close the App when clicked
		self.minimizeBtn.clicked.connect(self.showMinimized) # Minimize the App when clicked

		# Multithreading for Camera and Fish feeder widget
		self.cameraWidget = CameraWidget(0, self.classResult, self.accuracyResult)
		self.cameraWidget.imageUpdate.connect(self.imageUpdateSlot)
		self.cameraWidget.start()

		self.fishFeederWidget = FishFeederWidget() # Instances of fish feeder

		# Trigger the Fish Feeding Device to operate
		self.feedNowBtn.clicked.connect(self.activateFishFeeder)

		# Start live feeding
		self.liveFeedBtn.setCheckable(True)
		self.liveFeedBtn.setChecked(False)
		self.liveFeedBtn.clicked.connect(self.startLiveFeed)

		self.captureBtn.clicked.connect(self.saveImage)
		self.showFolderBtn.clicked.connect(self.openFileDialog)

		self.loadFeedingScheduledTime()

		self.show()

	def activateFishFeeder(self):
		self.fishFeederWidget.start()
		self.fishFeederWidget.stop()

	def startLiveFeed(self):
		if self.liveFeedBtn.isChecked():
			self.liveFeedBtn.setText("STOP DETECTION")
			self.liveFeedBtn.setStyleSheet("""
				QPushButton {
					background-color: #A40808;
					color: #fff;
					border-radius: 15px;
					padding: 10px 25px;
					font: bold 12pt "Poppins";
				}

				QPushButton:hover {
					background-color: #F42020;
				}

				QPushButton:pressed {
					background-color: #F65050;
				}
			""")

			self.loadingScreen = LoadingScreen(self) # Create an instance of loading screen
			self.cameraWidget.stop() # Stop the normal camera to operate
			sleep(1)
			self.cameraWidget = CameraWidget(1, self.classResult, self.accuracyResult) # initialize the classification model
			self.cameraWidget.imageUpdate.connect(self.imageUpdateSlot)
			self.cameraWidget.start() # start detection
		else:
			self.loadingScreen = LoadingScreen(self) # Create an instance of loading screen
			self.cameraWidget.stop() # stop detection
			sleep(1)
			self.cameraWidget = CameraWidget(0, self.classResult, self.accuracyResult) # initialize the normal camera
			self.cameraWidget.imageUpdate.connect(self.imageUpdateSlot)
			self.cameraWidget.start() # start the normal camera			
			sleep(1)
			self.classResult.setText("No Detection")
			self.accuracyResult.setText("0%")
			self.liveFeedBtn.setText("START DETECTION")
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
		
	def fishFeedingSchedCounter(self):
		rawCurrentDatetime = datetime.now()
		formattedCurrentDate = rawCurrentDatetime.strftime("%B %d, %Y (%A)")
		formattedCurrentTime = rawCurrentDatetime.strftime("%I:%M:%S %p")
		
		self.dateLabel.setText(formattedCurrentDate)
		self.timeLabel.setText(formattedCurrentTime)

		# Acquired feeding time for morning and afternoon schedule
		rawFirstFeedingSched = datetime.strptime(self.firstSchedResult.text(), "%I:%M %p")
		rawSecondFeedingSched = datetime.strptime(self.secondSchedResult.text(), "%I:%M %p")
		rawThirdFeedingSched = rawSecondFeedingSched + timedelta(hours=3) # dependent on second feeding schedule (3 hours advance)
		
		if rawThirdFeedingSched.time() > datetime.strptime("12:00 PM", "%I:%M %p").time():
			rawThirdFeedingSched = datetime.combine(rawThirdFeedingSched.date(), datetime.strptime("12:00 PM", "%I:%M %p").time())
	
		rawFourthFeedingSched = datetime.strptime(self.fourthSchedResult.text(), "%I:%M %p")
		rawFifthFeedingSched = datetime.strptime(self.fifthSchedResult.text(), "%I:%M %p")
		rawSixthFeedingSched = rawFifthFeedingSched + timedelta(hours=3) # dependent on fifth feeding schedule (3 hours advance)

		# Check if the resulting time is later than 12:00 AM but earlier than 4:00 AM, and adjust it accordingly
		if datetime.strptime("12:00 AM", "%I:%M %p").time() <= rawSixthFeedingSched.time() < datetime.strptime("4:00 AM", "%I:%M %p").time():
			rawSixthFeedingSched = datetime.combine(rawSixthFeedingSched.date(), datetime.strptime("12:00 AM", "%I:%M %p").time())

		firstFeedingSched = rawFirstFeedingSched.strftime("%I:%M:%S %p")
		secondFeedingSched = rawSecondFeedingSched.strftime("%I:%M:%S %p")
		thirdFeedingSched = rawThirdFeedingSched.strftime("%I:%M:%S %p")

		fourthFeedingSched = rawFourthFeedingSched.strftime("%I:%M:%S %p")
		fifthFeedingSched = rawFifthFeedingSched.strftime("%I:%M:%S %p")
		sixthFeedingSched = rawSixthFeedingSched.strftime("%I:%M:%S %p")

		self.mainFrame = self.findChild(QFrame, "mainFrame")
		self.cameraPreviewHolder = self.findChild(QLabel,"cameraPreviewHolder")

		# Updates the fish feeding status based on the inference result.
		if (self.classResult.text().lower() == "deficient"):		
			self.fishFeedingStatusResult.setText("Four times a day")
			self.thirdSchedTitle.show()
			self.thirdSchedResult.show()
			self.thirdSchedResult.setText(rawThirdFeedingSched.strftime("%I:%M %p").lstrip('0'))

			self.fourthSchedTitle.setText("4th:")
			self.fifthSchedTitle.setText("5th:")

			self.sixthSchedTitle.show()
			self.sixthSchedResult.show()
			self.sixthSchedResult.setText(rawSixthFeedingSched.strftime("%I:%M %p").lstrip('0'))

			self.mainFrame.setStyleSheet("""
				QFrame {
					background-color: rgb(250, 160, 160);
					border-top-left-radius: 20px;
					border-top-right-radius: 20px;
				}
			""")

			self.cameraPreviewHolder.setStyleSheet("""
				QLabel {
					background-color: rgba(255, 255, 255, 0);
					color: rgba(0, 0, 0, 255);
					border: 3px solid #A40808;
					border-radius: 5px;
				}
			""")

			self.feedNowBtn.setStyleSheet("""
				QPushButton {
					background-color: #A40808;
					color: #fff;
					border-radius: 15px;
					padding: 10px 25px;
					font: bold 12pt "Poppins";
				}

				QPushButton:hover {
					background-color: #F42020;
				}

				QPushButton:pressed {
					background-color: #F65050;
				}
			""")
			
			self.setTimeBtn.setStyleSheet("""
				QPushButton {
					background-color: #A40808;
					color: #fff;
					border-radius: 15px;
					padding: 10px 25px;
					font: bold 12pt "Poppins";
				}

				QPushButton:hover {
					background-color: #F42020;
				}

				QPushButton:pressed {
					background-color: #F65050;
				}
			""")

			self.showFolderBtn.setStyleSheet("""
				QPushButton {
					background-color: #A40808;
					color: #fff;
					border-radius: 15px;
					padding: 10px 25px;
					font: bold 12pt "Poppins";
				}

				QPushButton:hover {
					background-color: #F42020;
				}

				QPushButton:pressed {
					background-color: #F65050;
				}
			""")	

			self.captureBtn.setStyleSheet("""
				QPushButton {
					background-color: #A40808;
					color: #fff;
					border-radius: 15px;
					padding: 10px 25px;
					font: bold 12pt "Poppins";
				}

				QPushButton:hover {
					background-color: #F42020;
				}

				QPushButton:pressed {
					background-color: #F65050;
				}
			""")

			self.liveFeedBtn.setStyleSheet("""
				QPushButton {
					background-color: #A40808;
					color: #fff;
					border-radius: 15px;
					padding: 10px 25px;
					font: bold 12pt "Poppins";
				}

				QPushButton:hover {
					background-color: #F42020;
				}

				QPushButton:pressed {
					background-color: #F65050;
				}
			""")		

			if formattedCurrentTime in [firstFeedingSched, secondFeedingSched, fourthFeedingSched, fifthFeedingSched]:
				self.activateFishFeeder()
		else:
			self.resetToDefaultStyle()
			if formattedCurrentTime in [firstFeedingSched, secondFeedingSched, thirdFeedingSched, fourthFeedingSched, fifthFeedingSched, sixthFeedingSched]:
				self.activateFishFeeder()

	def resetToDefaultStyle(self):
		self.fishFeedingStatusResult.setText("Twice a day") 
		self.thirdSchedTitle.hide()
		self.thirdSchedResult.hide()
		
		self.fourthSchedTitle.setText("3rd:")
		self.fifthSchedTitle.setText("4th:")
		
		self.sixthSchedTitle.hide()
		self.sixthSchedResult.hide()

		self.mainFrame.setStyleSheet("""
			QFrame {
				background-color: rgb(211, 212, 206);
				border-top-left-radius: 20px;
				border-top-right-radius: 20px;
			}
		""")

		self.cameraPreviewHolder.setStyleSheet("""
			QLabel {
				background-color: rgba(255, 255, 255, 0);
				color: rgba(0, 0, 0, 255);
				border: 3px solid #287194;
				border-radius: 5px;
			}
		""")

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

	def openFeedingScheduleDialog(self):
		self.dialog = QDialog(self)
		uic.loadUi(feedingScheduleDialogUI, self.dialog)

		self.dialog.setGeometry(300, 120, 300, 300) # set the position of  the dialog

		self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Make the main window frameless 
		self.dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground) # make the background translucent

		# Access the QTimeEdit widget
		self.firstSchedTime = self.dialog.findChild(QTimeEdit, "firstSchedTime")
		self.secondSchedTime = self.dialog.findChild(QTimeEdit, "secondSchedTime")
		self.thirdSchedTime = self.dialog.findChild(QTimeEdit, "thirdSchedTime")
		self.fourthSchedTime = self.dialog.findChild(QTimeEdit, "fourthSchedTime")
		self.thirdSchedTitleDialog = self.dialog.findChild(QLabel, "thirdSchedTitle")
		self.fourthSchedTitleDialog = self.dialog.findChild(QLabel, "fourthSchedTitle")

		# Set the first QTime edit based on the current first schedule
		firstSchedEdit = QTime.fromString(self.firstSchedResult.text(), 'h:mm AP')
		self.firstSchedTime.setTime(firstSchedEdit)

		# Set the second QTime edit based on the current second schedule
		secondSchedEdit = QTime.fromString(self.secondSchedResult.text(), 'h:mm AP')
		self.secondSchedTime.setTime(secondSchedEdit)

		# Set the third QTime edit based on the current third schedule
		thirdSchedEdit = QTime.fromString(self.fourthSchedResult.text(), 'h:mm AP')
		self.thirdSchedTime.setTime(thirdSchedEdit)

		# Set the fourth QTime edit based on the current fourth schedule
		fourthSchedEdit = QTime.fromString(self.fifthSchedResult.text(), 'h:mm AP')
		self.fourthSchedTime.setTime(fourthSchedEdit)

		if (self.classResult.text().lower() == "deficient"):		
			self.thirdSchedTitleDialog.setText("Fourth Schedule:")
			self.fourthSchedTitleDialog.setText("Fifth Schedule:")
		else: 
			self.thirdSchedTitleDialog.setText("Third Schedule:")
			self.fourthSchedTitleDialog.setText("Fourth Schedule:")
		
		setTimeBtn = self.dialog.findChild(QPushButton, "setTimeDialogBtn")
		setTimeBtn.setStyleSheet("""
			QPushButton {
				background-color: #287194;
				color: #fff;
				border-radius: 10px;
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

	# Load the saved scheduled time 
	def loadFeedingScheduledTime(self):
		scheduleSettings = QSettings("FishFeedSchedule", "FeedingTimeSetter")
		savedFirstFeedingSchedule = scheduleSettings.value("firstSchedule")
		savedSecondFeedingSchedule = scheduleSettings.value("secondSchedule")
		savedThirdFeedingSchedule = scheduleSettings.value("thirdSchedule")
		savedFourthFeedingSchedule = scheduleSettings.value("fourthSchedule")

		if savedFirstFeedingSchedule or savedSecondFeedingSchedule or savedThirdFeedingSchedule or savedFourthFeedingSchedule:
			self.firstSchedResult.setText(savedFirstFeedingSchedule)
			self.secondSchedResult.setText(savedSecondFeedingSchedule)
			self.fourthSchedResult.setText(savedThirdFeedingSchedule)
			self.fifthSchedResult.setText(savedFourthFeedingSchedule)

	def setTime(self):
		# Get the time from the QTimeEdit widget as a QTime object and converted to String.	
		edittedFirstSched = self.firstSchedTime.time()
		edittedSecondSched = self.secondSchedTime.time()
		edittedThirdSched = self.thirdSchedTime.time()
		edittedFourthSched = self.fourthSchedTime.time()

		edittedFirstSchedStr = edittedFirstSched.toString('h:mm AP')
		edittedSecondSchedStr = edittedSecondSched.toString('h:mm AP')
		edittedThirdSchedStr = edittedThirdSched.toString('h:mm AP')
		edittedFourthSchedStr = edittedFourthSched.toString('h:mm AP')
		
		isValid = self.validateTime(edittedFirstSched, edittedSecondSched, edittedThirdSched, edittedFourthSched)

		if isValid[0] == True:
			# Set the editted time to the Time Schedule display.
			self.firstSchedResult.setText(edittedFirstSchedStr)
			self.secondSchedResult.setText(edittedSecondSchedStr)
			self.fourthSchedResult.setText(edittedThirdSchedStr)
			self.fifthSchedResult.setText(edittedFourthSchedStr)

			# Update the QSettings FeedingTimeSetter
			scheduleSettings = QSettings("FishFeedSchedule", "FeedingTimeSetter")
			scheduleSettings.setValue("firstSchedule", edittedFirstSchedStr)
			scheduleSettings.setValue("secondSchedule", edittedSecondSchedStr)
			scheduleSettings.setValue("thirdSchedule", edittedThirdSchedStr)
			scheduleSettings.setValue("fourthSchedule", edittedFourthSchedStr)
			self.dialog.reject()
		else:
			self.openInvalidInputDialog(isValid[1], isValid[2])

	def validateTime(self, edittedFirstSched, edittedSecondSched, edittedThirdSched, edittedFourthSched):
		if edittedSecondSched <= edittedFirstSched:
			return [False, "First", "second"]

		if edittedFourthSched <= edittedThirdSched:
			return [False, "Third", "fourth"]
		return [True]
	
	def openInvalidInputDialog(self, schedule1, schedule2):
		self.invalidInputMessage = QMessageBox(self)
		self.invalidInputMessage.setIcon(QMessageBox.Warning)
		self.invalidInputMessage.setText(f"WARNING:\n\n {schedule1} schedule should be earlier than the {schedule2} schedule")
		self.invalidInputMessage.setGeometry(300, 150, 300, 300) # set the position of  the dialog
		
		# Customized QMessageBox() 
		font = QFont('Poppins', 12)
		self.invalidInputMessage.setFont(font)
		self.invalidInputMessage.setStyleSheet("""
				QMessageBox {
						background-color: rgb(250, 160, 160);
				}
				QMessageBox QLabel {
						qproperty-alignment: AlignCenter;
						background-color: transparent;
				}
		""")

		okButton = self.invalidInputMessage.addButton(QMessageBox.Ok)
		okButton.setStyleSheet("""
				QPushButton {
						background-color: #F44336;
						color: #fff;
						border-radius: 15px;
						padding: 10px 25px;
						font: bold 10pt "Poppins";
				}
		""")
		self.invalidInputMessage.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.invalidInputMessage.exec_()

	def successDialog(self):
		self.successMessageDialog = QMessageBox(self)
		icon = QPixmap(successIconPath)
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

	def closeApp(self):
		self.cameraWidget.stop()
		QApplication.quit()

class CameraWidget(QThread):
	imageUpdate = pyqtSignal(QImage)
	
	def __init__(self, liveFeedStatus, classResult, accuracyResult):
		super().__init__()
		self.liveFeedStatus = liveFeedStatus
		self.classResult = classResult
		self.accuracyResult = accuracyResult

	def run(self):
		self.ThreadActive = True
		capture = cv2.VideoCapture(cv2.CAP_ANY) 
		while self.ThreadActive:
			ret, frame = capture.read()
			if ret:
				if self.liveFeedStatus == 0:
					self.displayFrame(frame)
				elif self.liveFeedStatus == 1:
					predictions = model(frame, stream=True, conf=0.5)
					for prediction in predictions:
						annotatedFrame = prediction.plot()
						self.displayFrame(annotatedFrame)

						classificationResult = "-"
						classLabels = prediction.boxes.cls
						if 0 in classLabels:
							classificationResult = "Deficient"
						elif 1 in classLabels:
							classificationResult = "Sufficient"
						else:
							classificationResult = "No Detection"
						self.classResult.setText(classificationResult)
						
						classScore = prediction.boxes.conf
						if len(classScore) > 0:
							classScoreAverage = (torch.sum(classScore) / len(classScore)) * 100
							rounded_value = f'{round(classScoreAverage.item(), 2)}%'
							self.accuracyResult.setText(rounded_value)
						else:
							self.accuracyResult.setText("0%")
						
	def hasDeficient(self, list):
		return 0 in list

	def displayFrame(self, frame):
		image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		convertToQtFormat = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
		imageData = convertToQtFormat.scaled(cameraVerticalResolution, cameraHorizontalResolution, Qt.KeepAspectRatio)
		self.imageUpdate.emit(imageData)

	def stop(self):
		self.ThreadActive = False
		self.quit()

class FishFeederWidget(QThread):	
	def run(self):
		fd.feedNow()

	def stop(self):
		self.quit()

class LoadingScreen(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setFixedSize(200, 200)
		self.setGeometry(300, 200, 300, 300) # set the position of  the dialog
		self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
	
		self.labelAnimation = QLabel(self)
		self.movie = QMovie(loadingIndicatorPath)
		self.labelAnimation.setMovie(self.movie)

		timer = QTimer(self)
		self.startAnimation()
		timer.singleShot(3500, self.stopAnimation)
		self.show()

	def startAnimation(self):
		self.movie.start()

	def stopAnimation(self):
		self.movie.stop()
		self.close()
		
# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
