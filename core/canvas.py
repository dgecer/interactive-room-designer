from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint

from objects.rectangle import Rectangle
from objects.circle import Circle
from objects.line import Line
from objects.furniture import Furniture
from objects.room import Room

from utils.constants import (
    PERSPECTIVE_TOOL, ROOM_TOOL, RECTANGLE_TOOL, CIRCLE_TOOL, 
    LINE_TOOL, SOFA_TOOL, BED_TOOL, TABLE_TOOL, CHAIR_TOOL
)

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1000, 700)
        self.objects = []
        
        self.current_tool = PERSPECTIVE_TOOL
        self.drawing = False
        self.drawing_room = False 
        
        self.start_x = 0
        self.start_y = 0
        self.current_shape = None

        self.room = Room(self.width(), self.height(), QPoint(self.width() // 2, self.height() // 2))
        self.selected_vp = False

    def set_tool(self, tool):
        self.current_tool = tool
        self.selected_vp = False
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.white)

        # Ufuk Çizgisi (Horizon Line)
        painter.setPen(QPen(Qt.gray, 1, Qt.DashLine))
        painter.drawLine(0, self.room.vp.y(), self.width(), self.room.vp.y())

        # Odayı ve Gridleri Çiz
        self.room.draw(painter, self.width(), self.height())

        for obj in self.objects:
            obj.draw(painter)

        if self.current_shape:
            self.current_shape.draw(painter)

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()

        # VP Taşıma
        if self.current_tool == PERSPECTIVE_TOOL:
            distance = ((x - self.room.vp.x()) ** 2 + (y - self.room.vp.y()) ** 2) ** 0.5
            if distance < 15:
                self.selected_vp = True
            return

        # ODA (KARŞI DUVAR) ÇİZİMİ BAŞLANGICI
        if self.current_tool == ROOM_TOOL:
            self.drawing_room = True
            self.start_x = x
            self.start_y = y
            return

        # 2D Şekiller ve Mobilyalar
        if self.current_tool == RECTANGLE_TOOL:
            self.drawing = True
            self.start_x, self.start_y = x, y
            self.current_shape = Rectangle(x, y, 0, 0)
        elif self.current_tool == CIRCLE_TOOL:
            self.drawing = True
            self.start_x, self.start_y = x, y
            self.current_shape = Circle(x, y, 0)
        elif self.current_tool == LINE_TOOL:
            self.drawing = True
            self.start_x, self.start_y = x, y
            self.current_shape = Line(x, y, x, y)
        elif self.current_tool == SOFA_TOOL:
            self.objects.append(Furniture(x, y, 160, 90, "Sofa", self.room.vp, "#7D8ABC"))
            self.update()
        elif self.current_tool == BED_TOOL:
            self.objects.append(Furniture(x, y, 180, 110, "Bed", self.room.vp, "#C499BA"))
            self.update()
        elif self.current_tool == TABLE_TOOL:
            self.objects.append(Furniture(x, y, 100, 100, "Table", self.room.vp, "#A67B5B"))
            self.update()
        elif self.current_tool == CHAIR_TOOL:
            self.objects.append(Furniture(x, y, 70, 70, "Chair", self.room.vp, "#909090"))
            self.update()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        # VP Sürükleme
        if self.selected_vp and self.current_tool == PERSPECTIVE_TOOL:
            self.room.vp.setX(x)
            self.room.vp.setY(y)
            self.update()
            return

        # ODA (KARŞI DUVAR) SERBEST ÇİZİMİ
        if self.current_tool == ROOM_TOOL and self.drawing_room:
            self.room.bw_x = min(x, self.start_x)
            self.room.bw_y = min(y, self.start_y)
            self.room.bw_w = abs(x - self.start_x)
            self.room.bw_h = abs(y - self.start_y)
            self.update()
            return

        if not self.drawing or not self.current_shape:
            return

        # 2D Şekil Çizimi Güncellemesi
        if self.current_tool == RECTANGLE_TOOL:
            self.current_shape.width = x - self.start_x
            self.current_shape.height = y - self.start_y
        elif self.current_tool == CIRCLE_TOOL:
            self.current_shape.radius = max(abs(x - self.start_x), abs(y - self.start_y)) // 2
        elif self.current_tool == LINE_TOOL:
            self.current_shape.x2 = x
            self.current_shape.y2 = y

        self.update()

    def mouseReleaseEvent(self, event):
        self.selected_vp = False
        
        # Oda çizimini bitirme
        if self.drawing_room:
            self.drawing_room = False
            self.update()
            return

        # 2D Şekil Çizimini bitirme ve listeye ekleme
        if self.drawing and self.current_shape:
            self.objects.append(self.current_shape)
            self.current_shape = None
            self.drawing = False
            self.update()