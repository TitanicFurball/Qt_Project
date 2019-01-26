import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from project_main_page import Ui_MainWindow
import time
from PyQt5.QtCore import QTime, QTimer


class Main_Page(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 800, 600)
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
            

app = QApplication(sys.argv)
ex = Main_Page()
ex.show()
sys.exit(app.exec_())
