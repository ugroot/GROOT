from tkinter import *
from groot import input_taking
from speechtotext import listen

window = Tk()
button_flag = True
#this is to set window title
window.title("Groot:Your personal bro assistance")

#set background colour
window.configure(background="#D7DBDD")

def OnClicked(arg=None):
    userData = E1.get()
    ans=input_taking(userData)

def listen_def():
	textfromspeach=listen();
	print(textfromspeach)
	ans=input_taking(textfromspeach)

#text input
E1 = Entry(window, width=100)
E1.bind("<Return>",OnClicked)


#listen button
L1 = Button(window,text="Press to speak", command=listen_def, height=200)
L1.pack(side = RIGHT)
E1.pack()
ans="Output will be here"
my_text = Label(window, text=ans, width=100)
my_text.pack(side=LEFT)
#this is to make window on top
#not able to get it in focus have something is mind please help ;)
window.attributes("-topmost", True)

#this is set window default size and its position
window.geometry("700x80+700+400")

window.mainloop()
