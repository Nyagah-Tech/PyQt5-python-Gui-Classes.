import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget,QMessageBox,QPushButton,QLineEdit
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'My context menu'
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        # create our line eddit and move it using the move method 
        self.lineedit = QLineEdit(self)
        self.lineedit.move(100,100)

        # resizing out lineedit using resize method 
        self.lineedit.resize(200,40)

        self.button = QPushButton('Show Text', self)
        self.button.move(150,150)
        self.button.clicked.connect(self.onClick)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    # method that will display the message in a messagebox once the button is clicked 
    def onClick(self):
        textValue = self.lineedit.text()
        QMessageBox.question(
            self,
            'Line Edit',
            'You have typed '+textValue,
            QMessageBox.Ok,
            QMessageBox.Ok
        )

    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())