# generating packages
from tkinter import *
from pygame import mixer
import os
from ttkbootstrap import Style
from tkinter import ttk

# setting up the window
root=Tk()
root.title('Blueplayer')
style = Style(theme='morph')
root.geometry("520x320")
root.resizable(width=False, height=False)

# defining the buttons
def play():
    currentsong=playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def restart():
    mixer.music.rewind()


mixer.init()

# Printing the list of songs
playlist = Listbox(root, selectmode=SINGLE, font=('ubuntu', 20), width=35)
playlist.grid(columnspan=9)


os.chdir = os.chdir(r"/Users/darcyluke/Desktop/MusicPlayer")
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

# Printing the Buttons
breaklabel = ttk.Label(root, text="")
breaklabel.grid(row=1, column=1)

playbtn = ttk.Button(root, text="Play", command=play, bootstyle="Primary")
playbtn.grid(row=2, column=4)

pausebtn = ttk.Button(root, text="Pause", command=pause, bootstyle="Danger")
pausebtn.grid(row=2, column=5)

Resumebtn = ttk.Button(root, text="Resume", command=resume, bootstyle="Success")
Resumebtn.grid(row=2, column=6)

stopbtn = ttk.Button(root, text="Stop", command=stop, bootstyle="Warning")
stopbtn.grid(row=2, column=7)

restartbtn = ttk.Button(root, text="Restart", command=restart, bootstyle="Info")
restartbtn.grid(row=2, column=8)

#Defining the volume slider and printing
def volume(e):
    mixer.music.set_volume(volume.get())


volume = ttk.Scale(root, bootstyle="Secondary",
                   length=150,
                   orient="vertical",
                   from_=1, to=0,
                   command=volume,)
volume.grid(row=0, column=12)

#Printing the volume slider info
volumepad = ttk.Label(root, text="")
volumepad.grid(row=1, column=10)
volumepad2 = ttk.Label(root, text="")
volumepad2.grid(row=1, column=11)
volumeinfo = ttk.Label(root, text="Volume", font=('Arial', 13, "bold"))
volumeinfo.grid(row=0, column=12)

mainloop()
