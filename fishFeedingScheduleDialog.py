from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogUI(object):
    def setupUi(self, dialogUI, firstSchedTimeMW, secondSchedTimeMW):
        dialogUI.setObjectName("dialogUI")
        dialogUI.resize(1024, 600)
        dialogUI.setStyleSheet("")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(dialogUI)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(dialogUI)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgba(0, 0, 0, 120);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dialogFrame = QtWidgets.QFrame(self.frame)
        self.dialogFrame.setMinimumSize(QtCore.QSize(500, 310))
        self.dialogFrame.setMaximumSize(QtCore.QSize(500, 310))
        self.dialogFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(217, 217, 217);\n"
"    border-radius:30px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color:transparent;\n"
"}\n"
"")
        self.dialogFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dialogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dialogFrame.setObjectName("dialogFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dialogFrame)
        self.verticalLayout_3.setContentsMargins(30, -1, 30, 15)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.feedingTimeTitle = QtWidgets.QLabel(self.dialogFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.feedingTimeTitle.setFont(font)
        self.feedingTimeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.feedingTimeTitle.setObjectName("feedingTimeTitle")
        self.verticalLayout_3.addWidget(self.feedingTimeTitle)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstSchedVLayout = QtWidgets.QVBoxLayout()
        self.firstSchedVLayout.setSpacing(0)
        self.firstSchedVLayout.setObjectName("firstSchedVLayout")
        self.firstSchedTitle = QtWidgets.QLabel(self.dialogFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.firstSchedTitle.setFont(font)
        self.firstSchedTitle.setObjectName("firstSchedTitle")
        self.firstSchedVLayout.addWidget(self.firstSchedTitle)
        self.firstSchedTime = QtWidgets.QTimeEdit(self.dialogFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(True)
        font.setWeight(75)
        self.firstSchedTime.setFont(font)
        self.firstSchedTime.setStyleSheet("QTimeEdit {\n"
"    background-color: transparent;\n"
"    color: #000;\n"
"    border: 3px solid rgb(25, 61, 77);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 20px;\n"
"}")
        self.firstSchedTime.setAlignment(QtCore.Qt.AlignCenter)
        self.firstSchedTime.setObjectName("firstSchedTime")
        self.firstSchedVLayout.addWidget(self.firstSchedTime)
        self.verticalLayout.addLayout(self.firstSchedVLayout)
        self.secondSchedVLayout = QtWidgets.QVBoxLayout()
        self.secondSchedVLayout.setSpacing(0)
        self.secondSchedVLayout.setObjectName("secondSchedVLayout")
        self.secondSchedTitle = QtWidgets.QLabel(self.dialogFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.secondSchedTitle.setFont(font)
        self.secondSchedTitle.setObjectName("secondSchedTitle")
        self.secondSchedVLayout.addWidget(self.secondSchedTitle)
        self.secondSchedTime = QtWidgets.QTimeEdit(self.dialogFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(True)
        font.setWeight(75)
        self.secondSchedTime.setFont(font)
        self.secondSchedTime.setStyleSheet("QTimeEdit {\n"
"    background-color: transparent;\n"
"    color: #000;\n"
"    border: 3px solid rgb(25, 61, 77);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 20px;\n"
"}")
        self.secondSchedTime.setAlignment(QtCore.Qt.AlignCenter)
        self.secondSchedTime.setObjectName("secondSchedTime")
        self.secondSchedVLayout.addWidget(self.secondSchedTime)
        self.verticalLayout.addLayout(self.secondSchedVLayout)
        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.buttonHLayout.setSpacing(15)
        self.buttonHLayout.setObjectName("buttonHLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonHLayout.addItem(spacerItem1)
        self.setTimeBtn = QtWidgets.QPushButton(self.dialogFrame)
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
"    padding: 3px 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #193D4D;\n"
"}\n"
"")
        self.setTimeBtn.setObjectName("setTimeBtn")
        self.buttonHLayout.addWidget(self.setTimeBtn)
        self.cancelTimeBtn = QtWidgets.QPushButton(self.dialogFrame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancelTimeBtn.setFont(font)
        self.cancelTimeBtn.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: #287194;\n"
"    padding: 5px 30px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #1F5773;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #193D4D;\n"
"}")
        self.cancelTimeBtn.setObjectName("cancelTimeBtn")
        self.buttonHLayout.addWidget(self.cancelTimeBtn)
        self.verticalLayout.addLayout(self.buttonHLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.dialogFrame)
        spacerItem2 = QtWidgets.QSpacerItem(243, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.frame)

        self.retranslateUi(dialogUI)
        QtCore.QMetaObject.connectSlotsByName(dialogUI)
        
        dialogUI.setWindowFlag(QtCore.Qt.FramelessWindowHint) # make the window frameless
        dialogUI.setAttribute(QtCore.Qt.WA_TranslucentBackground) # make the background translucent
        
        # Customized QMessageBox() 
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg_box.setText("WARNING:\n\n The first and second schedules must not be at the same time.")
        
        font = QtGui.QFont('Poppins', 12)
        self.msg_box.setFont(font)
        self.msg_box.setStyleSheet("""
                QMessageBox {
                        background-color: rgb(250, 160, 160);
                }
                QMessageBox QLabel {
                        qproperty-alignment: AlignCenter;
                }
        """)

        ok_button = self.msg_box.addButton(QtWidgets.QMessageBox.Ok)
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

        # Close the dialog
        self.cancelTimeBtn.clicked.connect(dialogUI.reject)

        # Set the time schedule
        self.setTimeBtn.clicked.connect(lambda: self.setTime(dialogUI, firstSchedTimeMW, secondSchedTimeMW))


    def setTime(self, dialogUI, firstSchedTimeMW, secondSchedTimeMW):
        # Get the time from the QTimeEdit widget as a QTime object and converted to String.
        editted_first_sched = self.firstSchedTime.time()
        editted_first_sched_str = editted_first_sched.toString('h:mm AP')

        editted_second_sched = self.secondSchedTime.time()
        editted_second_sched_str = editted_second_sched.toString('h:mm AP')
        
        isValidTime = self.validateTime(editted_first_sched_str, editted_second_sched_str)

        if isValidTime == True:
            # Set the editted time to the Time Schedule display.
            firstSchedTimeMW.setText(editted_first_sched_str)
            secondSchedTimeMW.setText(editted_second_sched_str)
            dialogUI.reject()
        else:
            self.msg_box.exec_()
            
    def validateTime(self, firstSchedTime, secondSchedTime):
        if firstSchedTime == secondSchedTime:
            return False
        return True

    def retranslateUi(self, dialogUI):
        _translate = QtCore.QCoreApplication.translate
        dialogUI.setWindowTitle(_translate("dialogUI", "Dialog"))
        self.feedingTimeTitle.setText(_translate("dialogUI", "Feeding Time Schedule"))
        self.firstSchedTitle.setText(_translate("dialogUI", "First Feeding Schedule:"))
        self.secondSchedTitle.setText(_translate("dialogUI", "Second Feeding Schedule:"))
        self.setTimeBtn.setText(_translate("dialogUI", "SET"))
        self.cancelTimeBtn.setText(_translate("dialogUI", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogUI = QtWidgets.QDialog()
    ui = Ui_dialogUI()
    ui.setupUi(dialogUI)
    dialogUI.show()
    sys.exit(app.exec_())
