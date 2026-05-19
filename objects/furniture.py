from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QRect
from objects.base_object import BaseObject
import os

class Furniture(BaseObject):
    def __init__(self, x, y, width, height, furniture_type, vp, color="gray"):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
        self.furniture_type = furniture_type
        self.vp = vp
        self.image_path = f"assets/furniture/{furniture_type.lower()}.png"

    def draw(self, painter):
        if not self.vp: return
        
        # PERSPEKTİF HESABI: VP noktasına olan uzaklık, "uzaklık algısını" belirler
        # Mobilyanın zemine bastığı nokta (y) ile VP arasındaki farkı alıyoruz
        dist_from_vp = abs(self.y - self.vp.y())
        scale = max(0.4, min(1.2, 1.0 - (dist_from_vp / self.vp.y()) * 0.5))

        draw_w = int(self.width * scale)
        draw_h = int(self.height * scale)

        # RESİM VEYA KUTU ÇİZİMİ
        if os.path.exists(self.image_path):
            pixmap = QPixmap(self.image_path)
            
            # Perspektif Etkisi: Alt kenarı zemine tam oturtmak için y'den boyu çıkarıyoruz
            target_rect = QRect(int(self.x), int(self.y - draw_h), draw_w, draw_h)
            
            # Resmi düz bir kutu gibi değil, zemine oturan bir parça gibi çiziyoruz
            painter.drawPixmap(target_rect, pixmap)
        else:
            # Yedek kutu: Gerçekçi 3D hissi için hafif gri bir gölgeyle çizim
            painter.setPen(QPen(QColor(80, 80, 80), 1))
            painter.setBrush(QBrush(QColor(self.color)))
            painter.drawRect(int(self.x), int(self.y - draw_h), draw_w, draw_h)

        # Label: Mobilyanın üstüne profesyonel bir etiket (sadece perspektife uygun olanlar)
        painter.setPen(QColor("#7D5A5E"))
        painter.drawText(int(self.x), int(self.y - draw_h - 5), self.furniture_type.upper())