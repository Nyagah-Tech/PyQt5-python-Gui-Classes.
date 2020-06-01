import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Images'
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):

        # creating our label
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('images/image2.jpg'))
        self.label.setGeometry(60,50,1000,400)
    

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

   
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())