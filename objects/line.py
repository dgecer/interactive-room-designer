from PyQt5.QtGui import QColor, QPen, QBrush, QPolygon
from PyQt5.QtCore import QPoint
from objects.base_object import BaseObject

class Line(BaseObject):
    def __init__(self, x1, y1, x2, y2, vp, color="#2ECC71"):
        super().__init__(x1, y1, color)
        self.x2, self.y2 = x2, y2
        self.vp = vp

    def draw(self, painter):
        if not self.vp: return
        dist_to_vp = ((self.x - self.vp.x())**2 + (self.y - self.vp.y())**2)**0.5
        depth = max(0.05, min(0.15, 200 / (dist_to_vp + 200)))
        
        x1_b = int(self.vp.x() + (self.x - self.vp.x()) * depth)
        y1_b = int(self.vp.y() + (self.y - self.vp.y()) * depth)
        x2_b = int(self.vp.x() + (self.x2 - self.vp.x()) * depth)
        y2_b = int(self.vp.y() + (self.y2 - self.vp.y()) * depth)

        painter.setPen(QPen(QColor(30, 30, 30), 2))
        painter.setBrush(QBrush(QColor(self.color).darker(110)))
        painter.drawPolygon(QPolygon([QPoint(self.x, self.y), QPoint(self.x2, self.y2), 
                                      QPoint(x2_b, y2_b), QPoint(x1_b, y1_b)]))