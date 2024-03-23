from basics import listen, speak
from basics.hotword import hotWord
from brain import gpt

if __name__=="__main__":
    while True:
        hotWord.hotword()
        query = listen.takeQuery()
        try:
            VirtualAssistant = gpt.ChatGpt(query)
            speak.speak(VirtualAssistant)
        except Exception as e:
            print(e)
        else:
            pass
