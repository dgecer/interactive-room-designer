from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from core.canvas import Canvas
from ui.toolbar import ToolBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Lunara Interior Designer"
        )

        self.resize(1600, 900)

        self.init_ui()

        # GLOBAL STYLE

        self.setStyleSheet("""

            QMainWindow {
                background-color: #FDF8F8;
            }

            QWidget {
                background-color: #FDF8F8;
                color: #4A3B3B;
                font-family: Segoe UI;
                font-size: 13px;
            }

            QPushButton {

                background-color: #E8CFCF;

                border: 2px solid #D4AF37;

                border-radius: 14px;

                padding: 10px;

                color: #4A3B3B;

                font-weight: bold;
            }

            QPushButton:hover {

                background-color: #F2DCDC;

                border: 2px solid #C89B2D;
            }

            QPushButton:pressed {

                background-color: #D9B6B6;
            }

        """)

    def init_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        layout = QHBoxLayout()

        self.canvas = Canvas()

        self.toolbar = ToolBar(
            self.canvas
        )

        layout.addWidget(
            self.toolbar
        )

        layout.addWidget(
            self.canvas
        )

        central_widget.setLayout(
            layout
        )