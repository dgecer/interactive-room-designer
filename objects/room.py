from PyQt5.QtGui import QColor, QBrush, QPen, QPolygon
from PyQt5.QtCore import QPoint, Qt

class Room:
    def __init__(self, width, height, vanishing_point):
        self.vp = vanishing_point
        
        # Karşı Duvarın (Back Wall) varsayılan koordinatları
        self.bw_w = 300
        self.bw_h = 200
        self.bw_x = (width - self.bw_w) / 2
        self.bw_y = (height - self.bw_h) / 2
        
        self.num_cols = 10 

    def draw(self, painter, canvas_width, canvas_height):
        # 1. KARŞI DUVAR (BACK WALL)
        painter.setPen(QPen(QColor(50, 50, 50), 3))
        painter.setBrush(QBrush(QColor(240, 240, 245)))
        painter.drawRect(int(self.bw_x), int(self.bw_y), int(self.bw_w), int(self.bw_h))

        # 2. PERSPEKTİF IŞINLARI (RAYS)
        painter.setPen(QPen(QColor(160, 160, 160), 1))
        X_points = [self.bw_x + i * (self.bw_w / self.num_cols) for i in range(self.num_cols + 1)]
        Y_points = [self.bw_y + i * (self.bw_h / self.num_cols) for i in range(self.num_cols + 1)]

        def draw_ray(px, py):
            dx = px - self.vp.x()
            dy = py - self.vp.y()
            if dx == 0 and dy == 0: return
            scale = 50 
            painter.drawLine(self.vp.x(), self.vp.y(), int(self.vp.x() + dx * scale), int(self.vp.y() + dy * scale))

        for x in X_points:
            draw_ray(x, self.bw_y)
            draw_ray(x, self.bw_y + self.bw_h)

        for y in Y_points:
            draw_ray(self.bw_x, y)
            draw_ray(self.bw_x + self.bw_w, y)

        # 3. DİNAMİK DERİNLİK IZGARALARI (Uzaklığa göre artan/azalan gridler)
        painter.setBrush(Qt.NoBrush)
        i = 1
        while True:
            factor = 1.35 ** i 

            x1 = self.vp.x() + (self.bw_x - self.vp.x()) * factor
            y1 = self.vp.y() + (self.bw_y - self.vp.y()) * factor
            x2 = self.vp.x() + (self.bw_x + self.bw_w - self.vp.x()) * factor
            y2 = self.vp.y() + (self.bw_y - self.vp.y()) * factor
            x3 = self.vp.x() + (self.bw_x + self.bw_w - self.vp.x()) * factor
            y3 = self.vp.y() + (self.bw_y + self.bw_h - self.vp.y()) * factor
            x4 = self.vp.x() + (self.bw_x - self.vp.x()) * factor
            y4 = self.vp.y() + (self.bw_y + self.bw_h - self.vp.y()) * factor

            # Çizilen poligon ekranı tamamen aştıysa döngüyü durdur (Performans koruması)
            if (x2 - x1) > canvas_width * 3 or (y4 - y1) > canvas_height * 3:
                break

            painter.drawPolygon(QPolygon([
                QPoint(int(x1), int(y1)), QPoint(int(x2), int(y2)),
                QPoint(int(x3), int(y3)), QPoint(int(x4), int(y4))
            ]))
            i += 1

        # 4. VP NOKTASI
        painter.setBrush(QBrush(QColor(255, 80, 80)))
        painter.setPen(QPen(QColor(180, 0, 0), 2))
        painter.drawEllipse(self.vp.x() - 8, self.vp.y() - 8, 16, 16)