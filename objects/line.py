from PyQt5.QtGui import QColor, QPen

from objects.base_object import BaseObject


class Line(BaseObject):
    def __init__(self, x1, y1, x2, y2, color="black"):
        super().__init__(x1, y1, color)

        self.x2 = x2
        self.y2 = y2

    def draw(self, painter):
        pen = QPen(QColor(self.color), 3)

        painter.setPen(pen)

        painter.drawLine(
            self.x,
            self.y,
            self.x2,
            self.y2
        )