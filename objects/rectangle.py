from PyQt5.QtGui import QColor, QPen, QBrush
from objects.base_object import BaseObject


class Rectangle(BaseObject):
    def __init__(self, x, y, width, height, color="blue"):
        super().__init__(x, y, color)

        self.width = width
        self.height = height

    def draw(self, painter):
        pen = QPen(QColor(self.color), 2)
        painter.setPen(pen)

        brush = QBrush(QColor(self.color))
        painter.setBrush(brush)

        painter.drawRect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def contains_point(self, x, y):
        return (
            self.x <= x <= self.x + self.width
            and
            self.y <= y <= self.y + self.height
        )