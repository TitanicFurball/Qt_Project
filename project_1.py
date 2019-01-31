import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QSlider, 
                             QLabel, QFrame, QLineEdit, QPushButton, QLCDNumber, 
                             QSpinBox, QRadioButton, QMenuBar, QStatusBar)
from PyQt5.QtCore import QTime, QTimer, Qt, QRect, QMetaObject, QCoreApplication
from pygame import mixer
from PyQt5.QtGui import QColor, QFont

#Окно Обратного Отсчёта - дизайн

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Time = QLCDNumber(self.centralwidget)
        self.Time.setGeometry(QRect(260, 80, 271, 121))
        self.Time.setFrameShape(QFrame.Box)
        self.Time.setFrameShadow(QFrame.Sunken)
        self.Time.setLineWidth(1)
        self.Time.setMidLineWidth(0)
        self.Time.setSmallDecimalPoint(False)
        self.Time.setDigitCount(8)
        self.Time.setObjectName("lcdNumber")
        
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(220, 0, 341, 61))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(0, 40, 831, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QRect(0, 220, 801, 31))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.Melody = QPushButton(self.centralwidget)
        self.Melody.setGeometry(QRect(-270, 240, 1091, 61))
        self.Melody.setObjectName("pushButton")
        
        self.Pause = QPushButton(self.centralwidget)
        self.Pause.setGeometry(QRect(520, 370, 81, 81))
        self.Pause.setDefault(True)
        self.Pause.setFlat(False)
        self.Pause.setObjectName("pushButton_2")
        
        self.Stop = QPushButton(self.centralwidget)
        self.Stop.setGeometry(QRect(190, 370, 81, 81))
        self.Stop.setDefault(True)
        self.Stop.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Таймер"))
        self.Melody.setText(_translate("MainWindow", "Рингтон"))
        self.Pause.setText(_translate("MainWindow", "Пауза"))
        self.Stop.setText(_translate("MainWindow", "Отмена"))
        
#Окно Установки Времени - дизайн

class Ui_MainWindow2(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(220, 0, 341, 61))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(0, 40, 831, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QRect(0, 220, 801, 31))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.Melody1 = QPushButton(self.centralwidget)
        self.Melody1.setGeometry(QRect(-270, 240, 1091, 61))
        self.Melody1.setObjectName("pushButton")
        
        self.start = QPushButton(self.centralwidget)
        self.start.setGeometry(QRect(520, 370, 81, 81))
        self.start.setDefault(True)
        self.start.setFlat(False)
        self.start.setObjectName("pushButton_2")
        
        self.stop1 = QPushButton(self.centralwidget)
        self.stop1.setGeometry(QRect(190, 370, 81, 81))
        self.stop1.setCheckable(False)
        self.stop1.setAutoExclusive(True)
        self.stop1.setDefault(True)
        self.stop1.setObjectName("pushButton_3")
        
        self.hours = QSpinBox(self.centralwidget)
        self.hours.setGeometry(QRect(150, 120, 71, 31))
        self.hours.setObjectName("spinBox")
        self.mins = QSpinBox(self.centralwidget)
        self.mins.setGeometry(QRect(350, 120, 71, 31))
        self.mins.setObjectName("spinBox_2")
        self.sec = QSpinBox(self.centralwidget)
        self.sec.setGeometry(QRect(550, 120, 71, 31))
        self.sec.setObjectName("spinBox_3")
        
        self.label_h = QLabel(self.centralwidget)
        self.label_h.setGeometry(QRect(240, 130, 41, 16))
        self.label_h.setTextFormat(Qt.AutoText)
        self.label_h.setObjectName("label_3")
        self.label_m = QLabel(self.centralwidget)
        self.label_m.setGeometry(QRect(440, 130, 41, 16))
        self.label_m.setTextFormat(Qt.AutoText)
        self.label_m.setObjectName("label_4")
        self.label_s = QLabel(self.centralwidget)
        self.label_s.setGeometry(QRect(640, 130, 41, 16))
        self.label_s.setTextFormat(Qt.AutoText)
        self.label_s.setObjectName("label_5")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.setngsButton = QPushButton(self.centralwidget)
        self.setngsButton.resize(100, 25)
        self.setngsButton.move(600, 20)
        self.setngsButton.setText("Доп. Настройки")

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Таймер"))
        self.Melody1.setText(_translate("MainWindow", "Рингтон"))
        self.start.setText(_translate("MainWindow", "Старт"))
        self.stop1.setText(_translate("MainWindow", "Отмена"))
        self.label_h.setText(_translate("MainWindow", "Ч"))
        self.label_m.setText(_translate("MainWindow", "МИН"))
        self.label_s.setText(_translate("MainWindow", "С"))
        
