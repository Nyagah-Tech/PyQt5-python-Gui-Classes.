import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QSlider, QVBoxLayout
from PyQt5.QtCore import QCoreApplication,Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Slider'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 300
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        vboxLayout = QVBoxLayout()
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(200,50)
        vboxLayout.addWidget(self.lineEdit)

        # there are two types of sliders that is the horizontal and the vertical 
        # QSlider(Qt.Vertical)
        # QSlider(Qt.Horizontal)
        self.slider = QSlider(Qt.Horizontal, self)
        # moving our slider using move() method 
        self.slider.move(220,30)
        # setting the minimum and maximum value 
        self.slider.setMinimum(1)
        self.slider.setMaximum(99)
        # setting a value to the slider
        self.slider.setValue(20)
        # setting a tick position either below or up \
        # self.slider.setTickPosition(QSlider.TicksAbove)
        # self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickPosition(QSlider.TicksAbove)
        # setting the slider interval
        self.slider.setTickInterval(10)
        # connect our slider with the changed value function 
        self.slider.valueChanged.connect(self.changedValue)

        vboxLayout.addWidget(self.slider)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def changedValue(self):
        size = str(self.slider.value())
        self.lineEdit.setText(size)
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())