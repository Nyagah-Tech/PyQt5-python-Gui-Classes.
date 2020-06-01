import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 

class ButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'QPushButtons '
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        layout = QHBoxLayout()
        # button 1 
        self.b1 = QPushButton("Button 1")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.setIcon(QIcon('f3.jpeg'))
        self.b1.clicked.connect(self.stateOfButton)
        self.b1.clicked.connect(lambda:self.clickedButton(self.b1))
        layout.addWidget(self.b1)
  
        # button 2 
        self.b2 = QPushButton("Button 2")
        self.b2.setEnabled(True)
        self.b2.clicked.connect(lambda:self.clickedButton(self.b2))
        layout.addWidget(self.b2)

        # button 3 
        self.b3 = QPushButton("Button 3")
        self.b3.clicked.connect(lambda:self.clickedButton(self.b3))
        layout.addWidget(self.b3)

        # button 4 
        self.b4 = QPushButton("Button 4")
        self.b4.clicked.connect(lambda:self.clickedButton(self.b4))
        self.b4.setDefault(True)
        layout.addWidget(self.b4)

        self.setLayout(layout)

    def stateOfButton(self):
        if self.b1.isChecked():
            print('button is pressed')
        else:
            print("button is released")

    def clickedButton(self,btn):
        print('clicked button is '+btn.text())

def main():
    app = QApplication(sys.argv)
    obj = ButtonExample()
    obj.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()