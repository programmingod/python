import pyttsx3
engine = pyttsx3.init()

name = input("What is your name? ")
engine.say("Hi there", name)


text = input("Text to be spoken: ")

engine.say(text)

engine.runAndWait()