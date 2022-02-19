"""
Some utils functions
to use for the application.
"""

from json import load


def get_config_object():
    """
    Return a object
    with the configuration from file
    'config.json'
    """

    # loading
    OBJECT = load(open('config.json'))

    return OBJECT
