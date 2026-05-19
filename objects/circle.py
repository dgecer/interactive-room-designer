from PyQt5.QtGui import (
    QColor,
    QPen,
    QBrush
)

from objects.base_object import BaseObject


class Circle(BaseObject):

    def __init__(
        self,
        x,
        y,
        radius,
        vp,
        color="#D97B66"
    ):

        super().__init__(x, y, color)

        self.radius = radius

        self.vp = vp

    def draw(self, painter):

        painter.setPen(
            QPen(QColor("black"), 2)
        )

        painter.setBrush(
            QBrush(QColor(self.color))
        )

        # PERSPECTIVE SCALE

        distance = abs(
            self.vp.y() - self.y
        )

        scale = max(
            0.5,
            1 - (distance / 1200)
        )

        width = int(
            self.radius * 2
        )

        height = int(
            self.radius * 2 * scale
        )

        painter.drawEllipse(
            self.x,
            self.y,
            width,
            height
        )

    def contains_point(self, x, y):

        dx = x - self.x
        dy = y - self.y

        return (
            dx * dx + dy * dy
        ) <= self.radius * self.radius