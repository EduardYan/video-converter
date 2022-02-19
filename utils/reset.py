"""
Utils functions to use
for reset or clean the
interface.
"""

from tkinter import Entry, END


class WidgetInvalid(TypeError):
    """
    Error in case
    the widget passed
    for parameter nos is valid.
    """
    pass


def clear_entry(entry:Entry) -> None:
    """
    Clear the entry
    passed for parameter.
    """

    if type(entry) not in [Entry]:
        WidgetInvalid('The widget for clear not is valid.')

    entry.config(state = 'normal') # normal for writing
    entry.delete('0', END) # cleaning
    entry.config(state = 'readonly')
