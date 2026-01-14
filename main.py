import sys
import signal
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRect, QTimer



class Window(QWidget):
    def make_grid(self, width, height):
        squares = []
        size = 50
        for i in range(width):
            for j in range (height):
               squares.append(QRect(size * i, size * j, size, size))
        return squares

    def paintEvent(self, event):
        painter = QPainter(self)
        grid = self.make_grid(4, 2)

        for square in grid:
            painter.drawRect(square)
            print(square)


app = QApplication(sys.argv)
window = Window()
window.resize(400, 400)
window.show()

# Allow Ctrl-C to work by processing Python signals periodically
signal.signal(signal.SIGINT, signal.SIG_DFL)
timer = QTimer()
timer.timeout.connect(lambda: None)
timer.start(100)  # Fire every 100ms

sys.exit(app.exec())
