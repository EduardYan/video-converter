#!/usr/bin/env python3

"""
Principal file for execute
the program.

Video Converter, a application
for convert to video
to audio.

"""


from models.ui import UI
from tkinter import Tk


if __name__ == '__main__':
    # creating a ui object for app
    root = Tk()
    ui = UI(root)
    ui.create()
    root.mainloop()