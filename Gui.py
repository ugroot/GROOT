from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QGridLayout,QPushButton,QMessageBox,QComboBox,QApplication,QVBoxLayout,QTabWidget,QScrollArea,QFormLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
from speechtotext import listen
from texttospeech import speak_this
from groot import input_taking
from newsWindow import newsBox
from asset.modules.newsLib.newsLibrary import news_func
import urllib.request


class Groot_Ui(QWidget):
    def __init__(self):
        super(Groot_Ui,self).__init__()
        self.initUI()

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.upperLayout = inpOutWidgetLayout()
        self.mainLayout.addLayout(self.upperLayout.inpOutLayout)
        self.mainLayout.addStretch(1)
        
        self.setLayout(self.mainLayout)
        self.setWindowTitle('GROOT')
        self.setWindowIcon(QIcon('asset/img/groot.png'))
        self.setGeometry(150,150,800,100)
        self.show()

        #Other Functions:
        self.upperLayout.speaker.clicked.connect(self.listen_reply)
        self.upperLayout.newsButton.clicked.connect(self.createNewsLayout)
        self.upperLayout.inputEdit.returnPressed.connect(self.callGroot)

    def callGroot(self):
        typed = str(self.upperLayout.inputEdit.text())
        reply = input_taking(typed)
        self.upperLayout.outputEdit.setText(reply)

    def listen_reply(self):
        spoken = listen()
        reply = input_taking(spoken)
        self.upperLayout.outputEdit.setText(reply)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:                
            self.close()

    def createNewsLayout(self):

        self.newsWindow = newsBox()
        self.newsWindow.show()     
    

    #Function to display warning message for quitting
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




class inpOutWidgetLayout(QVBoxLayout):
    def __init__(self,parent=None):
        super(inpOutWidgetLayout,self).__init__()
        #Grid Layout for the upper part.
        self.inpOutLayout = QGridLayout()

        self.inputLabel = QLabel('Input')
        self.inputLabel.setMinimumSize(self.sizeHint())
        self.outputLabel = QLabel('Output')
        self.inputLabel.setMinimumSize(self.sizeHint())
        #Speaker Widget
        self.speaker = QPushButton('Speak')
        self.speaker.setMinimumSize(self.sizeHint())
        #Text Field for Input
        self.inputEdit = QLineEdit()
        self.inputEdit.setMinimumSize(self.sizeHint()) 
        #Text Field for Output
        self.outputEdit = QLineEdit()
        self.outputEdit.setMinimumSize(self.sizeHint())
        #newsButton Button
        self.newsButton  = QPushButton('News')
        self.newsButton.setMinimumSize(self.sizeHint())
        #Spacing between the widgets
        self.inpOutLayout.setSpacing(20)
        #Positioning Inner Widgets
        self.inpOutLayout.addWidget(self.inputLabel, 1, 0)
        self.inpOutLayout.addWidget(self.inputEdit, 1, 1)
        self.inpOutLayout.addWidget(self.speaker,1,2)
        self.inpOutLayout.addWidget(self.outputLabel, 2, 0)
        self.inpOutLayout.addWidget(self.outputEdit, 2, 1)
        self.inpOutLayout.addWidget(self.newsButton,2,2)

        #Button is needed in parallel.
        
        


