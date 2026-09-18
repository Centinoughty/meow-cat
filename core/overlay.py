from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtCore import Qt


class CatOverlay(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.old_pos = None
        self._setup_ui()


    def _setup_ui(self):
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.ToolTip
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.label = QLabel(self)
        og_pixmap = QPixmap(self.image_path)

        target_width = 150
        target_height = 150

        scaled_pixmap = og_pixmap.scaled(
            target_width, 
            target_height, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )

        self.label.setPixmap(scaled_pixmap)
        self.resize(scaled_pixmap.width(), scaled_pixmap.height())


    def _clamp_to_screen(self, target_x, target_y, screen):
        geom = screen.geometry() 
        
        min_x = geom.x()
        min_y = geom.y()
        max_x = min_x + geom.width() - self.width()
        max_y = min_y + geom.height() - self.height()
        
        clamped_x = max(min_x, min(target_x, max_x))
        clamped_y = max(min_y, min(target_y, max_y))
        
        return clamped_x, clamped_y


    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.old_pos = e.globalPosition().toPoint()


    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if self.old_pos != None:
            delta = e.globalPosition().toPoint() - self.old_pos

            target_x = self.x() + delta.x()
            target_y = self.y() + delta.y()

            current_screen = self.screen()
            if current_screen:
                target_x, target_y = self._clamp_to_screen(target_x, target_y, current_screen)

            self.move(target_x, target_y)
            self.old_pos = e.globalPosition().toPoint()


    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None
