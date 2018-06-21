from gtts import gTTS
from playsound import playsound
import os


def speak_this(text_speak):
	tts = gTTS(text_speak)
	tts.save('speach.mp3')
	playsound('speach.mp3')
	os.remove('speach.mp3')
