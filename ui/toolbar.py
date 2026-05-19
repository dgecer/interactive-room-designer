from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class ToolBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(120)

        layout = QVBoxLayout()

        self.select_button = QPushButton("Select")
        self.rectangle_button = QPushButton("Rectangle")
        self.circle_button = QPushButton("Circle")
        self.line_button = QPushButton("Line")

        layout.addWidget(self.select_button)
        layout.addWidget(self.rectangle_button)
        layout.addWidget(self.circle_button)
        layout.addWidget(self.line_button)

        layout.addStretch()

        self.setLayout(layout)