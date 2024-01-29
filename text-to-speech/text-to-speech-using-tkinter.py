
from gtts import gTTS
import os

from tkinter import *

root=Tk()

canvas=Canvas(root,width=400,height=400)
canvas.pack()

def tts():
    text=entry.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save("tkinker_file_output.mp3")
    os.system('afplay tkinker_file_output.mp3')

entry=Entry(root)
canvas.create_window(230,280,window=entry)

button=Button(root,text="Start",command=tts)

canvas.create_window(210,330,window=button)
root.mainloop()
