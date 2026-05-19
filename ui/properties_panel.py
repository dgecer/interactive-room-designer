from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class PropertiesPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(200)

        layout = QVBoxLayout()

        title = QLabel("Properties Panel")

        layout.addWidget(title)
        layout.addStretch()

        self.setLayout(layout)