import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class HelloWord(QWidget):
    def __init__(self):
       super().__init__()
       self.title = 'PyQt5 simple window'
       self.left = 10
       self.top = 10
       self.width = 640
       self.height =  480
    #    self.hboxLayout()
       self.vboxLayout()
       self.initUI()
    # def hboxLayout(self):
    #     hbox = QHBoxLayout()
    #     label = QLabel('welcome to my first app')
    #     label.setAlignment(Qt.AlignCenter)
    #     hbox.addWidget(label)
    #     self.setLayout(hbox)
    def vboxLayout(self):
        labelV4 = QLabel('<a href="#">hover on this</a>')
        labelV1 = QLabel(text='<a href="www.google.com">this is a vertical label linkrd to google</a>')
        labelV2 = QLabel()
        labelV3 = QLabel()
        
        vbox = QVBoxLayout()
        # settext method 
        labelV2.setText('this is set text method')

        # setAlignment  method 
        labelV1.setAlignment(Qt.AlignCenter)
        
        # setindent method 
        labelV2.setIndent(100)

        # setPixmap method 
        labelV3.setPixmap(QPixmap('f3.jpeg'))
        
        # # setWordWrap method 
        # labelV2.setWordWrap(True)

        # # settextinteractionflags 
        # labelV1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # # setOpenExternalLinks 
        # labelV1.setOpenExternalLinks(True)

        # linkActivated method 
        labelV1.linkHovered.connect(self.hovered)

        vbox.addWidget(labelV1)
        vbox.addWidget(labelV2)
        vbox.addWidget(labelV3)
        vbox.addWidget(labelV4)
        
        self.setLayout(vbox)
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        button = QPushButton('PyQt5 Button',self)
        button.setToolTip('this is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        img = QIcon('f3.jpeg')
        self.setWindowIcon(img)
        self.show()

    @pyqtSlot()
    def hovered(self):
        print('Its hovered')
    def on_click(self):
        print('PyQt5 button clicked')
    

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = HelloWord()
    sys.exit(app.exec_())
