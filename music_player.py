from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("600x200")

mixer.init()
mixer.music.load("Soundbite.mp3")


def pause():
    mixer.music.pause()
def play():
    mixer.music.play()
def resume():
    mixer.music.unpause()


Label(root, text="Music Player").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=250, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Exit", command=quit).place(x=380, y=100)

root.mainloop()