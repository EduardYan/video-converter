"""
Model for a message.
"""


from tkinter.messagebox import showerror, showinfo, showwarning, askquestion


class MessageTypeInvalid(TypeError):
    """
    Class in case the type for make
    a message is invalid.
    """
    pass


class Message:
    """
    Create a message

    With properties:
        title
        content

    """

    # options for validate the type
    TYPE_OPTIONS = ['i', 'w', 'e', 'a']

    def __init__(self, title:str, content:str, type:str) -> None:
        if type not in self.TYPE_OPTIONS:
            raise MessageTypeInvalid(f'The type for create a message is invalid availables are {self.TYPE_OPTIONS}')

        # values to show
        self.title = title
        self.content = content
        self.type = type

    def show(self):
        """
        Show a window
        with the title
        passed in the constructor
        and the content.
        """

        # validating to show
        if self.type == 'i':
            showinfo(self.title, self.content)

        elif self.type == 'w':
            showwarning(self.title, self.content)

        elif self.type == 'e':
            showerror(self.title, self.content)

        elif self.type == 'a':
            return askquestion(self.title, self.content)
