from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QGridLayout,QPushButton,QMessageBox,QComboBox,QApplication,QVBoxLayout,QTabWidget,QScrollArea,QFormLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
import sys
import urllib.request

class newsElements(QWidget):
    def __init__(self,Heading="None",SubHeading="None",Url="None",ImageUrl="None",parent="None"):
        super(newsElements,self).__init__()
        self.elementLayout = QGridLayout()
        self.textLayout = QVBoxLayout()
        self.heading = QLabel('<b>%s</b>'%Heading)
        self.subHeading = QLabel()
        self.subHeading.setText('<b><a href="{}">{}More</a></b>'.format(Url,SubHeading))
        self.subHeading.setOpenExternalLinks(True)

        data = urllib.request.urlopen(ImageUrl).read()
        self.image = QImage()
        self.image.loadFromData(data)

        self.lbl = QLabel("image")
        self.lbl.setPixmap(QPixmap(self.image).scaled(64,64,Qt.KeepAspectRatio))

        self.textLayout.addWidget(self.heading)
        self.textLayout.addWidget(self.subHeading)
        self.elementLayout.addLayout(self.textLayout,1,0)
        self.elementLayout.addWidget(self.lbl,1,1)

        self.setLayout(self.elementLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = newsElements("Spotifyme","NewsNewsNews","https://google.com","https://www.gstatic.com/webp/gallery3/1.png",parent=None)
    sys.exit(app.exec_())
