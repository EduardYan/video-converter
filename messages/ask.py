"""
This module have
functions to use for ask.

"""


from tkinter.messagebox import askquestion
from tkinter import Tk
from models.message import Message


def ask_if_quit(window:Tk, title:str) -> None:
    """
    Ask for quit of the program
    with a window.


    window parameter is required
    for destroy it.
    """

    # creating a message
    message = Message(title, 'You want quit?', type = 'a')
    if message.show() == 'yes':
        window.destroy() # destroy
