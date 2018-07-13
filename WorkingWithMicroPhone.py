import speech_recognition as sr
#import pyaudio
r = sr.Recognizer()
mic = sr.Microphone()
harvard=sr.Microphone.list_microphone_names()
#harvard = sr.AudioFile('audio.wav')
with harvard as source:
    audio = r.record(source)
    print(type(audio))
    print(r.recognize_google(audio,language='hi-HI'))
    print(r.recognize_google(audio))