from tkinter import *
from jarvis import input_taking


window = Tk()

#this is to set window title
window.title("Jarvis:Your personal bro assistance")

#set background colour
window.configure(background="#D7DBDD")


def OnClicked():
    userData = E1.get()
    input_taking(userData)

#text input and enter button
E1 = Entry(window, width=100)
L1 = Button(window, text="Enter", width=3,command=OnClicked)
L1.pack( side = RIGHT)
E1.pack(side = LEFT)




#this is to make window on top
#not able to get it in focus have something is mind please help ;)
window.attributes("-topmost", True)

#this is set window default size and its position
window.geometry("700x80+700+400")

window.mainloop()
window.destroy()
