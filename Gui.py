from tkinter import *
from groot import input_taking
from speechtotext import listen


window = Tk()
button_flag = True
#this is to set window title
window.title("Jarvis:Your personal bro assistance")

#set background colour
window.configure(background="#D7DBDD")

def OnClicked(arg=None):
    userData = E1.get()
    input_taking(userData)

def listen_def():
	audio=listen();

#text input
E1 = Entry(window, width=100)
E1.bind("<Return>",OnClicked)

#listen button
L1 = Button(window, command=listen_def)
L1.pack(side = RIGHT)
E1.pack(side = LEFT)

#this is to make window on top
#not able to get it in focus have something is mind please help ;)
window.attributes("-topmost", True)

#this is set window default size and its position
window.geometry("700x80+700+400")

window.mainloop()
window.destroy()
