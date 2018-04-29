import boto3
import pygame
import os  
import time


polly = boto3.client('polly')
spoker_text=polly.synthesize_speech(Text='I am jarvis here for your help',
									OutputFormat='mp3',
									VoiceId='Brian')

with open('output.mp3', 'wb') as f:
	f.write(spoker_text['AudioStream'].read())
	f.close()

print('lol')	
pygame.mixer.init()
pygame.init()
with open("output.mp3", "rb") as f:
	pygame.mixer.music.load(f)
	pygame.mixer.music.play()
	a=pygame.mixer.music.get_pos()
	
	while a != -1:
		print(a)
		a=pygame.mixer.music.get_pos()
		pass

	print(a)


pygame.mixer.quit()



