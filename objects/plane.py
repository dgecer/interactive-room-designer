from PyQt5.QtGui import (
    QColor,
    QBrush,
    QPen,
    QPolygon
)

from PyQt5.QtCore import QPoint

from objects.base_object import BaseObject


class Plane(BaseObject):

    def __init__(
        self,
        points,
        color
    ):

        super().__init__(0, 0, color)

        self.points = points

    def draw(self, painter):

        painter.setPen(
            QPen(QColor(120, 120, 120), 2)
        )

        painter.setBrush(
            QBrush(QColor(self.color))
        )

        polygon = QPolygon(
            self.points
        )

        painter.drawPolygon(polygon)