from PyQt5.QtWidgets import QApplication
from faceUnlocker import unlock
from texttospeech import speak_this
import sys
 

from Gui import Groot_Ui


if __name__ == '__main__':
    app = QApplication(sys.argv)
    security = unlock()
    if security == True:
        speak_this("Master Found! Welcome Master!")
        groot = Groot_Ui()   #! Groot UI defined in the Gui.py file
    else:
        speak_this("Imposter Found! Cannot Allow Access")
        sys.exit(1)
    
    sys.exit(app.exec_())
