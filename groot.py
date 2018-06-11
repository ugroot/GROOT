from text_speach import speak_this
from asset.something import anything



def input_taking(input_text_msg):
	str(input_text_msg)
	if input_text_msg == 'hi groot':
		speak_this("hello")
		return "hello world. I'm jarvis. I'm here to help you. I was also thinking to kill humanity."

	elif input_text_msg == 'how are you':
		speak_this("I'm still hot and sexy")
		return "I'm still hot and sexy"

	elif input_text_msg == 'what is love':
		speak_this("It's is something you should not do")
		return "I'm still hot and sexy"

	elif input_text_msg == 'open facebook':
		speak_this('hang on.....')

	else:
		speak_this("I am Groot")
		return "I am Groot"
