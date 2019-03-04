from PyQt5.QtWidgets import QPushButton,QWidget, QMessageBox, QTextEdit, QLabel, QLineEdit, QGridLayout,QGridLayout
from PyQt5.QtGui import QIcon
from speechtotext import listen
from texttospeech import speak_this

class Groot_Ui(QWidget):
    def __init__(self):
        super(Groot_Ui,self).__init__()
        self.initUI()

    def initUI(self):
        # Self geometry

        inp = QLabel('Input')
        output = QLabel('Output')

        self.inpEdit = QLineEdit()  #Text Field for Input
        self.outputEdit = QLineEdit() #Text Field for Output

        grid = QGridLayout()  #Outer Layout
        gridInner = QGridLayout() #Inner layout
        gridInner.setSpacing(20)

        gridInner.addWidget(inp, 1, 0)
        gridInner.addWidget(self.inpEdit, 1, 1)

        gridInner.addWidget(output, 2, 0)
        gridInner.addWidget(self.outputEdit, 2, 1)

        grid.addLayout(gridInner,1,0)

        #Button is needed in parallel.
        speaker = QPushButton('Speak')
        grid.addWidget(speaker,1,1)
        self.setLayout(grid)

        self.setGeometry(350,350,600,150)
        self.setWindowTitle('GROOT')
        self.setWindowIcon(QIcon('asset/img/groot.png'))

        #Function of speaker button linked:
        speaker.clicked.connect(listen) #When the Speak button is clicked the listen function
        #is triggered.
        self.inpEdit.returnPressed.connect(self.callGroot)

        self.show()
         
    
    def callGroot(self):
        typed = str(self.inpEdit.text())
        speak_this(typed)


    #Function to display warning message for quitting
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()