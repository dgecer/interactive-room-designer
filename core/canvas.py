from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(self.rect(), Qt.white)