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

        self.setGeometry(400, 400, 385, 600)
        self.setWindowTitle('Настройки таймера')

        self.lblSetTime = QLabel('Настройки времени', self)
        self.lblSetTime.resize(100, 30)
        self.lblSetTime.move(132, 30)

        self.inpHours = QLineEdit(self)
        self.inpHours.resize(20, 20)
        self.inpHours.move(114, 80)

        self.lblColon1 = QLabel(':', self)
        self.lblColon1.resize(10, 15)
        self.lblColon1.move(151, 82)

        self.inpMinutes = QLineEdit(self)
        self.inpMinutes.resize(20, 20)
        self.inpMinutes.move(171, 80)

        self.lblColon2 = QLabel(':', self)
        self.lblColon2.resize(10, 15)
        self.lblColon2.move(206, 82)

        self.inpSeconds = QLineEdit(self)
        self.inpSeconds.resize(20, 20)
        self.inpSeconds.move(224, 80)

        self.col = QColor(250, 250, 250)

        sld1 = QSlider(Qt.Horizontal, self)
        sld1.setFocusPolicy(Qt.NoFocus)
        sld1.setGeometry(50, 180, 150, 20)
        sld1.valueChanged[int].connect(self.changeValueR)

        sld2 = QSlider(Qt.Horizontal, self)
        sld2.setFocusPolicy(Qt.NoFocus)
        sld2.setGeometry(50, 220, 150, 20)
        sld2.valueChanged[int].connect(self.changeValueG)

        sld3 = QSlider(Qt.Horizontal, self)
        sld3.setFocusPolicy(Qt.NoFocus)
        sld3.setGeometry(50, 260, 150, 20)
        sld3.valueChanged[int].connect(self.changeValueB)

        redlbl = QLabel('R', self)
        redlbl.resize(20, 20)
        redlbl.move(30, 178)

        greenlbl = QLabel('G', self)
        greenlbl.resize(20, 20)
        greenlbl.move(30, 218)

        bluelbl = QLabel('B', self)
        bluelbl.resize(20, 20)
        bluelbl.move(30, 258)

        self.square = QFrame(self)
        self.square.setGeometry(260, 180, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.lblSetCol = QLabel('Настройки цвета', self)
        self.lblSetCol.resize(90, 20)
        self.lblSetCol.move(140, 138)

        self.lblSetNote = QLabel('Настройки напоминания', self)
        self.lblSetNote.resize(130, 20)
        self.lblSetNote.move(122, 315)

        self.lblInstructionsNote = QLabel('Введите текст (не более 40 символов):', self)
        self.lblInstructionsNote.resize(300, 20)
        self.lblInstructionsNote.move(50, 350)

        self.inpNote = QLineEdit(self)
        self.inpNote.resize(250, 30)
        self.inpNote.move(50, 376)

        self.lblSetRingtone = QLabel('Настройки рингтона', self)
        self.lblSetRingtone.resize(120, 20)
        self.lblSetRingtone.move(130, 437)

        self.btnOk = QPushButton('OK', self)
        self.btnOk.resize(30, 30)
        self.btnOk.move(160, 520)
        self.btnOk.clicked.connect(self.OkButton)

        self.lblVerdict = QLabel(self)
        self.lblVerdict.resize(260, 40)
        self.lblVerdict.move(40, 545)
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
        self.hours = self.inpHours.text()
        self.minutes = self.inpMinutes.text()
        self.seconds = self.inpSeconds.text()
        self.note = self.inpNote.text()
        self.checkSettings()
        return self.hours, self.minutes

    def return_time_and_note(self):
        if self.verdict == 'ok':
            return self.hours, self.minutes, self.seconds, self.note
        
    def return_colour(self):
        return self.col.name()

    def checkSettings(self):
        class SettingsError(Exception):
            pass

        class NoteError(SettingsError):
            pass

        class TimeError(SettingsError):
            pass

        self.verdict = ''

        try:
            if not self.hours:
                self.hours = '0'
            if not self.minutes:
                self.minutes = '0'
            if not self.seconds:
                self.seconds = '0'
    
            if not self.hours.isdigit():
                raise TimeError('Неверный формат ввода часов. Введите число.')
            if not self.minutes.isdigit():
                raise TimeError('Неверный формат ввода минут. Введите число.')
            if not self.seconds.isdigit():
                raise TimeError('Неверный формат ввода секунд. Введите число.')

            if self.hours == '0' and self.minutes == '0' and self.seconds == '0':
                raise TimeError('Время не введено. Введите время')

            minutes = int(self.minutes)
            seconds = int(self.seconds)

            if minutes < 0:
                raise TimeError('Число минут должно быть неотрицательно.')
            if minutes > 59:
                raise TimeError('Число минут должно быть меньше 60.')
            if seconds < 0:
                raise TimeError('Число секунд должно быть неотрицательно.')
            if seconds > 59:
                raise TimeError('Число секунд должно быть меньше 60.')

            if len(self.note) > 40:
                raise NoteError('Количество символов не должно превышать 40.')

            self.verdict += 'ок'

        except TimeError as e:
            self.verdict += 'Вернитесь в настройки времени.' + '\n' + str(e)

        except NoteError as e:
            self.verdict += 'Вернитесь в настройки напоминания.' + '\n' + str(e)

        finally:
            self.lblVerdict.setText(self.verdict)
            self.lblVerdict.show()
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
