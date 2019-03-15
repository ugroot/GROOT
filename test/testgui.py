import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.windowLayout =  QVBoxLayout()
        self.button = QPushButton("This is a button")
        self.button.setMinimumSize(self.minimumSizeHint())
        self.heading = QLabel("This is a text")
        self.heading.setMaximumSize(200,200)
        self.windowLayout.addWidget(self.heading)
        self.windowLayout.addWidget(self.button)
        self.setLayout(self.windowLayout)
        self.setGeometry(100,100,300,300)
        self.show()

def givemeback():
    data = [{'heading':'First','subheading':'This is a flower','url':'https://google.com','urlImage':'https://www.gstatic.com/webp/gallery3/1.png'},{'heading':'Second','subheading':'This is better flower','url':'https://facebook.com','urlImage':'https://www.gstatic.com/webp/gallery3/2.png'}]

if __name__ =='__main__':
    app = QApplication(sys.argv)
    mw = MyWindow()
    sys.exit(app.exec_())