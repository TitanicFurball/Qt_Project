from PyQt5 import QtCore, QtGui, QtWidgets
import pygame

class Ui_MainWindow3(object):
    def __init__(self):
        self.melody = "media/Alarm clock.mp3"
        self.play = (False, "media/Alarm clock.mp3")
        self.setupUi()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(20, 110, 291, 41))
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(20, 70, 291, 41))
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(20, 150, 291, 41))
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(20, 190, 291, 41))
        self.Button4.setObjectName("Button4")
        self.Button5 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(20, 230, 291, 41))
        self.Button5.setObjectName("Button5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.setButton = QtWidgets.QPushButton(self.centralwidget)
        self.setButton.setGeometry(QtCore.QRect(170, 20, 75, 23))
        self.setButton.setObjectName("setButton")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 50, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 283, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "Будильник"))
        self.Button2.setText(_translate("MainWindow", "Весёлое солнышко"))
        self.Button3.setText(_translate("MainWindow", "Грёзы"))
        self.Button4.setText(_translate("MainWindow", "Летняя фантазия"))
        self.Button5.setText(_translate("MainWindow", "Энергия"))
        self.label.setText(_translate("MainWindow", "Рингтон"))
        self.setButton.setText(_translate("MainWindow", "Установить"))
        self.CancelButton.setText(_translate("MainWindow", "Отменить"))
        
        self.Button1.clicked.connect(self.play("media/Alarm clock.mp3"))
        self.Button2.clicked.connect(self.play("media/Happy sunny.mp3"))
        self.Button3.clicked.connect(self.play("media/Dreams.mp3"))
        self.Button4.clicked.connect(self.play("media/Summer fantasy.mp3"))
        self.Button5.clicked.connect(self.play("media/Energy.mp3"))        
        self.setButton.clicked.connect(self.setmel())
        self.CancelButton.clicked.connect(self.canmel())
        
        
    def play(self, path):
        self.play = (True, path)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    
    
    def setmel(self):
        if self.play[0]:
            pygame.mixer.music.stop()
            self.melody = self.play[1]
            self.play = False, self.play[1]
    
    
    def canmel(self):
        if self.play[0]:
            pygame.mixer.music.stop()
            self.play = False, self.play[1]