import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak loudly and in good tone:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('you said : {}'.format(text))
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as er:
        print('Could not request results from Google Speech Recognition service; {0}'.format(er))

