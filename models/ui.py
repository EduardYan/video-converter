"""
This file have
the model to create
interface for the program.
"""


from tkinter import (
    Tk,
    Label,
    Frame,
    Entry,
    Button,
    StringVar,
    Menu
)
from tkinter.filedialog import askopenfilename, asksaveasfilename
from moviepy.editor import VideoFileClip
from utils.config import CONFIG
from utils.video import validate_file_extension, get_extension
from utils.reset import clear_entry
from errors.path import InvalidPath
from messages.ask import ask_if_quit
from messages.show import show_message
from data.about import ABOUT_MESSAGE, CONTACT_MESSAGE
from os import environ


# getting values to config
NAME = CONFIG['NAME']


class UI:
    """
    Create a interface
    """

    def __init__(self, window:Tk) -> None:
        # background to use
        self.background = '#335533'

        self.wind = window
        self.wind.title(NAME)
        self.wind.resizable(False, False) # no resizable
        self.wind.config(background = self.background)


    def create(self) -> None:
        """
        Create all the interface
        for the program.
        """

        bar_menu = Menu(self.wind, background = '#aaa')
        file_menu = Menu(bar_menu, tearoff = 0, background = '#aaa', activebackground = '#bbb')
        file_menu.add_command(label = 'Convert', command = self.convert_to_audio)
        # file_menu.add_separator() # not use yet
        file_menu.add_command(label = 'Quit', command = lambda: ask_if_quit(self.wind, NAME))

        help_menu = Menu(bar_menu, tearoff = 0, background = '#aaa', activebackground = '#bbb')
        help_menu.add_command(label = 'About', command = lambda: show_message(NAME, ABOUT_MESSAGE, type = 'i'))
        help_menu.add_command(label = 'Contact', command = lambda: show_message(NAME, CONTACT_MESSAGE, type = 'i'))

        bar_menu.add_cascade(label = 'File', menu = file_menu)
        bar_menu.add_cascade(label = 'Help', menu = help_menu)

        # config for the menu
        self.wind.config(menu = bar_menu)

        # frames
        self.frame = Frame(self.wind)
        self.frame.config(background = self.background)
        self.frame.pack(side = 'left')
        self.frame_2 = Frame(self.wind)
        self.frame_2.config(background = self.background)
        self.frame_2.pack(side = 'right')

        # title
        self.title = Label(self.frame, text = NAME)
        self.title.config(background = self.background, foreground = '#fff')
        self.title.grid(row = 0, column = 0, sticky = 'news', pady = 5, padx = 3)


        self.message = Label(self.frame, text = 'Browser the file to convert.')
        self.message.config(background = self.background, foreground = '#fff')
        self.message.grid(row = 1, column = 0, pady = 11)


        # browser button
        self.button = Button(self.frame, text = 'Browser')
        self.button['command'] = lambda: self.browse_file()
        self.button.config(
            background = '#44a',
            cursor = 'hand2',
            activebackground = '#44c',
            width = '10'
        )

        self.button.grid(row = 2, column = 0, pady = 6)

        path_message = Label(self.frame_2, text = 'File Choice.')
        path_message.config(background = self.background, foreground = '#fff')
        path_message.grid(row = 0, column = 1, pady = 1)

        self.var = StringVar()
        self.path = Entry(self.frame_2)
        self.path.config(
            textvariable = self.var,
            selectbackground = '#88bb88',
            state = 'readonly',
        )

        self.path.grid(row = 1, column = 1, pady = 14, padx = 30, ipady = 1, ipadx = 1)

        # convert button
        convert_button = Button(self.frame_2, text = 'Convert')
        convert_button['command'] = lambda: self.convert_to_audio()
        convert_button.config(
            background = '#44a',
            cursor = 'hand2',
            activebackground = '#44c',
            width = '10'
        )
        convert_button.grid(row = 2, column = 1)


    def show_file_path(self, path:str) -> None:
        """
        Show the path of the file
        in a label items.


        Recived the path to show.
        """

        # Validating the path if not is string
        if type(path) not in [str]:
            raise InvalidPath('The path for set to the input. Not is valid, must be a string.')

        self.var.set(str(path))


    def get_path_video(self) -> str:
        """
        Return the path of the entry.
        """

        path = str(self.var.get())

        return path


    def save(self):
        """
        Save the file
        to audio mp3 format.
        """

        # getting the path to open
        path_video_mp4 = self.get_path_video()
        video_mp4 = VideoFileClip(path_video_mp4)
        audio_mp3 = video_mp4.audio

        path_to_save = asksaveasfilename() # where to save

        try:
            # writing
            audio_mp3.write_audiofile(path_to_save)

            video_mp4.close()
            audio_mp3.close()

            # showing message
            show_message(NAME, 'File Converted and Saved sucessfully.', type = 'i')

        except:
            show_message(NAME, 'Some error to save the audio.', type = 'e')


    def convert_to_audio(self):
        """
        Convert a file mp4 passed
        for parameter to a audio
        file. The extension for the
        mp4 file must be '.mp4'
        """

        # getting the path for the video
        path_video_mp4 = self.get_path_video()

        try:
            extension = get_extension(path_video_mp4)

            if validate_file_extension(extension):
                # from asyncio import run
                # run(self.save())
                self.save()

            else:
                show_message(NAME, 'The extenstion for convert the file not is valid. Must be .mp4', type = 'e')

            # cleaning
            clear_entry(self.path)

        except IndexError:
            # in case nothing in selection
            show_message(NAME, 'Please, select a file to convert.', type = 'e')


    def browse_file(self) -> None:
        """
        Browse the file
        for get the video,
        finnally show in the Entry
        widget.
        """

        # directory for get in browser
        VIDEOS_DIR = environ['XDG_VIDEOS_DIR']

        # getting the path
        path = askopenfilename(
            initialdir = VIDEOS_DIR,
            # only mp4
            filetypes = (
                ('Videos mp4', '*.mp4'),
                ('All', '*.*')
            )
        )

        try:
            # showing in entry
            self.show_file_path(path)

        except InvalidPath:
            show_message(NAME, 'Please, select a file to convert.', type = 'e')
