from PyQt5.QtGui import (
    QColor,
    QPen,
    QBrush,
    QPolygon
)

from PyQt5.QtCore import QPoint

from objects.base_object import BaseObject


class Rectangle(BaseObject):

    def __init__(
        self,
        x,
        y,
        width,
        height,
        vp,
        color="#D8A7B1"
    ):

        super().__init__(x, y, color)

        self.width = width
        self.height = height

        self.vp = vp

    def draw(self, painter):

        painter.setPen(
            QPen(QColor("#7A4E57"), 2)
        )

        painter.setBrush(
            QBrush(QColor(self.color))
        )

        # FRONT FACE

        p1 = QPoint(
            self.x,
            self.y
        )

        p2 = QPoint(
            self.x + self.width,
            self.y
        )

        p3 = QPoint(
            self.x + self.width,
            self.y + self.height
        )

        p4 = QPoint(
            self.x,
            self.y + self.height
        )

        # DEPTH

        depth = 0.35

        p5 = QPoint(
            int(p1.x() + (self.vp.x() - p1.x()) * depth),
            int(p1.y() + (self.vp.y() - p1.y()) * depth)
        )

        p6 = QPoint(
            int(p2.x() + (self.vp.x() - p2.x()) * depth),
            int(p2.y() + (self.vp.y() - p2.y()) * depth)
        )

        p7 = QPoint(
            int(p3.x() + (self.vp.x() - p3.x()) * depth),
            int(p3.y() + (self.vp.y() - p3.y()) * depth)
        )

        # FRONT

        painter.drawPolygon(
            QPolygon([p1, p2, p3, p4])
        )

        # SIDE

        painter.drawPolygon(
            QPolygon([p2, p6, p7, p3])
        )

        # TOP

        painter.drawPolygon(
            QPolygon([p1, p2, p6, p5])
        )

    def contains_point(self, x, y):

        min_x = min(
            self.x,
            self.x + self.width
        )

        max_x = max(
            self.x,
            self.x + self.width
        )

        min_y = min(
            self.y,
            self.y + self.height
        )

        max_y = max(
            self.y,
            self.y + self.height
        )

        padding = 40

        return (
            min_x - padding <= x <= max_x + padding
            and
            min_y - padding <= y <= max_y + padding
        )