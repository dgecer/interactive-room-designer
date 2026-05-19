from PyQt5.QtGui import QColor, QPen, QBrush
from PyQt5.QtCore import QPoint, Qt


class PerspectiveGrid:

    @staticmethod
    def draw(
        painter,
        width,
        height,
        mode,
        vanishing_points,
        horizon_y,
        room_margin
    ):

        painter.setRenderHint(
            painter.Antialiasing
        )

        PerspectiveGrid.draw_background(
            painter,
            width,
            height,
            vanishing_points,
            horizon_y,
            room_margin
        )

        if mode == "1-point":

            PerspectiveGrid.draw_one_point(
                painter,
                width,
                height,
                vanishing_points
            )

        elif mode == "2-point":

            PerspectiveGrid.draw_two_point(
                painter,
                width,
                height,
                vanishing_points
            )

        elif mode == "3-point":

            PerspectiveGrid.draw_three_point(
                painter,
                width,
                height,
                vanishing_points
            )

    @staticmethod
    def draw_background(
        painter,
        width,
        height,
        vanishing_points,
        horizon_y,
        room_margin
    ):

        left = room_margin
        right = width - room_margin

        top = room_margin
        bottom = height - room_margin

        # BACK WALL

        painter.setPen(Qt.NoPen)

        painter.setBrush(
            QBrush(QColor(244, 244, 248))
        )

        back_wall = [
            QPoint(left, top),
            QPoint(right, top),
            QPoint(right, bottom),
            QPoint(left, bottom)
        ]

        painter.drawPolygon(back_wall)

        # FLOOR

        painter.setBrush(
            QBrush(QColor(220, 220, 228))
        )

        floor = [
            QPoint(left, bottom),
            QPoint(right, bottom),
            QPoint(width, height),
            QPoint(0, height)
        ]

        painter.drawPolygon(floor)

        # CEILING

        painter.setBrush(
            QBrush(QColor(252, 252, 255))
        )

        ceiling = [
            QPoint(0, 0),
            QPoint(width, 0),
            QPoint(right, top),
            QPoint(left, top)
        ]

        painter.drawPolygon(ceiling)

        # LEFT WALL

        painter.setBrush(
            QBrush(QColor(230, 230, 236))
        )

        left_wall = [
            QPoint(0, 0),
            QPoint(left, top),
            QPoint(left, bottom),
            QPoint(0, height)
        ]

        painter.drawPolygon(left_wall)

        # RIGHT WALL

        painter.setBrush(
            QBrush(QColor(225, 225, 232))
        )

        right_wall = [
            QPoint(width, 0),
            QPoint(right, top),
            QPoint(right, bottom),
            QPoint(width, height)
        ]

        painter.drawPolygon(right_wall)    
         
    def draw_one_point(
        painter,
        width,
        height,
        vanishing_points
    ):

        vp = vanishing_points[0]

        painter.setPen(
            QPen(QColor(210, 210, 210), 1)
        )

        step = 40

        # FLOOR

        for x in range(0, self.width, step):

            painter.drawLine(
                x,
                self.height,
                self.vp.x(),
                self.vp.y()
            )

        # CEILING

        for x in range(0, self.width, step):

            painter.drawLine(
                x,
                0,
                self.vp.x(),
                self.vp.y()
            )

        # LEFT WALL

        for y in range(0, self.height, step):

            painter.drawLine(
                0,
                y,
                self.vp.x(),
                self.vp.y()
            )

        # RIGHT WALL


    @staticmethod
    def draw_two_point(
        painter,
        width,
        height,
        vanishing_points
    ):

        left_vp = vanishing_points[0]
        right_vp = vanishing_points[1]

        painter.setPen(
            QPen(QColor(210, 210, 210), 1)
        )

        step = 40

        for x in range(0, width, step):

            painter.drawLine(
                x,
                height,
                left_vp.x(),
                left_vp.y()
            )

            painter.drawLine(
                x,
                height,
                right_vp.x(),
                right_vp.y()
            )

        PerspectiveGrid.draw_vanishing_point(
            painter,
            left_vp
        )

        PerspectiveGrid.draw_vanishing_point(
            painter,
            right_vp
        )

    @staticmethod
    def draw_three_point(
        painter,
        width,
        height,
        vanishing_points
    ):

        left_vp = vanishing_points[0]
        right_vp = vanishing_points[1]
        top_vp = vanishing_points[2]

        painter.setPen(
            QPen(QColor(210, 210, 210), 1)
        )

        step = 40

        for x in range(0, width, step):

            painter.drawLine(
                x,
                height,
                left_vp.x(),
                left_vp.y()
            )

            painter.drawLine(
                x,
                height,
                right_vp.x(),
                right_vp.y()
            )

            painter.drawLine(
                x,
                height,
                top_vp.x(),
                top_vp.y()
            )

        PerspectiveGrid.draw_vanishing_point(
            painter,
            left_vp
        )

        PerspectiveGrid.draw_vanishing_point(
            painter,
            right_vp
        )

        PerspectiveGrid.draw_vanishing_point(
            painter,
            top_vp
        )

    @staticmethod
    def draw_vanishing_point(
        painter,
        point
    ):

        painter.setBrush(
            QBrush(QColor(255, 80, 80))
        )

        painter.setPen(
            QPen(QColor(180, 0, 0), 2)
        )

        painter.drawEllipse(
            point.x() - 7,
            point.y() - 7,
            14,
            14
        )