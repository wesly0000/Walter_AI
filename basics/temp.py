# from pygame import mixer
import pygame





def SpeakEdge(data):
    
    def play_audio(audio_file):
        pygame.init()
        sound = pygame.mixer.Sound(audio_file)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))  # Convert seconds to milliseconds
        pygame.quit()

    command = f'edge-tts --voice "en-CA-LiamNeural" --pitch=-10Hz --rate=-5% --text "{data}" --write-media "temp/data.mp3" '
    os.system(command)
    audio_file = 'temp\data.mp3'
    play_audio(audio_file)


# SpeakEdge('hi i am assistant built by wesly, and currently, im just a dummy robot!')