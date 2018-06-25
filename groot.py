from text_speach import speak_this
from random import randint
import sys
sys.path.insert(0, 'asset/modules')
from OpenUrl.openurl import openweb
import re

def input_taking(input_text_msg):
	didyousay=('hi groot',
			  'how are you',
			  'what is love',
			  'open facebook',
			  'how are you so smart'
			  )

	ansisthis=("hello, What can i do for you",
			   "I'm still hot and sexy. Tell me something about you hotty",
			   "It's is something you should not do",
			   "oh, It is because my Creator is so smart."
			   )

	whenidontknow=("I am Groot",
				   "what you are saying bro",
				   "What the fuck, say again",
				   "ok, lets try again")

	if re.findall('[A-Z|a-z]{2,}[.][a-z]{2,}', input_text_msg):
		urls=re.findall('[A-Z|a-z]{2,}[.][a-z]{2,}', input_text_msg)
		url=urls[0]
		url_sk=re.findall('([a-z|A-Z]{2,})[.]', url)
		speak_this('opening'+url_sk[0]+'please wait!!')
		returnvar="opening'+url_sk[0]+'please wait!!"
		openweb(url)

	else:
		l=0
		for i in range(0,3):
			if didyousay[i]==input_text_msg.lower():
				speak_this(ansisthis[i])
				returnvar=ansisthis[i]
				l=1

			if l==0:
				i=randint(0, 3)
				speak_this(whenidontknow[i])
				returnvar=whenidontknow[i]

	return returnvar

	# if input_text_msg.lowercase() == 'hi groot':
	# 	speak_this("hello")
	# 	return "hello world. I'm jarvis. I'm here to help you. I was also thinking to kill humanity."
	#
	# elif input_text_msg.lowercase() == 'how are you':
	# 	speak_this("I'm still hot and sexy")
	# 	return "I'm still hot and sexy"
	#
	# elif input_text_msg.lowercase() == 'what is love':
	# 	speak_this("It's is something you should not do")
	# 	return "I'm still hot and sexy"
	#
	# elif input_text_msg.lowercase() == 'open facebook':
	# 	speak_this('hang on.....')
	#
	# else:
	# 	speak_this("I am Groot")
	# 	return "I am Groot"
