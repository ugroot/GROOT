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
        var=r.recognize_google(audio)
    except sr.UnknownValueError:
        var="Groot can't understand could not understand audio"
    except sr.RequestError as e:
        var=" Look's like, there is some problem with Google Speech Recognition"

    return var

    #will show all posible text from audio
    #print(r.recognize_google(audio, show_all=True))
