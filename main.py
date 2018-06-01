from text_speach import speak_this
from asset.something import anything
import re



def input_taking(input_text_msg):
	str(input_text_msg)

input_text=input('hello,, say something \n ')
input_taking(input_text)

if input_text == 'hi':
	speak_this("hello world. I'm jarvis. I'm here to help you. I was also thinking to kill humanity.")
	print("hello world. I'm jarvis. I'm here to help you. I was also thinking to kill humanity.")
elif input_text == 'how are you':
	speak_this("I'm still hot and sexy")
	print("I'm still hot and sexy")
elif input_text == 'open facebook':
	anything('ummmmm....')
	speak_this('hang on.....')

else:
	speak_this("look's like i don't know what you are saying nigga")
	input_taking(input())
