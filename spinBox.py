import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox,QLabel,QVBoxLayout
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Spin Box'
        self.left = 100
        self.top = 100
        self.width = 480
        self.height = 300
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        # making a vertical box QVBoxLayout
        vBoxLayout = QVBoxLayout(self)

        # make a label and move it
        self.label = QLabel('Current Value', self)
        self.label.move(100,100)
        self.label.resize(250,40)
        # adding to our vBoxLayout 
        vBoxLayout.addWidget(self.label)

        # create a spinbox 
        self.spinbox = QSpinBox(self)
        self.spinbox.move(100,70)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(100)
        vBoxLayout.addWidget(self.spinbox)
        self.spinbox.valueChanged.connect(self.valueChanged)
        vBoxLayout.addWidget(self.spinbox)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def valueChanged(self):
        self.label.setText('Current value :' + str(self.spinbox.value()))
 
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())