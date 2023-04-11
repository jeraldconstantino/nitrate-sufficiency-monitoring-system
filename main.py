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

from PyQt5 import QtCore, QtGui, QtWidgets
from fishFeedingScheduleDialog import Ui_dialogUI
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime
from RPiDevices.fishFeeder import feedNow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet("*{\n"
"    background-color: rgb(25, 61, 77);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appTitle.sizePolicy().hasHeightForWidth())
        self.appTitle.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.appTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(22)
        self.appTitle.setFont(font)
        self.appTitle.setAutoFillBackground(False)
        self.appTitle.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"}")
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setObjectName("appTitle")
        self.verticalLayout.addWidget(self.appTitle)
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(211, 212, 206);\n"
"    border-top-left-radius: 50px;\n"
"    border-top-right-radius: 50px;\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setContentsMargins(15, 15, 20, 15)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cameraLayout = QtWidgets.QVBoxLayout()
        self.cameraLayout.setSpacing(15)
        self.cameraLayout.setObjectName("cameraLayout")
        self.cameraPreviewHolder = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraPreviewHolder.sizePolicy().hasHeightForWidth())
        self.cameraPreviewHolder.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.cameraPreviewHolder.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.cameraPreviewHolder.setFont(font)
        self.cameraPreviewHolder.setAutoFillBackground(False)
        self.cameraPreviewHolder.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 255);\n"
