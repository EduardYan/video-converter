"""
This module have
some functions
to use for convert the video
to audio.
"""


from errors.path import InvalidPath


def get_extension(path:str) -> str:
    """
    Return a string with the extension
    of the file in the path passed for parameter.
    """

    if type(path) not in [str]:
        InvalidPath('The path passed for parameter not is valid. Verify the path.')

    # split with "."
    parts = path.split('.')
    last = parts[1]

    return last


def validate_file_extension(extension:str) -> None:
    """
    Validate the file extension passed for
    parameter.
    """

    # only .mp4 allowed
    if not extension == 'mp4':
        return False

    return True
