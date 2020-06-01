import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu
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
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    # the context menu event emmitters for pyqt5.
    # it takes two args: self and event  
    def contextMenuEvent(self,event):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction('New')
        oppenAct = contextMenu.addAction('Open')
        quitAct = contextMenu.addAction('Quit')

        # context menu is displayed using the exec_()  method inorder to get the coordinate of the mouse from the event object
        # and the mapToGlobal() changes the widget coordintes to the global coordinates
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            self.close()
    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())