from gtts import gTTS
import os
from tkinter import *

root = Tk()

def text_speech():
    text = entry.get()
    lang = 'en'
    output = gTTS(text=text, lang=lang, slow=False)



canvas = Canvas(root, width=400, height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text='Start', command=lambda: )
canvas.create_window(200, 230, window=button)


root.mainloop()
