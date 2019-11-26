import random
import sys
from UI import Ui_MainWindow
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

MAX_X = MAX_Y = 400


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        size = random.randint(0, min(MAX_X, MAX_Y))
        rx, ly = random.randint(size, MAX_X), random.randint(size, MAX_Y)
        self.circles.append((QRect(QPoint(rx - size, ly - size), QPoint(rx, ly)),
                             QColor(random.randrange(256),
                                    random.randrange(256),
                                    random.randrange(256))))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        for rect, color in self.circles:
            qp.setPen(color)
            qp.drawEllipse(rect)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
