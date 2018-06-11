import pyttsx3

def speak_this(text_speak):

	groot = pyttsx3.init();
	voices = groot.getProperty('voices')
	groot.setProperty('voice', voices[0].id)
	groot.say(text_speak);
	groot.runAndWait();
