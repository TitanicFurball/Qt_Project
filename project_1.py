import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from project_main_page import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 800, 600)
        self.Pause.clicked.connect(self.run)
 
    def run(self):
        pass
 
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())