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
        self.Pause.clicked.connect(self.run)
 
    def run(self):
        self.showTime()        
        
    def showTime(self):
        try:
            '''time1 = QTime(0, 0, 2)
            text = ''
            while text!='00:00:00':
                text = time1.toString('hh:mm:ss')
                if (time1.second() % 2) != 0:
                    text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
                print(text)
                self.Time.display(text)
                time1.addSecs(-1)
                time.sleep(1)'''
            time1 = '00:02'
            if len(time1) == 2:
                time1 = '00:00:' + time1
            elif len(time1) == 5:
                time1 = '00:' + time1
            time_sec = time1.split(':')
            seconds = 0
            for i in range(3):
                if time_sec[i][0] == '0':
                    time_sec[i] = time_sec[i][1]
                time_sec[i] = int(time_sec[i])
            seconds = time_sec[0] * 3600 + time_sec[1] * 60 + time_sec[2]
            
            for i in range(seconds, -1, -1):
                print(i)
                h = i//3600
                h1 = str(h)
                m = str((i-h*3600)//60)
                m1 = str(m)
                sec = i%60
                sec1 = str(sec)
                if len(h1) != 2:
                    h1 = '0' + h1
                if len(m1) != 2:
                    m1 = '0' + m1     
                if len(sec1) != 2:
                    sec1 = '0' + sec1
                time1 = h1 + ':' + m1 + ':' + sec1
                if int(sec) % 2 == 1:
                    time1 = time1.replace(':', ' ')
                print(time1)
                self.Time.display(time1)
                
        except Exception as e:
            print(e)
               
 
 
app = QApplication(sys.argv)
ex = Main_Page()
ex.show()
sys.exit(app.exec_())