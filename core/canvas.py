from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import (
    QPainter,
    QPen,
    QColor
)

from PyQt5.QtCore import Qt, QPoint

from objects.rectangle import Rectangle
from objects.line import Line
from objects.room import Room

from utils.constants import (
    PERSPECTIVE_TOOL,
    ROOM_TOOL,

    RECTANGLE_TOOL,
    LINE_TOOL,

    SELECT_TOOL
)


class Canvas(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(1000, 700)

        self.setFocusPolicy(
            Qt.StrongFocus
        )

        self.objects = []

        self.current_tool = PERSPECTIVE_TOOL

        self.drawing = False
        self.drawing_room = False

        self.start_x = 0
        self.start_y = 0

        self.current_shape = None

        self.selected_object = None

        # ROOM

        self.room = Room(
            self.width(),
            self.height(),
            QPoint(
                self.width() // 2,
                self.height() // 2
            )
        )

        self.selected_vp = False

    def set_tool(self, tool):

        self.current_tool = tool

        self.selected_vp = False

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        # BACKGROUND

        painter.fillRect(
            self.rect(),
            QColor("#FFF8F8")
        )

        # HORIZON LINE

        painter.setPen(
            QPen(
                QColor("#C9A227"),
                2,
                Qt.DashLine
            )
        )

        painter.drawLine(
            0,
            self.room.vp.y(),
            self.width(),
            self.room.vp.y()
        )

        # ROOM

        self.room.draw(
            painter,
            self.width(),
            self.height()
        )

        # OBJECTS

        for obj in self.objects:

            obj.draw(painter)

            # SELECTION OUTLINE

            if obj == self.selected_object:

                painter.setPen(
                    QPen(
                        QColor("#D4AF37"),
                        2,
                        Qt.DashLine
                    )
                )

                if hasattr(obj, "width"):

                    painter.drawRect(
                        min(obj.x, obj.x + obj.width) - 8,
                        min(obj.y, obj.y + obj.height) - 8,
                        abs(obj.width) + 16,
                        abs(obj.height) + 16
                    )

        # CURRENT SHAPE

        if self.current_shape:

            self.current_shape.draw(
                painter
            )

    def mousePressEvent(self, event):

        x = event.x()
        y = event.y()

        # SELECT TOOL

        if self.current_tool == SELECT_TOOL:

            self.selected_object = None

            for obj in reversed(self.objects):

                if (
                    hasattr(obj, "contains_point")
                    and
                    obj.contains_point(x, y)
                ):

                    self.selected_object = obj

                    break

            self.update()

            return

        # PERSPECTIVE TOOL

        if self.current_tool == PERSPECTIVE_TOOL:

            distance = (
                (x - self.room.vp.x()) ** 2
                +
                (y - self.room.vp.y()) ** 2
            ) ** 0.5

            if distance < 15:

                self.selected_vp = True

            return

        # ROOM TOOL

        if self.current_tool == ROOM_TOOL:

            self.drawing_room = True

            self.start_x = x
            self.start_y = y

            return

        # RECTANGLE TOOL

        if self.current_tool == RECTANGLE_TOOL:

            self.drawing = True

            self.start_x = x
            self.start_y = y

            self.current_shape = Rectangle(
                x,
                y,
                0,
                0,
                self.room.vp
            )

        # LINE TOOL

        elif self.current_tool == LINE_TOOL:

            self.drawing = True

            self.start_x = x
            self.start_y = y

            self.current_shape = Line(
                x,
                y,
                x,
                y,
                self.room.vp
            )

    def mouseMoveEvent(self, event):

        x = event.x()
        y = event.y()

        # MOVE VP

        if (
            self.selected_vp
            and
            self.current_tool == PERSPECTIVE_TOOL
        ):

            self.room.vp.setX(x)

            self.room.vp.setY(y)

            self.update()

            return

        # ROOM DRAW

        if (
            self.current_tool == ROOM_TOOL
            and
            self.drawing_room
        ):

            self.room.bw_x = min(
                x,
                self.start_x
            )

            self.room.bw_y = min(
                y,
                self.start_y
            )

            self.room.bw_w = abs(
                x - self.start_x
            )

            self.room.bw_h = abs(
                y - self.start_y
            )

            self.update()

            return

        if (
            not self.drawing
            or
            not self.current_shape
        ):

            return

        # RECTANGLE

        if self.current_tool == RECTANGLE_TOOL:

            self.current_shape.width = (
                x - self.start_x
            )

            self.current_shape.height = (
                y - self.start_y
            )

        # LINE

        elif self.current_tool == LINE_TOOL:

            self.current_shape.x2 = x
            self.current_shape.y2 = y

        self.update()

    def mouseReleaseEvent(self, event):

        self.selected_vp = False

        # ROOM

        if self.drawing_room:

            self.drawing_room = False

            self.update()

            return

        # SHAPES

        if (
            self.drawing
            and
            self.current_shape
        ):

            self.objects.append(
                self.current_shape
            )

            self.current_shape = None

            self.drawing = False

            self.update()

    def keyPressEvent(self, event):

        # DELETE OBJECT

        if (
            event.key() == Qt.Key_Delete
            and
            self.selected_object
        ):

            self.objects.remove(
                self.selected_object
            )

            self.selected_object = None

            self.update()

        # CHANGE COLOR

        elif (
            event.key() == Qt.Key_C
            and
            self.selected_object
        ):

            current = self.selected_object.color

            colors = [
                "#D8A7B1",
                "#E6B8A2",
                "#CFA5D6",
                "#F0C987",
                "#9BB8D3"
            ]

            index = (
                colors.index(current)
                if current in colors
                else 0
            )

            self.selected_object.color = colors[
                (index + 1) % len(colors)
            ]

            self.update()

    def wheelEvent(self, event):

        if not self.selected_object:
            return

        delta = event.angleDelta().y()

        scale = 15 if delta > 0 else -15

        # RECTANGLE RESIZE

        if hasattr(
            self.selected_object,
            "width"
        ):

            self.selected_object.width = max(
                20,
                self.selected_object.width + scale
            )

        if hasattr(
            self.selected_object,
            "height"
        ):

            self.selected_object.height = max(
                20,
                self.selected_object.height + scale
            )

        self.update()