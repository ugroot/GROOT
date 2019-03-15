import sys
sys.path.append("..")

from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QLabel,QVBoxLayout,QLineEdit,QSizePolicy,QPushButton
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import QUrl,Qt

import urllib.request
from utils.newz import news_func

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.MainLayout = QVBoxLayout()
        self.elementLayout = QVBoxLayout()
    
        
        val = news_func()
        #print(val)
        url = val[0]['url']
        self.text = QLabel()
        self.text.setText('<a href="%s">Link</a>'%url)
        self.text.setOpenExternalLinks(True)
        self.box = myBox()
        self.MainLayout.addLayout(self.box.myBoxLayout)

        imageUrl = val[0]['urlToImage'] 
        data = urllib.request.urlopen(imageUrl).read()

        self.image = QImage()
        self.image.loadFromData(data)

        self.lbl = QLabel("Image")
        #To Keep The Aspect Ratio Upto the Maximum Size
        self.lbl.setPixmap(QPixmap(self.image).scaled(64,64,Qt.KeepAspectRatio))

        self.words = QLabel("This is a text")
        self.words2 = QLabel("This is another text")
        self.elementLayout.addWidget(self.text)
        self.elementLayout.setSpacing(10.0)
        self.elementLayout.addWidget(self.text)
        self.elementLayout.addWidget(self.words)
        self.elementLayout.addWidget(self.words2)
        #self.elementLayout.setColumnStretch(10,10)
        self.MainLayout.addLayout(self.elementLayout)
        #self.MainLayout.addWidget(self.label)
        self.setLayout(self.MainLayout)
        self.setGeometry(100,100,400,400)
        self.show()




class textField(QLineEdit):
    def __init__(self,parent=None):
        super(textField,self).__init__()


class myBox(QGridLayout):
    def __init__(self,parent=None):
        super(myBox,self).__init__()
        self.inp = QLabel("Input")
        self.inputEdit = QLineEdit()
        self.out = QLabel("Output")
        self.output = QLineEdit()
        self.speaker = QPushButton("Speak")
        self.myBoxLayout = QGridLayout()
        self.myBoxLayout.addWidget(self.inp,1,0)
        self.myBoxLayout.addWidget(self.inputEdit,1,1)
        self.myBoxLayout.addWidget(self.speaker,1,2)
        self.myBoxLayout.addWidget(self.out,2,0)
        self.myBoxLayout.addWidget(self.output,2,1)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