#Окно Выбор Рингтона - дизайн

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Button1 = QRadioButton(self.centralwidget)
        self.Button1.setGeometry(QRect(20, 110, 291, 41))
        self.Button1.setObjectName("Button1")

        self.Button2 = QRadioButton(self.centralwidget)
        self.Button2.setGeometry(QRect(20, 70, 291, 41))
        self.Button2.setObjectName("Button2")
        
        self.Button3 = QRadioButton(self.centralwidget)
        self.Button3.setGeometry(QRect(20, 150, 291, 41))
        self.Button3.setObjectName("Button3")
        
        self.Button4 = QRadioButton(self.centralwidget)
        self.Button4.setGeometry(QRect(20, 190, 291, 41))
        self.Button4.setObjectName("Button4")
        
        self.Button5 = QRadioButton(self.centralwidget)
        self.Button5.setGeometry(QRect(20, 230, 291, 41))
        self.Button5.setObjectName("Button5")
        
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(90, 20, 81, 21))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.setButton = QPushButton(self.centralwidget)
        self.setButton.setGeometry(QRect(170, 20, 75, 23))
        self.setButton.setObjectName("setButton")
        
        self.CancelButton = QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QRect(20, 20, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(-10, 50, 311, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 283, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", 
                                        "  Alarm clock_________________"))
        self.Button2.setText(_translate("MainWindow", 
                                        "  Dreams____________________"))
        self.Button3.setText(_translate("MainWindow",
                                        "  Sunny_____________________"))
        self.Button4.setText(_translate("MainWindow", 
                                        "  Fantasy____________________"))
        self.Button5.setText(_translate("MainWindow",
                                        "  Ambient____________________"))
        self.label.setText(_translate("MainWindow",
                                      "Рингтон"))
        self.setButton.setText(_translate("MainWindow", "Установить"))
        self.CancelButton.setText(_translate("MainWindow", "Отменить"))
        
#Окно Обратного Отсчёта - код

class Main_Page(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, h, m, s, window): 
        super().__init__()
        self.setWindowTitle('Таймер')
        
        with open("changes.txt", "rt", encoding="utf8") as f:
            text = f.read().split(';')
        color = text[0].replace('(', '').replace(')', '')
        self.note = text[1]
        color = [int(i) for i in color.split(', ')]
        current_color = QColor(color[0], color[1], color[2], color[3])
        self.setStyleSheet("QMainWindow { background-color: %s }" % 
                                  current_color.name())
        
        self.h = h
        self.m = m
        self.s = s
        self.window = window
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
        self.t1 = QTime(self.h, self.m, self.s, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000) 
        self.showTime()
        
    def showTime(self):
        if [self.t1.hour(), self.t1.minute(), self.t1.second()] == [0, 0, 0]:
            self.timer.stop()
            self.Melody.setEnabled(False)
            if self.note != '':
                self.Melody.setText(self.note)
            self.Pause.setEnabled(False)
            mixer.init()
            mixer.music.load(self.window.mel.ringtone)
            self.play_check = True
            mixer.music.play(-1)
        text = self.t1.toString('hh:mm:ss')
        if (self.t1.second() % 2) != 0:
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.t1 = self.t1.addSecs(-1)
        self.Time.display(text)
    
    def pauseTime(self):
        if self.timer.isActive():
            self.timer.stop()
            self.Pause.setText('Дальше')
        else:
            self.Pause.setText('Пауза')
            milisec_timer = QTimer(self)
            milisec_timer.setSingleShot(True)
            self.h = self.t1.hour()
            self.m = self.t1.minute()
            self.s = self.t1.second()
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
                   
#Меню - Установка времени - код

