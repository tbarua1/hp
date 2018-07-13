import speech_recognition as sr
#import SpeechRecognition as sr
print(sr.__version__)
r = sr.Recognizer()
# r.recognize_google()
#harvard = sr.AudioFile('song.webm')
harvard = sr.AudioFile('audio.wav')
with harvard as source:
    audio = r.record(source)
    print(type(audio))
    print(r.recognize_google(audio,language='hi-HI'))
    print(r.recognize_google(audio))