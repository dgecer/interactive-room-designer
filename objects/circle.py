from PyQt5.QtGui import QColor, QPen, QBrush

from objects.base_object import BaseObject


class Circle(BaseObject):
    def __init__(self, x, y, radius, color="red"):
        super().__init__(x, y, color)

        self.radius = radius

    def draw(self, painter):
        pen = QPen(QColor(self.color), 2)
        painter.setPen(pen)

        brush = QBrush(QColor(self.color))
        painter.setBrush(brush)

        painter.drawEllipse(
            self.x,
            self.y,
            self.radius * 2,
            self.radius * 2
        )