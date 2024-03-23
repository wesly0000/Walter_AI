import struct
import pyaudio
import pvporcupine
from basics import path


wakeword = path.wakeWord

porcupine=None
paud=None
audio_stream=None


def hotword():
    global porcupine, paud, audio_stream 
    try:
        print('waiting for the Hotword: ')

        access_key="v2FFktZVM4EhJNO+57W4PcsVPEllq+iAv3rtKP7Bi7ujHO5doLRxSw==" #to create access key signup to https://console.picovoice.ai/ 
        #new version of pvporcupine has a limitation--> you can use only in upto 3 devices in free version. 
        #you can install older version of pvporcupine --> pip install pvporcupine==1.9.5 , which does not require any access key
        #if you are using older version of pvporcupine, replace the below line with--> porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        print(wakeword)
        porcupine=pvporcupine.create(access_key=access_key,keyword_paths=[wakeword]) #pvporcupine.KEYWORDS for all keywords
        # porcupine=pvporcupine.create(keywords=["jarvis"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("HOTWORD DETECTED! \nAsk me to do anything for you!\n\n")
                break

    except Exception as e:  # Catch specific exceptions for better error handling
        print('hotword malfunctioned:', e)         
    

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

