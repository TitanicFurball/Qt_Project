import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from project_main_page import Ui_MainWindow
from project_page_2 import Ui_MainWindow2
from PyQt5.QtCore import QTime, QTimer

class Main_Page(QMainWindow, Ui_MainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 800, 600)
        self.hide()
        
        self.Pause.clicked.connect(self.runTime)
 
    def runTime(self):
        self.time1 = QTime(0, 0, 10)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000) 
        self.showTime()
        
    def showTime(self):
        if self.time1.hour() == 0 and self.time1.minute() == 0 and self.time1.second() == 0:
            self.timer.stop()            
        text = self.time1.toString('hh:mm:ss')
        if (self.time1.second() % 2) != 0:
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.time1 = self.time1.addSecs(-1)
        self.Time.display(text)

class First_Main_Page(QMainWindow, Ui_MainWindow2, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 800, 600)
        self.start.clicked.connect(self.DoAction)
        self.stop1.setEnabled(False)
        self.start.setEnabled(False)
        self.hours.setMaximum(23)
        self.mins.setMaximum(59)
        self.sec.setMaximum(59)
        self.hours.valueChanged.connect(self.ActivateStart)
        self.mins.valueChanged.connect(self.ActivateStart)
        self.sec.valueChanged.connect(self.ActivateStart)
            
            
    def ActivateStart(self):
        hour, minu, s = self.hours.value(), self.mins.value(), self.sec.value()
        if not (hour == 0 and minu == 0 and  s == 0): 
            self.start.setDisabled(False)
        else:
            self.start.setEnabled(False)
    
    def DoAction(self):
        self.start.setEnabled(False)
        self.hide()
        word = True
                

app = QApplication(sys.argv)
ex1 = First_Main_Page()
ex = Main_Page()
ex1.show()
ex.show()
sys.exit(app.exec_())