import pyttsx4

def speak(audio):
    engine = pyttsx4.init('sapi5')
    voices = engine.getProperty('voices')
    # for v in voices:
    #     print(v)
    engine.setProperty('voice', voices[3].id)
    engine.setProperty('rate', 145 )
    print("             ")
    print('J.A.R.V.I.S: ' , audio)
    print("             ")
    engine.say(audio)
    try:
        engine.runAndWait()
    except RuntimeError:
        print('Overloading PYTTSX4!')

# speak('hi, how are you?')