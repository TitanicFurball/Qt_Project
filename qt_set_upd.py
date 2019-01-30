import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel,
                             QApplication, QFrame, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setGeometry(400, 400, 385, 400)
        self.setWindowTitle('Настройки таймера')

        self.col = QColor(250, 250, 250)

        sld1 = QSlider(Qt.Horizontal, self)
        sld1.setFocusPolicy(Qt.NoFocus)
        sld1.setGeometry(50, 80, 150, 20)
        sld1.valueChanged[int].connect(self.changeValueR)

        sld2 = QSlider(Qt.Horizontal, self)
        sld2.setFocusPolicy(Qt.NoFocus)
        sld2.setGeometry(50, 120, 150, 20)
        sld2.valueChanged[int].connect(self.changeValueG)

        sld3 = QSlider(Qt.Horizontal, self)
        sld3.setFocusPolicy(Qt.NoFocus)
        sld3.setGeometry(50, 160, 150, 20)
        sld3.valueChanged[int].connect(self.changeValueB)

        redlbl = QLabel('R', self)
        redlbl.resize(20, 20)
        redlbl.move(30, 78)

        greenlbl = QLabel('G', self)
        greenlbl.resize(20, 20)
        greenlbl.move(30, 118)

        bluelbl = QLabel('B', self)
        bluelbl.resize(20, 20)
        bluelbl.move(30, 158)

        self.square = QFrame(self)
        self.square.setGeometry(260, 80, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.lblSetCol = QLabel('Настройки цвета', self)
        self.lblSetCol.resize(90, 20)
        self.lblSetCol.move(140, 38)

        self.lblSetNote = QLabel('Настройки напоминания', self)
        self.lblSetNote.resize(130, 20)
        self.lblSetNote.move(122, 215)

        self.lblInstructionsNote = QLabel('Введите текст (не более 40 символов):', self)
        self.lblInstructionsNote.resize(300, 20)
        self.lblInstructionsNote.move(50, 250)

        self.inpNote = QLineEdit(self)
        self.inpNote.resize(250, 30)
        self.inpNote.move(50, 276)

        self.btnOk = QPushButton('OK', self)
        self.btnOk.resize(30, 30)
        self.btnOk.move(160, 360)
        self.btnOk.clicked.connect(self.OkButton)

        self.lblVerdict = QLabel(self)
        self.lblVerdict.resize(260, 40)
        self.lblVerdict.move(40, 445)
        self.lblVerdict.show()

        self.show()

    def changeValueR(self, value):
        self.col.setRed(250 - value)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())
        self.show()
        
    def changeValueG(self, value):
        self.col.setGreen(250 - value)
        self.square.setStyleSheet("QFrame { background-color: %s }" %

                                  self.col.name())
        self.show()

    def changeValueB(self, value):
        self.col.setBlue(250 - value)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())
        self.show()

    def OkButton(self):
        self.note = self.inpNote.text()
        self.checkSettings()
        print(self.verdict)
        print(self.col)
        print(self.note)
        return self.col, self.note

    def checkSettings(self):
        class SettingsError(Exception):
            pass

        class NoteError(SettingsError):
            pass
        
        self.verdict = ''

        try:
            if len(self.note) > 40:
                raise NoteError('Количество символов не должно превышать 40.')
            self.verdict += 'ок'

        except NoteError as e:
            self.verdict += 'Вернитесь в настройки напоминания.' + ' ' + str(e)

        finally:
            self.lblVerdict.setText(self.verdict)
            self.lblVerdict.show()            


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
