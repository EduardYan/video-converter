"""
Some utils functions
to use for the application.
"""

from json import load


# path to config path
CONFIG_FILE_PATH = './config.json'


def get_config_object():
    """
    Return a object
    with the configuration from file
    'config.json'
    """

    # loading
    OBJECT = load(open(CONFIG_FILE_PATH))

    return OBJECT


def validate_config_object(object):
    """
    Validate the object of configuration
    passed for parameter.

    Execption is lauch if the config object
    passed not is valid.

    """

    # set the keys allowed here
    keys_allowed = ['NAME']

    if not keys_allowed[0] in object:
        raise TypeError(f'The file of configuration {CONFIG_FILE_PATH} not is valid.')


# configuration to use in files
CONFIG = get_config_object()

# validating the config object
validate_config_object(CONFIG)