import sys
from random import sample

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        d1 = sample(range(1, 150), 1)[0]
        d2 = sample(range(1, 150), 1)[0]
        d3 = sample(range(1, 150), 1)[0]
        d4 = sample(range(1, 150), 1)[0]
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(30, 30, d1, d1)
        qp.drawEllipse(330, 250, d2, d2)
        qp.drawEllipse(70, 10, d3, d3)
        qp.drawEllipse(250, 100, d4, d4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())