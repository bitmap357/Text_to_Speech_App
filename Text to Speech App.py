from gtts import gTTS
import os
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200, 180, window=entry)


root.mainloop()