class First_Main_Page(QMainWindow, Ui_MainWindow2, QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Установка времени')
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
        self.setngsButton.clicked.connect(self.open_settings)
        
    def ActivateStart(self):
        self.h, self.m, self.s = (self.hours.value(), self.mins.value(), 
                                        self.sec.value())
        if not (self.h in [0, ''] and self.m in [0, ''] and  self.s in [0, '']): 
            self.start.setDisabled(False)
        else:
            self.start.setEnabled(False)
    
    def DoAction(self):
        self.hide()
        self.ex = Main_Page(self.h, self.m, self.s, self)
        self.ex.show()
    
    def open_mel_win(self):
        self.mel.show() 
    
    def open_settings(self):
        self.hide()
        self.sttngs = Settings()
        self.sttngs.show()

#Окно Выбора Рингтона - код

class Melody_Page(QMainWindow, Ui_MainWindow3, QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Рингтон')
        self.setupUi(self)
        self.move(1100, 69)
        self.melody = "Dreams.mp3"
        self.ringtone = "Dreams.mp3"
        self.Button2.setChecked(True)
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

# Окно Дополнительных Настроек

class Settings(QWidget):
    
    def __init__(self):
        super().__init__() 
        self.initUI()
 
    def initUI(self):
        self.setGeometry(550, 250, 385, 450)
        self.setWindowTitle('Настройки таймера')
        
        with open("changes.txt", "rt", encoding="utf8") as f:
            text = f.read().split(';')
        color = text[0].replace('(', '').replace(')', '')
        self.note = text[1]
        col = [int(i) for i in color.split(', ')]
        
        self.col = QColor(col[0], col[1], col[2], col[3])
        
        self.sld1 = QSlider(Qt.Horizontal, self)
        self.sld1.setFocusPolicy(Qt.NoFocus)
        self.sld1.setGeometry(50, 80, 150, 20)
        self.sld1.setTracking(True)
        self.sld1.setSliderPosition(250 - col[0])
        self.sld1.valueChanged[int].connect(self.changeValueR)
        
        self.sld2 = QSlider(Qt.Horizontal, self)
        self.sld2.setFocusPolicy(Qt.NoFocus)
        self.sld2.setGeometry(50, 120, 150, 20)
        self.sld2.setTracking(True)
        self.sld2.setSliderPosition(250 - col[1])
        self.sld2.valueChanged[int].connect(self.changeValueG)
        
        self.sld3 = QSlider(Qt.Horizontal, self)
        self.sld3.setFocusPolicy(Qt.NoFocus)
        self.sld3.setGeometry(50, 160, 150, 20)
        self.sld3.setTracking(True)
        self.sld3.setSliderPosition(250 - col[2])
        self.sld3.valueChanged[int].connect(self.changeValueB)
        
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
        self.lblSetCol = QLabel('Настройки цвета \n(Чтобы принять изменения,' + 
                                '\n нажмите Enter в поле для заметки)', self)
        self.lblSetCol.setAlignment(Qt.AlignCenter)
        self.lblSetCol.resize(200, 40)
        self.lblSetCol.move(80, 15)
        self.lblSetNote = QLabel('Настройки напоминания \n' + 
                                 '(Изменения принимаются при' + 
                                 'нажатии Enter в поле)', self)
        self.lblSetNote.setAlignment(Qt.AlignCenter)
        self.lblSetNote.resize(300, 40)
        self.lblSetNote.move(40, 200)
        self.lblInstrNote = QLabel('Введите текст (не более 40 символов):',
                                   self)
        self.lblInstrNote.resize(300, 20)
        self.lblInstrNote.move(50, 250)
        
        self.inpNote = QLineEdit(self)
        self.inpNote.resize(250, 30)
        self.inpNote.move(50, 276)
        self.inpNote.returnPressed.connect(self.OkAction)
        
        self.btnOk = QPushButton('OK', self)
        self.btnOk.resize(30, 30)
        self.btnOk.setEnabled(False)
        self.btnOk.move(160, 400)
        self.btnOk.clicked.connect(self.Confirm_changes)
        
        self.lblVerdict = QLabel(self)
        self.lblVerdict.resize(260, 40)
        self.lblVerdict.setAlignment(Qt.AlignCenter)
        self.lblVerdict.move(55, 335)
        self.lblVerdict.show() 
        self.show()
        
        self.first_page = First_Main_Page()

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

    def OkAction(self):
        self.note = self.inpNote.text()
        self.checkSettings()
    
    def checkSettings(self):
        
        class SettingsError(Exception):
            pass


        class NoteError(SettingsError):
            pass

        self.verdict = ''
        try:
            if len(self.note) > 40:
                msg = 'Количество символов не должно превышать 40.'
                msg += '\nВведите текст заново.'
                raise NoteError(msg)
            self.verdict = 'Изменения приняты.'
            self.btnOk.setDisabled(False)
        except NoteError as e:
            self.verdict = '\n' + str(e)
            self.btnOk.setEnabled(False)
        finally:
            self.lblVerdict.setText(self.verdict) 
            self.lblVerdict.show()
    
    def Confirm_changes(self):
        try:
            col = self.col.getRgb()
            with open("changes.txt", "wt", encoding="utf8") as f:
                f.write(str(col) + ';' + self.note)
            current_color = QColor(col[0], col[1], col[2], col[3])
            self.hide()
            self.first_page.setStyleSheet("QMainWindow { background-color: %s }"
                                          % current_color.name())           
            self.first_page.show()
        except Exception as e:
            print(e)
        

app = QApplication(sys.argv)
ex = Settings()
ex.show()
sys.exit(app.exec_())