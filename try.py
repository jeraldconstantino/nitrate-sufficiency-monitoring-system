from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # create the frame
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frame.setGeometry(0, 0, self.width(), self.height())
        self.frame.setVisible(False)

        # create the button
        self.button = QtWidgets.QPushButton("Show Frame", self)
        self.button.clicked.connect(self.toggleFrameVisibility)

        # set the central widget
        central_widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(central_widget)
        layout.addWidget(self.button)
        self.setCentralWidget(central_widget)

    def toggleFrameVisibility(self):
        self.frame.setVisible(not self.frame.isVisible())