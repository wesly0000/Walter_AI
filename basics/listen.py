import speech_recognition as sr


def takeQuery():
    # It takes microphone input from the user and returns string output
        time_listen = 3
        # Jarvis.TakeCommand()
        r = sr.Recognizer()
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                
                print("\nListening...")

                # whiteLEd()
                r.pause_threshold = 0.6
                audio = r.listen(source, phrase_time_limit=3)

                try:
                        print("Processing.....\n")
                        #playsound(path.process)
                        # greenled()
                        query = r.recognize_google(audio, language='en-in')
                        query = query.lower()
                
                        print("             ")
                        print('\nW.E.S.L.Y(online): ' + query+ '\n')
                        print("             ")
                        return query
        
                except Exception as e:
                        print(e)
          
                