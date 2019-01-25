import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.col = QColor(0, 0, 0)

        sld1 = QSlider(Qt.Horizontal, self)
        sld1.setFocusPolicy(Qt.NoFocus)
        sld1.setGeometry(30, 40, 100, 20)
        sld1.valueChanged[int].connect(self.changeValueR)

        sld2 = QSlider(Qt.Horizontal, self)
        sld2.setFocusPolicy(Qt.NoFocus)
        sld2.setGeometry(30, 80, 100, 20)
        sld2.valueChanged[int].connect(self.changeValueG)

        sld3 = QSlider(Qt.Horizontal, self)
        sld3.setFocusPolicy(Qt.NoFocus)
        sld3.setGeometry(30, 120, 100, 20)
        sld3.valueChanged[int].connect(self.changeValueB)

        redb = QLabel('R', self)
        redb.resize(20, 20)
        redb.move(10, 40)

        greenb = QLabel('G', self)
        greenb.resize(20, 20)
        greenb.move(10, 80)

        blueb = QLabel('B', self)
        blueb.resize(20, 20)
        blueb.move(10, 120)

        self.square = QFrame(self)
        self.square.setGeometry(250, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValueR(self, value):
        self.col.setRed(value * 2.55)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
        self.show()

    def changeValueG(self, value):
        self.col.setGreen(value * 2.55)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
        self.show()

    def changeValueB(self, value):
        self.col.setBlue(value * 2.55)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
