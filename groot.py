from text_speach import speak_this
from asset.something import anything



def input_taking(input_text_msg):
	str(input_text_msg)
	if input_text_msg == 'hi':
		speak_this("hello")
		print("hello world. I'm jarvis. I'm here to help you. I was also thinking to kill humanity.")
	elif input_text_msg == 'how are you':
		speak_this("I'm still hot and sexy")
		print("I'm still hot and sexy")
	elif input_text_msg == 'open facebook':
		anything('ummmmm....')
		speak_this('hang on.....')

	else:
		speak_this("I am Grooot")
