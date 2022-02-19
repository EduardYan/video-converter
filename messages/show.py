"""
Some functions for use
in case show messages
"""


from models.message import Message


def show_message(title:str, message:str, type:str) -> None:
    """
    Show a message
    with the title
    and message passed
    for parameter.


    Parameter type is required
    to show the message
    """

    # creating a message to show
    message = Message(title, message, type)
    message.show()