"    border: 3px solid rgb(25, 61, 77);\n"
"    border-radius: 40px;\n"
"}")
        self.cameraPreviewHolder.setFrameShape(QtWidgets.QFrame.Box)
        self.cameraPreviewHolder.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cameraPreviewHolder.setLineWidth(1)
        self.cameraPreviewHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraPreviewHolder.setObjectName("cameraPreviewHolder")
        self.cameraLayout.addWidget(self.cameraPreviewHolder)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.captureBtn = QtWidgets.QPushButton(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.captureBtn.setFont(font)
        self.captureBtn.setStyleSheet("QPushButton {\n"
"    background-color: #287194;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    padding: 5px 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #193D4D;\n"
"}")
        self.captureBtn.setObjectName("captureBtn")
        self.horizontalLayout_3.addWidget(self.captureBtn)
        self.liveFeedBtn = QtWidgets.QPushButton(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.liveFeedBtn.setFont(font)
        self.liveFeedBtn.setStyleSheet("QPushButton {\n"
"    background-color: #287194;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    padding: 5px 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #193D4D;\n"
"}")
        self.liveFeedBtn.setObjectName("liveFeedBtn")
        self.horizontalLayout_3.addWidget(self.liveFeedBtn)
        self.showFolderBtn = QtWidgets.QPushButton(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showFolderBtn.setFont(font)
        self.showFolderBtn.setStyleSheet("QPushButton {\n"
"    background-color: #287194;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    padding: 5px 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #193D4D;\n"
"}")
        self.showFolderBtn.setObjectName("showFolderBtn")
        self.horizontalLayout_3.addWidget(self.showFolderBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cameraLayout.addLayout(self.horizontalLayout_3)
        self.cameraLayout.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.cameraLayout)
        self.fishFeederLayout = QtWidgets.QVBoxLayout()
        self.fishFeederLayout.setSpacing(20)
        self.fishFeederLayout.setObjectName("fishFeederLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.fishFeederLayout.addItem(spacerItem2)
        self.currentTimeLayout = QtWidgets.QVBoxLayout()
        self.currentTimeLayout.setSpacing(0)
        self.currentTimeLayout.setObjectName("currentTimeLayout")
        self.currentTimeTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.currentTimeTitle.setFont(font)
        self.currentTimeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTimeTitle.setObjectName("currentTimeTitle")
        self.currentTimeLayout.addWidget(self.currentTimeTitle)
        self.dateLabel = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.currentTimeLayout.addWidget(self.dateLabel)
        self.timeLabel = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.currentTimeLayout.addWidget(self.timeLabel)
        self.fishFeederLayout.addLayout(self.currentTimeLayout)
        self.inferenceResultLayout = QtWidgets.QVBoxLayout()
        self.inferenceResultLayout.setSpacing(0)
        self.inferenceResultLayout.setObjectName("inferenceResultLayout")
        self.inferenceResultTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inferenceResultTitle.setFont(font)
        self.inferenceResultTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.inferenceResultTitle.setObjectName("inferenceResultTitle")
        self.inferenceResultLayout.addWidget(self.inferenceResultTitle)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.classTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.classTitle.setFont(font)
        self.classTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.classTitle.setObjectName("classTitle")
        self.horizontalLayout_5.addWidget(self.classTitle)
        self.classificationResultLabel = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classificationResultLabel.setFont(font)
        self.classificationResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classificationResultLabel.setObjectName("classificationResultLabel")
        self.horizontalLayout_5.addWidget(self.classificationResultLabel)
        self.inferenceResultLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.accuracyTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.accuracyTitle.setFont(font)
        self.accuracyTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.accuracyTitle.setObjectName("accuracyTitle")
        self.horizontalLayout_4.addWidget(self.accuracyTitle)
        self.accuracyResult = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accuracyResult.setFont(font)
        self.accuracyResult.setAlignment(QtCore.Qt.AlignCenter)
        self.accuracyResult.setObjectName("accuracyResult")
        self.horizontalLayout_4.addWidget(self.accuracyResult)
        self.inferenceResultLayout.addLayout(self.horizontalLayout_4)
        self.fishFeederLayout.addLayout(self.inferenceResultLayout)
        self.fishFeedingStatusLayout = QtWidgets.QVBoxLayout()
        self.fishFeedingStatusLayout.setSpacing(0)
        self.fishFeedingStatusLayout.setObjectName("fishFeedingStatusLayout")
        self.fishFeedingStatusTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fishFeedingStatusTitle.setFont(font)
        self.fishFeedingStatusTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.fishFeedingStatusTitle.setObjectName("fishFeedingStatusTitle")
        self.fishFeedingStatusLayout.addWidget(self.fishFeedingStatusTitle)
        self.fishFeedingStatusResult = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.fishFeedingStatusResult.setFont(font)
        self.fishFeedingStatusResult.setAlignment(QtCore.Qt.AlignCenter)
        self.fishFeedingStatusResult.setObjectName("fishFeedingStatusResult")
        self.fishFeedingStatusLayout.addWidget(self.fishFeedingStatusResult)
        self.fishFeederLayout.addLayout(self.fishFeedingStatusLayout)
        self.timeScheduleLayout = QtWidgets.QVBoxLayout()
        self.timeScheduleLayout.setSpacing(0)
        self.timeScheduleLayout.setObjectName("timeScheduleLayout")
        self.timeScheduleTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timeScheduleTitle.setFont(font)
        self.timeScheduleTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.timeScheduleTitle.setObjectName("timeScheduleTitle")
        self.timeScheduleLayout.addWidget(self.timeScheduleTitle)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.firstSchedTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.firstSchedTitle.setFont(font)
        self.firstSchedTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.firstSchedTitle.setObjectName("firstSchedTitle")
        self.horizontalLayout_7.addWidget(self.firstSchedTitle)
        self.firstSchedResult = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.firstSchedResult.setFont(font)
        self.firstSchedResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.firstSchedResult.setObjectName("firstSchedResult")
        self.horizontalLayout_7.addWidget(self.firstSchedResult)
        self.timeScheduleLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.secondSchedTitle = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.secondSchedTitle.setFont(font)
        self.secondSchedTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.secondSchedTitle.setObjectName("secondSchedTitle")
        self.horizontalLayout_6.addWidget(self.secondSchedTitle)
        self.secondSchedResult = QtWidgets.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.secondSchedResult.setFont(font)
        self.secondSchedResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.secondSchedResult.setObjectName("secondSchedResult")
        self.horizontalLayout_6.addWidget(self.secondSchedResult)
        self.timeScheduleLayout.addLayout(self.horizontalLayout_6)
        self.fishFeederLayout.addLayout(self.timeScheduleLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.fishFeederLayout.addItem(spacerItem3)
        self.feedingSchedBtns = QtWidgets.QVBoxLayout()
        self.feedingSchedBtns.setSpacing(15)
        self.feedingSchedBtns.setObjectName("feedingSchedBtns")
        self.feedNowBtn = QtWidgets.QPushButton(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.feedNowBtn.setFont(font)
        self.feedNowBtn.setStyleSheet("QPushButton {\n"
"    background-color: #287194;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    padding: 5px 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #193D4D;\n"
"}")
        self.feedNowBtn.setObjectName("feedNowBtn")
        self.feedingSchedBtns.addWidget(self.feedNowBtn)
        self.setTimeBtn = QtWidgets.QPushButton(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setTimeBtn.setFont(font)
        self.setTimeBtn.setStyleSheet("QPushButton {\n"
"    background-color: #287194;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    padding: 5px 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #193D4D;\n"
"}")
        self.setTimeBtn.setObjectName("setTimeBtn")
        self.feedingSchedBtns.addWidget(self.setTimeBtn)
        self.fishFeederLayout.addLayout(self.feedingSchedBtns)
        self.horizontalLayout.addLayout(self.fishFeederLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # make the window frameless
        
        # Open the dialog when "SET TIME" button is clicked.
        self.setTimeBtn.clicked.connect(lambda: self.openFeedingScheduleDialog(MainWindow))

        # Trigger the Fish Feeding Device to operate
        self.feedNowBtn.clicked.connect(feedNow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.fishFeedingSchedCounter)
        self.timer.start(1000) # Timer updates every 1 second
        
        self.fishFeedingSchedCounter()

    def openFeedingScheduleDialog(self, parent):
        if not hasattr(self, 'dialog'):
            dialogUI = QtWidgets.QDialog(parent)
            ui = Ui_dialogUI()
            ui.setupUi(dialogUI, self.firstSchedResult, self.secondSchedResult)
            dialogUI.setModal(True)

            # Ensure that the dialog show up at the center
            x = int(parent.geometry().x() + (parent.geometry().width() - dialogUI.width()) / 2)
            y = int(parent.geometry().y() + (parent.geometry().height() - dialogUI.height()) / 2)
            dialogUI.move(x, y)

            # Set the first QTime edit based on the current first schedule
            first_feeding_sched_edit = QTime.fromString(self.firstSchedResult.text(), 'h:mm AP')
            ui.firstSchedTime.setTime(first_feeding_sched_edit)

            # Set the second QTime edit based on the current second schedule        
            second_feeding_sched_edit = QTime.fromString(self.secondSchedResult.text(), 'h:mm AP')
            ui.secondSchedTime.setTime(second_feeding_sched_edit)

            dialogUI.show()
            dialogUI.exec_()

    # Display a real-time date and time 
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nutrient Sufficiency Monitoring System"))
        self.appTitle.setText(_translate("MainWindow", "NITRATE SUFFICIENCY MONITORING SYSTEM"))
        self.cameraPreviewHolder.setText(_translate("MainWindow", "Camera is not yet enabled . . ."))
        self.captureBtn.setText(_translate("MainWindow", "CAPTURE"))
        self.liveFeedBtn.setText(_translate("MainWindow", "GO LIVE!"))
        self.showFolderBtn.setText(_translate("MainWindow", "SHOW FOLDER"))
        self.currentTimeTitle.setText(_translate("MainWindow", "TIMESTAMP:"))
        self.dateLabel.setText(_translate("MainWindow", "-"))
        self.timeLabel.setText(_translate("MainWindow", "-"))
        self.inferenceResultTitle.setText(_translate("MainWindow", "INFERENCE RESULT:"))
        self.classTitle.setText(_translate("MainWindow", "CLASS:"))
        self.classificationResultLabel.setText(_translate("MainWindow", "DEFICIENT"))
        self.accuracyTitle.setText(_translate("MainWindow", "ACCURACY:"))
        self.accuracyResult.setText(_translate("MainWindow", "90%"))
        self.fishFeedingStatusTitle.setText(_translate("MainWindow", "FISH FEEDING STATUS:"))
        self.fishFeedingStatusResult.setText(_translate("MainWindow", "-"))
        self.timeScheduleTitle.setText(_translate("MainWindow", "TIME SCHEDULE:"))
        self.firstSchedTitle.setText(_translate("MainWindow", "First:"))
        self.firstSchedResult.setText(_translate("MainWindow", "8:00 AM"))
        self.secondSchedTitle.setText(_translate("MainWindow", "Second:"))
        self.secondSchedResult.setText(_translate("MainWindow", "4:00 PM"))
        self.feedNowBtn.setText(_translate("MainWindow", "FEED NOW"))
        self.setTimeBtn.setText(_translate("MainWindow", "SET TIME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())