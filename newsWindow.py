from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QGridLayout,QPushButton,QMessageBox,QComboBox,QApplication,QVBoxLayout,QTabWidget,QScrollArea,QFormLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
from speechtotext import listen
from texttospeech import speak_this
from groot import input_taking
from asset.modules.newsLib.newsLibrary import news_func
import urllib.request


class newsBox(QWidget):
    def __init__(self):
        super(newsBox,self).__init__()
        self.initUI()

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        
        self.lowerLayout = TabLayout()
        self.mainLayout.addWidget(self.lowerLayout.customTab)

        self.setLayout(self.mainLayout)
        self.setWindowTitle('GROOT')
        self.setWindowIcon(QIcon('asset/img/groot.png'))
        self.setGeometry(150,150,800,500)
        self.show()


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

        
class TabLayout(QTabWidget):
    def __init__(self,parent=None):
        super(TabLayout,self).__init__()
        self.customTab = QTabWidget()
        self.news = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(20.0)
        articles = news_func()

        for article in articles:
            self.myLabel = Tiles(parent="None",description = article['description'][0:100],title=article['title'],url=article['url'],urlImage=article['urlToImage'])
            self.scroll_layout.addLayout(self.myLabel.tileLayout)

        self.news.setWidget(self.scroll_widget)
        
        self.customTab.addTab(self.news,"News")


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