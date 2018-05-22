import boto3
import pygame
import os
import time

def speak_this(text_speak):
	polly = boto3.client('polly')
	spoker_text=polly.synthesize_speech(Text=text_speak,
										OutputFormat='mp3',
										VoiceId='Brian')

	with open('output.mp3', 'wb') as f:
		f.write(spoker_text['AudioStream'].read())
		f.close()


	pygame.mixer.init()
	pygame.init()
	with open("output.mp3", "rb") as f:
		pygame.mixer.music.load(f)
		pygame.mixer.music.play()
		a=pygame.mixer.music.get_pos()

	while a != -1:

		a=pygame.mixer.music.get_pos()
		pass

	print(a)


	os.remove('output.mp3')
	pygame.mixer.quit()
