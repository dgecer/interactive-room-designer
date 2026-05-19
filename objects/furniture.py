from PyQt5.QtGui import (
    QColor,
    QPen,
    QBrush,
    QPolygon
)

from PyQt5.QtCore import QPoint

from objects.base_object import BaseObject


class Furniture(BaseObject):

    def __init__(
        self,
        x,
        y,
        width,
        height,
        furniture_type,
        vp,
        color="gray"
    ):

        super().__init__(x, y, color)

        self.width = width
        self.height = height

        self.furniture_type = furniture_type

        self.vp = vp

    def draw(self, painter):

        painter.setPen(
            QPen(QColor("black"), 2)
        )

        painter.setBrush(
            QBrush(QColor(self.color))
        )

        # PERSPECTIVE DEPTH

        depth_x = int(
            (self.vp.x() - self.x) * 0.08
        )

        depth_y = int(
            (self.vp.y() - self.y) * 0.08
        )

        # PERSPECTIVE POLYGON

        points = [

            QPoint(
                self.x,
                self.y
            ),

            QPoint(
                self.x + self.width,
                self.y
            ),

            QPoint(
                self.x + self.width + depth_x,
                self.y + depth_y
            ),

            QPoint(
                self.x + depth_x,
                self.y + self.height + depth_y
            )
        ]

        polygon = QPolygon(points)

        painter.drawPolygon(polygon)

        # LABEL

        painter.drawText(
            self.x + 10,
            self.y + 25,
            self.furniture_type.upper()
        )