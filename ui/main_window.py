from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
)

from core.canvas import Canvas
from ui.toolbar import ToolBar
from ui.properties_panel import PropertiesPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interactive Room Design Tool")
        self.setGeometry(100, 100, 1200, 800)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        self.toolbar = ToolBar()
        self.canvas = Canvas()
        self.properties_panel = PropertiesPanel()

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas, stretch=1)
        layout.addWidget(self.properties_panel)

        central_widget.setLayout(layout)