import webbrowser
webbrowser.open("final.wav")

import pyglet
song = pyglet.media.load('final.wav')
song.play()
pyglet.app.run()