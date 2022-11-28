import sys

import keyboard

from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QCursor, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu


class KeyBoardManager(QObject):
    F1Signal = pyqtSignal()

    def start(self):
        keyboard.add_hotkey("F1", self.F1Signal.emit, suppress=True)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        manager = KeyBoardManager(self)
        manager.F1Signal.connect(self.focus)
        manager.start()

    def focus(self):
        self.setWindowState(self.windowState() & ~Qt.WindowState.WindowMinimized | Qt.WindowState.WindowActive)
        self.show()
        self.activateWindow()
        self.raise_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())