from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QGridLayout,QPushButton,QMessageBox,QComboBox,QApplication,QVBoxLayout,QTabWidget,QScrollArea,QFormLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
from speechtotext import listen
from texttospeech import speak_this
from groot import input_taking
from utils.newsLibrary import news_func
import urllib.request


class Groot_Ui(QWidget):
    def __init__(self):
        super(Groot_Ui,self).__init__()
        self.initUI()

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.upperLayout = inpOutWidgetLayout()
        self.mainLayout.addLayout(self.upperLayout.inpOutLayout)
        #self.mainLayout.addStretch(1)
        
        self.lowerLayout = TabLayout()
        self.mainLayout.addWidget(self.lowerLayout.customTab)

        self.setLayout(self.mainLayout)
        self.setWindowTitle('GROOT')
        self.setWindowIcon(QIcon('asset/img/groot.png'))
        self.setGeometry(150,150,800,500)
        self.show()

        #Other Functions:
        self.upperLayout.speaker.clicked.connect(self.listen_reply)
        # self.upperLayout.refresh.clicked.connect(self.createPopup)
        self.upperLayout.inputEdit.returnPressed.connect(self.callGroot)


    # def createPopup(self):
    #     popup = Popup()
    #     popup.show()

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
        #Refresh Button
        self.refresh  = QPushButton('Refresh')
        self.refresh.setMinimumSize(self.sizeHint())
        #Spacing between the widgets
        self.inpOutLayout.setSpacing(20)
        #Positioning Inner Widgets
        self.inpOutLayout.addWidget(self.inputLabel, 1, 0)
        self.inpOutLayout.addWidget(self.inputEdit, 1, 1)
        self.inpOutLayout.addWidget(self.speaker,1,2)
        self.inpOutLayout.addWidget(self.outputLabel, 2, 0)
        self.inpOutLayout.addWidget(self.outputEdit, 2, 1)
        self.inpOutLayout.addWidget(self.refresh,2,2)

        #Button is needed in parallel.
        
        

class TabLayout(QTabWidget):
    def __init__(self,parent=None):
        super(TabLayout,self).__init__()
        self.customTab = QTabWidget()
        self.news = QScrollArea()
        #self.news.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(20.0)
        articles = news_func()

        for article in articles:
            self.myLabel = Tiles(parent="None",description = article['description'][0:100],title=article['title'],url=article['url'],urlImage=article['urlToImage'])
            self.scroll_layout.addLayout(self.myLabel.tileLayout)

        self.news.setWidget(self.scroll_widget)

        self.wiki = QWidget()
        
        self.customTab.addTab(self.news,"News")
        self.customTab.addTab(self.wiki,"Add More Feature")

class Tiles(QWidget):
    def __init__(self,parent="None",title="None",description="None",url="None",urlImage="None"):
        super(Tiles,self).__init__()
        #Heading Widget
        self.heading = QLabel('<b>%s</b>'%title)
        #SubHeading Widget with link to open in browser
        self.subHeading = QLabel('{}<a href="{}">...more</a>'.format(description,url))
        self.subHeading.setOpenExternalLinks(True)
        #Image Widget with article
        data = urllib.request.urlopen(urlImage).read()
        self.image = QImage()
        self.image.loadFromData(data)
        self.imageLabel = QLabel("image")
        self.imageLabel.setPixmap(QPixmap(self.image).scaled(64,64,Qt.KeepAspectRatio))
        self.tileLayout = QGridLayout()
        self.tileLayout.addWidget(self.heading,1,0)
        self.tileLayout.addWidget(self.imageLabel,1,1)
        self.tileLayout.addWidget(self.subHeading,2,0)

# class Popup(QWidget):
#     def __init__(self, parent=None):
#         super(Popup,self).__init__()
#         self.PopupLayout = QGridLayout()
#         self.title("Hi I am Groot Why Don't you add a Keyword to search in news?")
#         self.keywordField = QLineEdit()
#         self.keywordField.returnPressed.connect(closemyself)

#         def closemyself():
#             typed = str(self.keywordField.text())

#         self.setGeometry(150,150,800,500)
#         print("I am created")
#         self.show()