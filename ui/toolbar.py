from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QColorDialog,
    QFileDialog,
    QMessageBox,
    QShortcut
)

from PyQt5.QtGui import QKeySequence

from utils.constants import (
    SELECT_TOOL,
    ROOM_TOOL,
    PERSPECTIVE_TOOL,
    RECTANGLE_TOOL,
    TRIANGLE_TOOL,
    LINE_TOOL
)

from utils.file_handler import (
    save_scene,
    load_scene
)


class ToolBar(QWidget):

    def __init__(self, canvas):
        super().__init__()

        self.canvas = canvas

        self.setFixedWidth(200)

        layout = QVBoxLayout()

        # TOOL BUTTONS

        self.buttons = {

            "Set Perspective": PERSPECTIVE_TOOL,

            "Select": SELECT_TOOL,

            "Room": ROOM_TOOL,

            "Rectangle": RECTANGLE_TOOL,

            "Triangle": TRIANGLE_TOOL,

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

        # ROTATE BUTTON

        self.rotate_button = QPushButton(
            "Rotate"
        )

        self.rotate_button.clicked.connect(
            self.rotate_object
        )

        layout.addWidget(
            self.rotate_button
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

        # SAVE BUTTON

        self.save_button = QPushButton(
            "Save Scene"
        )

        self.save_button.clicked.connect(
            self.save_current_scene
        )

        layout.addWidget(
            self.save_button
        )

        # LOAD BUTTON

        self.load_button = QPushButton(
            "Load Scene"
        )

        self.load_button.clicked.connect(
            self.load_saved_scene
        )

        layout.addWidget(
            self.load_button
        )

        layout.addStretch()

        self.setLayout(layout)

        # SHORTCUTS

        self.save_shortcut = QShortcut(
            QKeySequence("Ctrl+S"),
            self
        )

        self.save_shortcut.activated.connect(
            self.save_current_scene
        )

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

    def rotate_object(self):

        obj = self.canvas.selected_object

        if not obj:
            return

        obj.rotation += 15

        self.canvas.update()

    def change_color(self):

        obj = self.canvas.selected_object

        if not obj:
            return

        color = QColorDialog.getColor()

        if color.isValid():

            obj.color = color.name()

            self.canvas.update()

    def save_current_scene(self):

        filename, _ = QFileDialog.getSaveFileName(

            self,

            "Save Scene",

            "scene.json",

            "JSON Files (*.json)"
        )

        if not filename:
            return

        save_scene(
            self.canvas.objects,
            filename
        )

        QMessageBox.information(

            self,

            "Saved",

            "Scene saved successfully."
        )

    def load_saved_scene(self):

        filename, _ = QFileDialog.getOpenFileName(

            self,

            "Load Scene",

            "",

            "JSON Files (*.json)"
        )

        if not filename:
            return

        data = load_scene(filename)

        print(data)

        QMessageBox.information(

            self,

            "Loaded",

            "Scene loaded successfully."
        )