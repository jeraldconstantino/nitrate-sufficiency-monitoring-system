from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(210, 180, 641, 91))
        self.message.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(72)
        self.message.setFont(font)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.pressMe = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_pressed())
        self.pressMe.setGeometry(QtCore.QRect(260, 330, 521, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(28)
        self.pressMe.setFont(font)
        self.pressMe.setObjectName("pressMe")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nitrate Sufficiency Monitoring System"))
        self.message.setText(_translate("MainWindow", "Hello World!"))
        self.pressMe.setText(_translate("MainWindow", "Press ME!"))

    def on_pressed(self):
        self.message.setText("Pressed!!!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
