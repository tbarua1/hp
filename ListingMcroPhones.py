import speech_recognition as sr
#sudo apt-get install python-pyaudio python3-pyaudio
#import pyaudio
r = sr.Recognizer()
mic = sr.Microphone()
harvard=sr.Microphone.list_microphone_names()
#harvard = sr.AudioFile('audio.wav')
for source in harvard:
    print(source)