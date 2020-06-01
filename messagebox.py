import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'pyqt5 push buttons'
        self.left = 100
        self.top = 100
        self.width = 680
        self.height =  540
    # set window icon 
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

    # creating our push button 
        button = QPushButton('AboutBox',self)
        button2 = QPushButton('QuestionMsg', self)

    # moving our push button using the x an y 
        button.move(200,200)
        button2.move(100,100)

    # linking our button with the qmessagebox 
        button.clicked.connect(self.aboutMe)
        button2.clicked.connect(self.QuestionMessage)

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def aboutMe(self):
        QMessageBox.about(
            self,
            'About message',
            'This is about message box'
        )
    
    def QuestionMessage(self):
        message = QMessageBox.question(
            self,
            'Question Message',
            'Have you choosen me?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if message == QMessageBox.Yes:
            print('Yes i have')
        else:
            print('No i have not')

   

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
