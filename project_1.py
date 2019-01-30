import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from project_main_page import Ui_MainWindow
from project_page_2 import Ui_MainWindow2
from PyQt5.QtCore import QTime, QTimer
from project_page_3 import Ui_MainWindow3
from pygame import mixer


class Main_Page(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, a, b, c, window): 
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.window = window
        #self.mel = Melody_Page()
        self.play_check = False 
        self.setupUi(self)
        self.setGeometry(300, 100, 800, 600)        
        self.current_timer = QTimer(self)
        self.current_timer.setSingleShot(True)
        self.current_timer.timeout.connect(self.runTime)
        self.current_timer.start(100)
        self.Pause.clicked.connect(self.pauseTime)
        self.Stop.clicked.connect(self.stopTime)
        self.Melody.clicked.connect(self.open_mel_win)
 
    def runTime(self):
        self.time1 = QTime(self.a, self.b, self.c, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000) 
        self.showTime()
        
    def showTime(self):
        if self.time1.hour() == 0 and self.time1.minute() == 0 and self.time1.second() == 0:
            self.timer.stop()
            self.Melody.setEnabled(False)
            self.Pause.setEnabled(False)
            mixer.init()
            mixer.music.load(self.window.mel.ringtone)
            self.play_check = True
            mixer.music.play(-1)
        text = self.time1.toString('hh:mm:ss')
        if (self.time1.second() % 2) != 0:
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.time1 = self.time1.addSecs(-1)
        self.Time.display(text)
    
    def pauseTime(self):
        if self.timer.isActive():
            self.timer.stop()
            self.Pause.setText('Дальше')
        else:
            self.Pause.setText('Пауза')
            milisec_timer = QTimer(self)
            milisec_timer.setSingleShot(True)
            self.a = self.time1.hour()
            self.b = self.time1.minute()
            self.c = self.time1.second()
            milisec_timer.start(500)
            milisec_timer.timeout.connect(self.runTime)
    
    def stopTime(self):
        if self.play_check:
            mixer.music.stop()
        self.timer.stop()
        self.Pause.setDisabled(False)
        self.Melody.setDisabled(False)
        self.current_timer.stop()
        self.hide()
        self.window.show()
    
    def open_mel_win(self):
        self.window.mel.show()
                   

class First_Main_Page(QMainWindow, Ui_MainWindow2, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 800, 600)
        self.mel = Melody_Page()
        self.start.clicked.connect(self.DoAction)
        self.stop1.setEnabled(False)
        self.start.setEnabled(False)
        self.hours.setMaximum(23)
        self.mins.setMaximum(59)
        self.sec.setMaximum(59)
        self.hours.valueChanged.connect(self.ActivateStart)
        self.mins.valueChanged.connect(self.ActivateStart)
        self.sec.valueChanged.connect(self.ActivateStart)
        self.Melody1.clicked.connect(self.open_mel_win)
        
    def ActivateStart(self):
        self.hour, self.minu, self.s = self.hours.value(), self.mins.value(), self.sec.value()
        if not (self.hour in [0, ''] and self.minu in [0, ''] and  self.s in [0, '']): 
            self.start.setDisabled(False)
        else:
            self.start.setEnabled(False)
    
    def DoAction(self):
        self.hide()
        self.ex = Main_Page(self.hour, self.minu, self.s, self)
        self.ex.show()
    
    def open_mel_win(self):
        self.mel.show() 


class Melody_Page(QMainWindow, Ui_MainWindow3, QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(1100, 69)
        self.melody = "Dreams.mp3"
        self.ringtone = "Dreams.mp3"
        self.Button1.setChecked(True)
        self.Button1.clicked.connect(self.play1)
        self.Button2.clicked.connect(self.play1)
        self.Button3.clicked.connect(self.play1)
        self.Button4.clicked.connect(self.play1)
        self.Button5.clicked.connect(self.play1)
        self.setButton.clicked.connect(self.set_melody)
        self.CancelButton.clicked.connect(self.cancel_melody)      
    
    def play1(self):
        if self.Button1.isChecked():
            self.melody = "Alarm clock.mp3"
        elif self.Button2.isChecked():
            self.melody = "Dreams.mp3"
        elif self.Button3.isChecked():
            self.melody = "Sunny.mp3"
        elif self.Button4.isChecked():
            self.melody = "Fantasy.mp3"
        elif self.Button5.isChecked():
            self.melody = "Calm.mp3"         
        self.play = (True, self.melody)
        mixer.init()
        mixer.music.load(self.melody)
        mixer.music.play()

    def set_melody(self):
        self.ringtone = self.melody

    def cancel_melody(self):
        mixer.music.stop()
        self.hide()
        

app = QApplication(sys.argv)
ex1 = First_Main_Page()
ex1.show()
sys.exit(app.exec_())