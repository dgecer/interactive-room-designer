from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from utils.constants import (
    SELECT_TOOL,
    RECTANGLE_TOOL,
    CIRCLE_TOOL,
    LINE_TOOL,
    SOFA_TOOL,
    BED_TOOL,
    TABLE_TOOL,
    CHAIR_TOOL
)


class ToolBar(QWidget):
    def __init__(self, canvas):
        super().__init__()

        self.canvas = canvas

        self.setFixedWidth(120)

        layout = QVBoxLayout()

        self.select_button = QPushButton("Select")
        self.rectangle_button = QPushButton("Rectangle")
        self.circle_button = QPushButton("Circle")
        self.line_button = QPushButton("Line")
        self.sofa_button = QPushButton("Sofa")
        self.bed_button = QPushButton("Bed")
        self.table_button = QPushButton("Table")
        self.chair_button = QPushButton("Chair")

        self.select_button.clicked.connect(
            lambda: self.set_tool(SELECT_TOOL)
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

        layout.addWidget(self.select_button)
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
        self.canvas.current_tool = tool