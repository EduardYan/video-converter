"""
Model for a error.
"""


class Error:
    """
    Model for a error.

    With properties:
        title
        message
    """

    def __init__(self, title:str, message:str) -> None:
        self.title = title
        self.message = message
