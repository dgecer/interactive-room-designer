from PyQt5.QtGui import (
    QColor,
    QBrush,
    QPen,
    QPolygon
)

from PyQt5.QtCore import (
    QPoint,
    Qt
)


class Room:

    def __init__(
        self,
        width,
        height,
        vanishing_point
    ):

        self.width = width
        self.height = height

        self.vp = vanishing_point

        # BACK WALL

        self.bw_x = 250
        self.bw_y = 170

        self.bw_w = 500
        self.bw_h = 320

    def draw(
        self,
        painter,
        width,
        height
    ):

        self.width = width
        self.height = height

        left = self.bw_x
        right = self.bw_x + self.bw_w

        top = self.bw_y
        bottom = self.bw_y + self.bw_h

        painter.setPen(Qt.NoPen)

        # BACK WALL

        painter.setBrush(
            QBrush(QColor("#F7EAEA"))
        )

        back_wall = QPolygon([
            QPoint(left, top),
            QPoint(right, top),
            QPoint(right, bottom),
            QPoint(left, bottom)
        ])

        painter.drawPolygon(back_wall)

        # FLOOR

        painter.setBrush(
            QBrush(QColor("#F3DDDD"))
        )

        floor = QPolygon([
            QPoint(left, bottom),
            QPoint(right, bottom),
            QPoint(width, height),
            QPoint(0, height)
        ])

        painter.drawPolygon(floor)

        # CEILING

        painter.setBrush(
            QBrush(QColor("#FFF5F5"))
        )

        ceiling = QPolygon([
            QPoint(0, 0),
            QPoint(width, 0),
            QPoint(right, top),
            QPoint(left, top)
        ])

        painter.drawPolygon(ceiling)

        # LEFT WALL

        painter.setBrush(
            QBrush(QColor("#F0DADA"))
        )

        left_wall = QPolygon([
            QPoint(0, 0),
            QPoint(left, top),
            QPoint(left, bottom),
            QPoint(0, height)
        ])

        painter.drawPolygon(left_wall)

        # RIGHT WALL

        painter.setBrush(
            QBrush(QColor("#ECD1D1"))
        )

        right_wall = QPolygon([
            QPoint(width, 0),
            QPoint(right, top),
            QPoint(right, bottom),
            QPoint(width, height)
        ])

        painter.drawPolygon(right_wall)

        # GRID

        painter.setPen(
            QPen(
                QColor("#E7CFCF"),
                1
            )
        )

        step = 40

        # FLOOR GRID

        for x in range(0, width, step):

            painter.drawLine(
                x,
                height,
                self.vp.x(),
                self.vp.y()
            )

        for y in range(bottom, height, step):

            painter.drawLine(
                0,
                y,
                width,
                y
            )

        # CEILING GRID

        for x in range(0, width, step):

            painter.drawLine(
                x,
                0,
                self.vp.x(),
                self.vp.y()
            )

        for y in range(0, top, step):

            painter.drawLine(
                0,
                y,
                width,
                y
            )

        # SIDE WALLS

        for y in range(0, height, step):

            painter.drawLine(
                0,
                y,
                self.vp.x(),
                self.vp.y()
            )

            painter.drawLine(
                width,
                y,
                self.vp.x(),
                self.vp.y()
            )

        # VANISHING POINT

        painter.setBrush(
            QBrush(QColor("#D48C8C"))
        )

        painter.setPen(
            QPen(
                QColor("#A35C5C"),
                2
            )
        )

        painter.drawEllipse(
            self.vp.x() - 8,
            self.vp.y() - 8,
            16,
            16
        )