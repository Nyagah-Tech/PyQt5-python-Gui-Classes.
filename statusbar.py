import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QWidget, QAction, QMenuBar


class Window(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.title = 'Qstatus Bar And Menu Bar'
        self.top = 200
        self.left = 200
        self.width = 600
        self.height = 500

        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        # creating our status bar \
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('this is a simple status bar')

        # creating a menu bar 
        mainMenu = self.menuBar()
        filemenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        searchMenu = mainMenu.addMenu('Search')
        toolMenu = mainMenu.addMenu('Tool')
        helpMenu = mainMenu.addMenu('Help')


        viewAction = QAction('View Status',self,checkable = True)
        viewAction.setStatusTip('View StatusBar')
        viewAction.setChecked(True)
        viewAction.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewAction)



        # creating an action   
        exitButton = QAction(QIcon('cr2.jpg'),'Exit',self)

        # creating a shortcut to close the application 
        exitButton.setShortcut("ctrl+E")
        # on mouse pointer this will appear 
        exitButton.setStatusTip('Exit Application')
        # button is  connected to the close function 
        exitButton.triggered.connect(self.close)

        filemenu.addAction(exitButton)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    
    def close(self):
        QCoreApplication.instance().quit()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())