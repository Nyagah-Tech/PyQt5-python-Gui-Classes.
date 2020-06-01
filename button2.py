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

        # creating a push button 
        button = QPushButton('close',self)

        # moving the button 
        button.move(200,200)
         
        # adding tooltip 
        button.setToolTip("<h3>This is a click Button</h3>")

        # adding a signal/event to be called once a button is clicked 
        button.clicked.connect(self.closeApp)

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def close(self):
        QCoreApplication.instance().quit()

    # message box and fetching the user input 
    def closeApp(self):
        reply = QMessageBox.question(
            self,
            'close message',
            'are you sure to close window',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        # checking if the reply is a yes 
        if reply == QMessageBox.Yes:
            self.close()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
