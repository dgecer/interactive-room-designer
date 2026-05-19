from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from objects.rectangle import Rectangle
from objects.circle import Circle
from objects.line import Line
from objects.furniture import Furniture

from utils.grid import PerspectiveGrid

from utils.constants import (
    RECTANGLE_TOOL,
    CIRCLE_TOOL,
    LINE_TOOL,
    SOFA_TOOL,
    BED_TOOL,
    TABLE_TOOL,
    CHAIR_TOOL
)


class Canvas(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(1000, 700)

        self.objects = []

        self.current_tool = None

        self.perspective_mode = "1-point"

        self.drawing = False

        self.start_x = 0
        self.start_y = 0

        self.current_shape = None

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(
            self.rect(),
            Qt.white
        )

        PerspectiveGrid.draw(
            painter,
            self.width(),
            self.height(),
            self.perspective_mode
        )

        for obj in self.objects:
            obj.draw(painter)

        if self.current_shape:
            self.current_shape.draw(painter)

    def mousePressEvent(self, event):

        x = event.x()
        y = event.y()

        # RECTANGLE

        if self.current_tool == RECTANGLE_TOOL:

            self.drawing = True

            self.start_x = x
            self.start_y = y

            self.current_shape = Rectangle(
                x,
                y,
                0,
                0
            )

        # CIRCLE

        elif self.current_tool == CIRCLE_TOOL:

            self.drawing = True

            self.start_x = x
            self.start_y = y

            self.current_shape = Circle(
                x,
                y,
                0
            )

        # LINE

        elif self.current_tool == LINE_TOOL:

            self.drawing = True

            self.start_x = x
            self.start_y = y

            self.current_shape = Line(
                x,
                y,
                x,
                y
            )

        # SOFA

        elif self.current_tool == SOFA_TOOL:

            sofa = Furniture(
                x,
                y,
                160,
                90,
                "Sofa",
                self.perspective_mode,
                "#7D8ABC"
            )

            self.objects.append(sofa)

            self.update()

        # BED

        elif self.current_tool == BED_TOOL:

            bed = Furniture(
                x,
                y,
                180,
                110,
                "Bed",
                self.perspective_mode,
                "#C499BA"
            )

            self.objects.append(bed)

            self.update()

        # TABLE

        elif self.current_tool == TABLE_TOOL:

            table = Furniture(
                x,
                y,
                100,
                100,
                "Table",
                self.perspective_mode,
                "#A67B5B"
            )

            self.objects.append(table)

            self.update()

        # CHAIR

        elif self.current_tool == CHAIR_TOOL:

            chair = Furniture(
                x,
                y,
                70,
                70,
                "Chair",
                self.perspective_mode,
                "#909090"
            )

            self.objects.append(chair)

            self.update()

    def mouseMoveEvent(self, event):

        if not self.drawing or not self.current_shape:
            return

        x = event.x()
        y = event.y()

        # RECTANGLE

        if self.current_tool == RECTANGLE_TOOL:

            self.current_shape.width = (
                x - self.start_x
            )

            self.current_shape.height = (
                y - self.start_y
            )

        # CIRCLE

        elif self.current_tool == CIRCLE_TOOL:

            radius = max(
                abs(x - self.start_x),
                abs(y - self.start_y)
            ) // 2

            self.current_shape.radius = radius

        # LINE

        elif self.current_tool == LINE_TOOL:

            self.current_shape.x2 = x
            self.current_shape.y2 = y

        self.update()

    def mouseReleaseEvent(self, event):

        if self.drawing and self.current_shape:

            self.objects.append(
                self.current_shape
            )

            self.current_shape = None

            self.drawing = False

            self.update()