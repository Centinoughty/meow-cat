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
        pixmap = QPixmap(self.image_path)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())


    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.old_pos = e.globalPosition().toPoint()


    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if self.old_pos != None:
            delta = e.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = e.globalPosition().toPoint()


    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None
