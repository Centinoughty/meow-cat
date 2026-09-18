import os
import signal
import sys
from PyQt6.QtWidgets import QApplication
from config import ASSET_PATH
from core.overlay import CatOverlay


def _configure_linux_window_backend():
    if (
        sys.platform.startswith("linux")
        and os.environ.get("XDG_SESSION_TYPE") == "wayland"
        and os.environ.get("DISPLAY")
    ):
        os.environ.setdefault("QT_QPA_PLATFORM", "xcb")


def main():
    _configure_linux_window_backend()

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)

    overlay = CatOverlay(ASSET_PATH)

    overlay.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    