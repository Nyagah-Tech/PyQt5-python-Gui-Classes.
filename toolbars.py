import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 ToolBars'
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):

        exitAction = QAction(QtGui.QIcon('images/f3.jpeg'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

        copyAction = QAction(QtGui.QIcon('images/cr2.jpg'),'Copy',self)
        copyAction.setShortcut('Ctrl+C')

        pasteAction = QAction(QtGui.QIcon('images/jamaica1.jpeg'),'Paste',self)
        pasteAction.setShortcut('Ctrl+V')

        deleteAction = QAction(QtGui.QIcon('images/image1.jpeg'),'Delete',self)
        deleteAction.setShortcut('Ctrl+D')

        saveAction = QAction(QtGui.QIcon('images/image2.jpg'),'Save',self)
        saveAction.setShortcut('Ctrl+S')

        # creating our toolbar 
        self.toolbar = self.addToolBar('Toolbar')

        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(deleteAction)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())