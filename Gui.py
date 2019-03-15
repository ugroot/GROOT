from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QGridLayout,QPushButton,QMessageBox,QComboBox,QApplication,QVBoxLayout,QTabWidget,QScrollArea,QFormLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
from speechtotext import listen
from texttospeech import speak_this
from groot import input_taking
from utils.newz import news_func
import urllib.request

class Groot_Ui(QWidget):
    def __init__(self):
        super(Groot_Ui,self).__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()
    
        self.upperLayout = inpOutLayout()
        mainLayout.addLayout(self.upperLayout.inpOutLayout)

        self.tabs = TabLayout()
        #This line sets max width for the news tab but still it is cutting some of the element.
        #self.tabs.scroll_widget.setMaximumWidth(self.tabs.width())
        mainLayout.addWidget(self.tabs.customTab)
        mainLayout.setSpacing(20.0)
        
        self.setLayout(mainLayout)
        self.setGeometry(150,150,800,500)
        self.setWindowTitle('GROOT')
        self.setWindowIcon(QIcon('asset/img/groot.png'))

        #Functions and Activities linked with the Gui

        #When the Speak button is clicked the listen function is triggered.
        self.upperLayout.speaker.clicked.connect(self.listen_reply)
        #When Input is done and enter is pressed the Groot starts processing it.
        self.upperLayout.inpEdit.returnPressed.connect(self.callGroot)
        self.show()
             
    def callGroot(self):
        typed = str(self.upperLayout.inpEdit.text())
        reply = input_taking(typed)
        self.outputEdit.setText(reply)

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

class inpOutLayout(QGridLayout):
    def __init__(self,parent=None):
        super(inpOutLayout,self).__init__()
        self.inp = QLabel('Input')
        self.output = QLabel('Output')
        self.inpOutLayout = QGridLayout()
        #Text Field for Input
        self.inpEdit = QLineEdit() 
        #Text Field for Output
        self.outputEdit = QLineEdit()
        self.inp_outLayout = QGridLayout()
        #Spacing between the widgets
        self.inpOutLayout.setSpacing(20)
        #Positioning Inner Widgets
        self.inpOutLayout.addWidget(self.inp, 1, 0)
        self.inpOutLayout.addWidget(self.inpEdit, 1, 1)
        self.inpOutLayout.addWidget(self.output, 2, 0)
        self.inpOutLayout.addWidget(self.outputEdit, 2, 1)
        #Button is needed in parallel.
        self.speaker = QPushButton('Speak')
        self.inpOutLayout.addWidget(self.speaker,1,2)

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
            self.block = newsElements(article['title'],article['description'],article['url'],article['urlToImage'],parent=None)
            self.scroll_layout.addWidget(self.block) #This line is messing up with something.
            print(self.block.textHeading)
            print(type(self.block)) #Works correctly till here.
    

        #self.news.setWidgetResizable(True)
        self.news.setWidget(self.scroll_widget)

        self.wiki = QWidget()
        
        self.customTab.addTab(self.news,"News")
        self.customTab.addTab(self.wiki,"Wiki")
        #self.news.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.MinimumExpanding)
        
class newsElements(QWidget):
    def __init__(self,Heading="None",SubHeading="None",Url="None",ImageUrl="None",parent="None"):
        super(newsElements,self).__init__()
        self.textHeading = Heading
        self.elementLayout = QGridLayout()
        self.textLayout = QVBoxLayout()
        self.heading = QLabel('<b>%s</b>'%Heading)
        self.subHeading = QLabel('<b><a href="{}">{}More</a></b>'.format(Url,SubHeading))

        data = urllib.request.urlopen(ImageUrl).read()
        self.image = QImage()
        self.image.loadFromData(data)

        self.lbl = QLabel("image")
        self.lbl.setPixmap(QPixmap(self.image).scaled(64,64,Qt.KeepAspectRatio))

        self.textLayout.addWidget(self.heading)
        self.textLayout.addWidget(self.subHeading)
        self.elementLayout.addLayout(self.textLayout,1,0)
        self.elementLayout.addWidget(self.lbl,1,1)

        
        




