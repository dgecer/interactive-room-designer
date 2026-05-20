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
from objects.triangle import Triangle

from utils.constants import (
    PERSPECTIVE_TOOL,
    ROOM_TOOL,
    RECTANGLE_TOOL,
    LINE_TOOL,
    TRIANGLE_TOOL,
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

        # DRAGGING

        self.dragging_object = False

        self.drag_offset_x = 0
        self.drag_offset_y = 0

        # RESIZE

        self.resizing_object = False

        self.resize_handle_size = 14

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

                    # RESIZE HANDLE

                    handle_x = (
                        obj.x + obj.width
                    )

                    handle_y = (
                        obj.y + obj.height
                    )

                    painter.setBrush(
                        QColor("#D4AF37")
                    )

                    painter.drawRect(
                        handle_x - 7,
                        handle_y - 7,
                        14,
                        14
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

                    # RESIZE HANDLE

                    if hasattr(obj, "width"):

                        handle_x = (
                            obj.x + obj.width
                        )

                        handle_y = (
                            obj.y + obj.height
                        )

                        if (
                            abs(x - handle_x) < 10
                            and
                            abs(y - handle_y) < 10
                        ):

                            self.resizing_object = True

                            self.update()

                            return

                    # DRAGGING

                    self.dragging_object = True

                    self.drag_offset_x = (
                        x - obj.x
                    )

                    self.drag_offset_y = (
                        y - obj.y
                    )

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

        # TRIANGLE TOOL

        elif self.current_tool == TRIANGLE_TOOL:

            self.drawing = True

            self.start_x = x
            self.start_y = y

            self.current_shape = Triangle(
                x,
                y,
                0,
                0,
                self.room.vp
            )

    def mouseMoveEvent(self, event):

        x = event.x()
        y = event.y()

        # RESIZE OBJECT

        if (
            self.resizing_object
            and
            self.selected_object
        ):

            self.selected_object.width = (
                x - self.selected_object.x
            )

            self.selected_object.height = (
                y - self.selected_object.y
            )

            self.update()

            return

        # DRAG OBJECT

        if (
            self.dragging_object
            and
            self.selected_object
        ):

            self.selected_object.x = (
                x - self.drag_offset_x
            )

            self.selected_object.y = (
                y - self.drag_offset_y
            )

            self.update()

            return

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

        # ROOM DRAWING

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

        # NO DRAWING

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

        # TRIANGLE

        elif self.current_tool == TRIANGLE_TOOL:

            self.current_shape.width = (
                x - self.start_x
            )

            self.current_shape.height = (
                y - self.start_y
            )

        self.update()

    def mouseReleaseEvent(self, event):

        self.selected_vp = False

        self.dragging_object = False

        self.resizing_object = False

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

        # DELETE

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