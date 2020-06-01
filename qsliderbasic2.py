import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel,QSlider,QWidget
from PyQt5.QtCore import QCoreApplication,Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Slider Part 2'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 400
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        # making our slider 
        self.slider = QSlider(Qt.Horizontal,self)
        self.slider.setGeometry(60,60,100,20)
        # connect our slider with the the label 
        self.slider.valueChanged[int].connect(self.changedValue)

        # making a label with an image in it 
        self.label = QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('images/jamaica1.jpeg'))
        self.label.setGeometry(60,100,150,120)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def changedValue(self,value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('images/jamaica1.jpeg'))
        elif value < 50 :
            self.label.setPixmap(QtGui.QPixmap('images/jamaica3.jpeg'))
        else :
            self.label.setPixmap(QtGui.QPixmap('images/image2.jpg'))
    
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())