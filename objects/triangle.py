from PyQt5.QtGui import (
    QColor,
    QPen,
    QBrush,
    QPolygon
)

from PyQt5.QtCore import QPoint

from objects.base_object import BaseObject


class Triangle(BaseObject):

    def __init__(
        self,
        x,
        y,
        width,
        height,
        vp,
        color="#CFA5D6"
    ):

        super().__init__(x, y, color)

        self.width = width
        self.height = height

        self.vp = vp

    def draw(self, painter):

        painter.save()

        painter.translate(
            self.x + self.width / 2,
            self.y + self.height / 2
        )

        painter.rotate(
            self.rotation
        )

        painter.translate(
            -(self.x + self.width / 2),
            -(self.y + self.height / 2)
        )

        painter.setPen(
            QPen(QColor("#7A4E57"), 2)
        )

        painter.setBrush(
            QBrush(QColor(self.color))
        )

        # FRONT

        p1 = QPoint(
            self.x + self.width // 2,
            self.y
        )

        p2 = QPoint(
            self.x,
            self.y + self.height
        )

        p3 = QPoint(
            self.x + self.width,
            self.y + self.height
        )

        # DEPTH

        depth = 0.35

        p4 = QPoint(
            int(p1.x() + (self.vp.x() - p1.x()) * depth),
            int(p1.y() + (self.vp.y() - p1.y()) * depth)
        )

        p5 = QPoint(
            int(p2.x() + (self.vp.x() - p2.x()) * depth),
            int(p2.y() + (self.vp.y() - p2.y()) * depth)
        )

        p6 = QPoint(
            int(p3.x() + (self.vp.x() - p3.x()) * depth),
            int(p3.y() + (self.vp.y() - p3.y()) * depth)
        )

        # FRONT FACE

        painter.drawPolygon(
            QPolygon([p1, p2, p3])
        )

        # SIDE FACE

        painter.drawPolygon(
            QPolygon([p2, p5, p6, p3])
        )

        # TOP FACE

        painter.drawPolygon(
            QPolygon([p1, p2, p5, p4])
        )

        painter.drawLine(p1, p4)
        painter.drawLine(p2, p5)
        painter.drawLine(p3, p6)

        painter.restore()

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

        padding = 30

        return (
            min_x - padding <= x <= max_x + padding
            and
            min_y - padding <= y <= max_y + padding
        )