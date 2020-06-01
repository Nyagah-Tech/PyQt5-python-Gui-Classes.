import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel,QCheckBox
from PyQt5.QtCore import QCoreApplication, Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Checkboxes'
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        # creating our checkbox 
        checkBox = QCheckBox('Do you like football ?',self)
        checkBox.resize(250,40)
        checkBox.move(100,100)
        checkBox.toggle()

        # connect our checkbox wit our checkBoxChange
        checkBox.stateChanged.connect(self.checkBoxChange)

        # creating our label 
        self.label = QLabel('Hello',self)
        self.label.resize(300,40)
        self.label.move(150,150)


        self.show()

    def checkBoxChange(self,state):
        if state == Qt.Checked:
            self.label.setText('Yes i like football !')
        else:
            self.label.setText('No i dont love football !')
    
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())