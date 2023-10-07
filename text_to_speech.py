import pyttsx3

text = input("Text to be spoken: ")

engine = pyttsx3.init()
engine.say(text)

engine.runAndWait()