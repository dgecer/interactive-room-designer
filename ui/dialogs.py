from PyQt5.QtWidgets import QInputDialog


class PerspectiveDialog:

    @staticmethod
    def choose_perspective(parent):

        items = [
            "1-Point Perspective",
            "2-Point Perspective",
            "3-Point Perspective"
        ]

        choice, ok = QInputDialog.getItem(
            parent,
            "Perspective Selection",
            "Choose Perspective Type:",
            items,
            0,
            False
        )

        if not ok:
            return None

        if choice == "1-Point Perspective":
            return "1-point"

        if choice == "2-Point Perspective":
            return "2-point"

        return "3-point"