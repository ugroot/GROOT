import speech_recognition as sr

def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    #will show all posible text from audio
    #print(r.recognize_google(audio, show_all=True))
