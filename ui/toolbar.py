from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton
)

from utils.constants import (
    SELECT_TOOL,
    ROOM_TOOL,
    PERSPECTIVE_TOOL,
    RECTANGLE_TOOL,
    LINE_TOOL
)


class ToolBar(QWidget):

    def __init__(self, canvas):
        super().__init__()

        self.canvas = canvas

        self.setFixedWidth(180)

        layout = QVBoxLayout()

        # TOOL BUTTONS

        self.buttons = {

            "Set Perspective": PERSPECTIVE_TOOL,

            "Select": SELECT_TOOL,

            "Room": ROOM_TOOL,

            "Rectangle": RECTANGLE_TOOL,

            "Line": LINE_TOOL
        }

        for name, tool in self.buttons.items():

            button = QPushButton(name)

            button.clicked.connect(
                lambda _, t=tool:
                self.set_tool(t)
            )

            layout.addWidget(button)

        # DELETE BUTTON

        self.delete_button = QPushButton(
            "Delete Object"
        )

        self.delete_button.clicked.connect(
            self.delete_selected
        )

        layout.addWidget(
            self.delete_button
        )

        # COLOR BUTTON

        self.color_button = QPushButton(
            "Change Color"
        )

        self.color_button.clicked.connect(
            self.change_color
        )

        layout.addWidget(
            self.color_button
        )

        # RESIZE BUTTONS

        self.grow_button = QPushButton(
            "Increase Size"
        )

        self.grow_button.clicked.connect(
            self.grow_object
        )

        layout.addWidget(
            self.grow_button
        )

        self.shrink_button = QPushButton(
            "Decrease Size"
        )

        self.shrink_button.clicked.connect(
            self.shrink_object
        )

        layout.addWidget(
            self.shrink_button
        )

        layout.addStretch()

        self.setLayout(layout)

        # STYLE

        self.setStyleSheet("""

            QWidget {

                background-color: #F7EAEA;

                border-right: 2px solid #D4AF37;
            }

            QPushButton {

                background-color: #EBC8C8;

                border: 2px solid #D4AF37;

                border-radius: 18px;

                min-height: 45px;

                padding: 8px;

                margin-top: 6px;

                font-size: 13px;

                font-weight: bold;

                color: #4A3B3B;
            }

            QPushButton:hover {

                background-color: #F6DADA;
            }

            QPushButton:pressed {

                background-color: #DDAFAF;
            }

        """)

    def set_tool(self, tool):

        self.canvas.set_tool(tool)

    def delete_selected(self):

        if not self.canvas.selected_object:
            return

        self.canvas.objects.remove(
            self.canvas.selected_object
        )

        self.canvas.selected_object = None

        self.canvas.update()

    def change_color(self):

        obj = self.canvas.selected_object

        if not obj:
            return

        colors = [
            "#D8A7B1",
            "#E6B8A2",
            "#CFA5D6",
            "#F0C987",
            "#9BB8D3"
        ]

        current = obj.color

        index = (
            colors.index(current)
            if current in colors
            else 0
        )

        obj.color = colors[
            (index + 1) % len(colors)
        ]

        self.canvas.update()

    def grow_object(self):

        obj = self.canvas.selected_object

        if not obj:
            return

        if hasattr(obj, "width"):

            obj.width += 15

        if hasattr(obj, "height"):

            obj.height += 15

        self.canvas.update()

    def shrink_object(self):

        obj = self.canvas.selected_object

        if not obj:
            return

        if hasattr(obj, "width"):

            obj.width = max(
                20,
                obj.width - 15
            )

        if hasattr(obj, "height"):

            obj.height = max(
                20,
                obj.height - 15
            )

        self.canvas.update()