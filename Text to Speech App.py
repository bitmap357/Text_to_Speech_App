from gtts import gTTS
import os
from tkinter import *

root = Tk()

def text_speech():
    text = entry.get()
    lang = 'en'
    output = gTTS(text=text, lang=lang, slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')


canvas = Canvas(root, width=400, height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text='Start', command=text_speech)
canvas.create_window(200, 230, window=button)


root.mainloop()
