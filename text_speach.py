from gtts import gTTS
from playsound import playsound
import os


def speak_this(text_speak):
	tts = gTTS(text_speak)
	tts.save('speech.mp3')
	playsound('speech.mp3')
	os.remove('speech.mp3')
