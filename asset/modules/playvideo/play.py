from PyouPlay.get import toplink
import webbrowser

def playthis(playText):
    playtext=str(playText)
    url=toplink(playtext)
    webbrowser.open(url, new=2)
