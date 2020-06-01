import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QDialog,QPushButton,QGridLayout,QGroupBox,QVBoxLayout
from PyQt5.QtCore import QCoreApplication

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Grid Layout '
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.gridLayoutCreation()
        
        # displays our group box 
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.groupBox)
        self.setLayout(vboxLayout)
        self.show()

    # the grid layout function
    def gridLayoutCreation(self):
        self.groupBox = QGroupBox("Grid Layout Example")

        # grid layout divides or wndow into row and columns 
        gridLayout = QGridLayout()

        gridLayout.addWidget(QPushButton('1'),0,0)
        gridLayout.addWidget(QPushButton('2'),0,1)
        gridLayout.addWidget(QPushButton('3'),0,2)
        gridLayout.addWidget(QPushButton('A'),1,0)
        gridLayout.addWidget(QPushButton('B'),1,1)
        gridLayout.addWidget(QPushButton('C'),1,2)

        # setting our grid layout to our groupbox 
        self.groupBox.setLayout(gridLayout)
        

    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())