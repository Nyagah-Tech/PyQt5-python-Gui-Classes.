import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem,QVBoxLayout
from PyQt5.QtCore import QCoreApplication

class Window(QWidget ):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Tables'
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('f3.jpeg'))

        self.UnitUI()

    def UnitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.creatingTables()
        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vboxLayout)
       
        self.show()

    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setItem(0,0, QTableWidgetItem('Name'))
        self.tableWidget.setItem(0,1, QTableWidgetItem('Email'))
        self.tableWidget.setItem(0,2, QTableWidgetItem('Phone No'))

        self.tableWidget.setItem(1,0, QTableWidgetItem('Dan'))
        self.tableWidget.setItem(1,1, QTableWidgetItem('danmuv12@gmail.com'))
        self.tableWidget.setItem(1,2, QTableWidgetItem('0712345678'))
        self.tableWidget.setColumnWidth(1,200)

        self.tableWidget.setItem(2,0, QTableWidgetItem('Dante'))
        self.tableWidget.setItem(2,1, QTableWidgetItem('danmuv11@gmail.com'))
        self.tableWidget.setItem(2,2, QTableWidgetItem('07123456867'))

    def close(self):
        QCoreApplication.instance().quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())