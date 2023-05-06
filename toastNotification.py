from PyQt5.QtWidgets import QMessageBox, QFrame, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class Toast(QMessageBox):
    def __init__(self, message, duration=2000):
        super().__init__()
        self.setText(message)
        self.setStandardButtons(QMessageBox.NoButton)
        self.setFrameStyle(QFrame.NoFrame)
        self.setStyleSheet("background-color: green; color: white; font-size: 16px;")
        self.buttonClicked.connect(self.close)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.FramelessWindowHint)
        self.show()
        self.timer = self.startTimer(duration)

    def timerEvent(self, event):
        self.close()
        self.killTimer(self.timer)