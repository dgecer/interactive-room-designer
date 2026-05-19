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
        perspective_mode,
        color="gray"
    ):
        super().__init__(x, y, color)

        self.width = width
        self.height = height

        self.furniture_type = furniture_type

        self.perspective_mode = perspective_mode

    def draw(self, painter):

        painter.setPen(
            QPen(QColor("black"), 2)
        )

        painter.setBrush(
            QBrush(QColor(self.color))
        )

        if self.perspective_mode == "1-point":

            points = [
                QPoint(self.x, self.y),

                QPoint(
                    self.x + self.width,
                    self.y
                ),

                QPoint(
                    self.x + self.width - 25,
                    self.y + self.height
                ),

                QPoint(
                    self.x - 25,
                    self.y + self.height
                )
            ]

        elif self.perspective_mode == "2-point":

            points = [
                QPoint(self.x, self.y),

                QPoint(
                    self.x + self.width,
                    self.y - 20
                ),

                QPoint(
                    self.x + self.width - 30,
                    self.y + self.height
                ),

                QPoint(
                    self.x - 30,
                    self.y + self.height - 10
                )
            ]

        else:

            points = [
                QPoint(self.x, self.y),

                QPoint(
                    self.x + self.width,
                    self.y - 30
                ),

                QPoint(
                    self.x + self.width - 40,
                    self.y + self.height
                ),

                QPoint(
                    self.x - 20,
                    self.y + self.height - 20
                )
            ]

        polygon = QPolygon(points)

        painter.drawPolygon(polygon)

        painter.drawText(
            self.x + 10,
            self.y + 20,
            self.furniture_type.upper()
        )