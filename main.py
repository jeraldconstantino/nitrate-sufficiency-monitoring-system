from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MessageBox(QWidget):
    def __init__(self, title, message, icon_path, parent=None):
        super().__init__(parent=parent)
        
        # Set window properties
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(300, 150)
        
        # Create widgets
        self.icon_label = QLabel()
        self.title_label = QLabel(title)
        self.message_label = QLabel(message)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        
        # Set widget properties
        if icon_path:
            pixmap = QPixmap(icon_path)
            if not pixmap.isNull():
                self.icon_label.setPixmap(pixmap.scaled(64, 64))
        self.title_label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        self.message_label.setWordWrap(True)
        self.ok_button.setFixedSize(100, 30)
        self.ok_button.setStyleSheet("font-size: 12pt;")
        
        # Create layouts
        icon_layout = QHBoxLayout()
        icon_layout.addWidget(self.icon_label, alignment=Qt.AlignHCenter)
        
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.title_label)
        content_layout.addWidget(self.message_label)
        content_layout.addWidget(self.ok_button, alignment=Qt.AlignHCenter)
        
        main_layout = QHBoxLayout()
        main_layout.addLayout(icon_layout)
        main_layout.addLayout(content_layout)
        
        self.setLayout(main_layout)
    
    def accept(self):
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    message_box = MessageBox("Error", "An error occurred while processing your request.", "invalid_path.png")
    message_box.show()
    app.exec_()
