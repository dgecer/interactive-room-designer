from PyQt5.QtGui import QColor, QPen
from PyQt5.QtCore import Qt


class PerspectiveGrid:

    @staticmethod
    def draw(painter, width, height, mode):

        painter.setRenderHint(painter.Antialiasing)

        if mode == "1-point":
            PerspectiveGrid.draw_one_point(
                painter,
                width,
                height
            )

        elif mode == "2-point":
            PerspectiveGrid.draw_two_point(
                painter,
                width,
                height
            )

        elif mode == "3-point":
            PerspectiveGrid.draw_three_point(
                painter,
                width,
                height
            )

    @staticmethod
    def draw_one_point(painter, width, height):

        center_x = width // 2
        center_y = height // 2

        painter.setPen(
            QPen(QColor(220, 220, 220), 1)
        )

        step = 40

        for x in range(0, width, step):

            painter.drawLine(
                x,
                0,
                center_x,
                center_y
            )

            painter.drawLine(
                x,
                height,
                center_x,
                center_y
            )

        for y in range(0, height, step):

            painter.drawLine(
                0,
                y,
                center_x,
                center_y
            )

            painter.drawLine(
                width,
                y,
                center_x,
                center_y
            )

        painter.setPen(
            QPen(QColor(255, 80, 80), 2)
        )

        painter.drawEllipse(
            center_x - 5,
            center_y - 5,
            10,
            10
        )

    @staticmethod
    def draw_two_point(painter, width, height):

        left_vp_x = width // 4
        right_vp_x = width - width // 4

        horizon_y = height // 2

        painter.setPen(
            QPen(QColor(210, 210, 210), 1)
        )

        step = 40

        for x in range(0, width, step):

            painter.drawLine(
                x,
                height,
                left_vp_x,
                horizon_y
            )

            painter.drawLine(
                x,
                height,
                right_vp_x,
                horizon_y
            )

        painter.setPen(
            QPen(QColor(255, 100, 100), 2)
        )

        painter.drawLine(
            0,
            horizon_y,
            width,
            horizon_y
        )

        painter.drawEllipse(
            left_vp_x - 5,
            horizon_y - 5,
            10,
            10
        )

        painter.drawEllipse(
            right_vp_x - 5,
            horizon_y - 5,
            10,
            10
        )

    @staticmethod
    def draw_three_point(painter, width, height):

        top_x = width // 2
        top_y = height // 5

        left_x = width // 4
        horizon_y = height // 2

        right_x = width - width // 4

        painter.setPen(
            QPen(QColor(220, 220, 220), 1)
        )

        step = 50

        for x in range(0, width, step):

            painter.drawLine(
                x,
                height,
                left_x,
                horizon_y
            )

            painter.drawLine(
                x,
                height,
                right_x,
                horizon_y
            )

            painter.drawLine(
                x,
                height,
                top_x,
                top_y
            )

        painter.setPen(
            QPen(QColor(255, 120, 120), 2)
        )

        painter.drawEllipse(
            top_x - 5,
            top_y - 5,
            10,
            10
        )

        painter.drawEllipse(
            left_x - 5,
            horizon_y - 5,
            10,
            10
        )

        painter.drawEllipse(
            right_x - 5,
            horizon_y - 5,
            10,
            10
        )