from tkinter import *
import tkinter.messagebox
from groot import input_taking
from speechtotext import listen


window = Tk()
button_flag = True
#this is to set window title
window.title("I'm Groot")
 
#set background colour
window.configure(background="#D7DBDD")

def OnClicked(arg=None):
	userData = E1.get()
	ans=input_taking(userData)
	print(userData)
	return userData

def listen_def():
	textfromspeach=listen();
	print(textfromspeach)
	ans=input_taking(textfromspeach)

def printit(arg=None):
	global E1
	string = E1.get()
	print(string)

#text input
label1 = Label(window,text="Enter text here:-",width=15)
label1.grid(row=0, sticky=W)
E1 = Entry(window, width=30)
E1.grid(row=0,column=1)
E1.focus_set()

E1.bind("<Return>",OnClicked)

#b = Label(window,text = text1)
#b.grid(row=1,column=1)


#listen button
ans="Output:-"
my_text = Label(window, text=ans, width=10)
my_text.grid(row=1)
#text2=Label(window,text="")
photo=PhotoImage(file="icon2.png")
L1 = Button(window,text="Press to speak",image=photo, command=listen_def,width = 26, height=50)
L1.grid(row=0, column=2, columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

#this is to make window on top
#not able to get it in focus have something is mind please help ;)
window.attributes("-topmost", True)

#this is set window default size and its position
window.geometry("347x66+700+400")

window.mainloop()
