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
    CIRCLE_TOOL,
    LINE_TOOL,

    SOFA_TOOL,
    BED_TOOL,
    TABLE_TOOL,
    CHAIR_TOOL,
    
    FLOOR_TOOL,
    CEILING_TOOL,
    WALL_TOOL
)


class ToolBar(QWidget):

    def __init__(self, canvas):
        super().__init__()

        self.canvas = canvas

        self.setFixedWidth(140)

        layout = QVBoxLayout()

        # BUTTONS
        
        self.perspective_button = QPushButton("Set Perspective")
        self.select_button = QPushButton("Select")

        self.room_button = QPushButton("Room")

        self.rectangle_button = QPushButton("Rectangle")
        self.circle_button = QPushButton("Circle")
        self.line_button = QPushButton("Line")

        self.sofa_button = QPushButton("Sofa")
        self.bed_button = QPushButton("Bed")
        self.table_button = QPushButton("Table")
        self.chair_button = QPushButton("Chair")
        
        self.floor_button = QPushButton("Floor")
        self.ceiling_button = QPushButton("Ceiling")
        self.wall_button = QPushButton("Wall")

        # CONNECTIONS

        self.perspective_button.clicked.connect(
            lambda: self.set_tool(PERSPECTIVE_TOOL)
        )

        self.floor_button.clicked.connect(
            lambda: self.set_tool(FLOOR_TOOL)
        )

        self.ceiling_button.clicked.connect(
            lambda: self.set_tool(CEILING_TOOL)
        )

        self.wall_button.clicked.connect(
            lambda: self.set_tool(WALL_TOOL)
        )
        
        self.select_button.clicked.connect(
            lambda: self.set_tool(SELECT_TOOL)
        )

        self.room_button.clicked.connect(
            lambda: self.set_tool(ROOM_TOOL)
        )

        self.rectangle_button.clicked.connect(
            lambda: self.set_tool(RECTANGLE_TOOL)
        )

        self.circle_button.clicked.connect(
            lambda: self.set_tool(CIRCLE_TOOL)
        )

        self.line_button.clicked.connect(
            lambda: self.set_tool(LINE_TOOL)
        )

        self.sofa_button.clicked.connect(
            lambda: self.set_tool(SOFA_TOOL)
        )

        self.bed_button.clicked.connect(
            lambda: self.set_tool(BED_TOOL)
        )

        self.table_button.clicked.connect(
            lambda: self.set_tool(TABLE_TOOL)
        )

        self.chair_button.clicked.connect(
            lambda: self.set_tool(CHAIR_TOOL)
        )

        # LAYOUT

        layout.addWidget(self.perspective_button)
        layout.addWidget(self.select_button)

        layout.addWidget(self.floor_button)
        layout.addWidget(self.ceiling_button)
        layout.addWidget(self.wall_button)
        
        layout.addWidget(self.room_button)

        layout.addWidget(self.rectangle_button)
        layout.addWidget(self.circle_button)
        layout.addWidget(self.line_button)

        layout.addWidget(self.sofa_button)
        layout.addWidget(self.bed_button)
        layout.addWidget(self.table_button)
        layout.addWidget(self.chair_button)

        layout.addStretch()

        self.setLayout(layout)

    def set_tool(self, tool):
        # Durum değişikliğini canvas'a bildir
        self.canvas.set_tool(tool)