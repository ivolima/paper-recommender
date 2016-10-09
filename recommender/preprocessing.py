# -*- coding: utf-8 -*-

# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import string


def remove_punctuation(text):
    """
    Remove punctuation from input string

    Parameters:
    -----------
    text : input unicode str

    Returns:
    --------
    processed_text : unicode str after punctuation removal

    """

    return unicode(filter(lambda x: x in string.punctuation, text))


def remove_numbers(text):
    """
    Remove digits from the input string

    Parameters:
    -----------
    text : input unicode str

    Returns:
    --------
    processed_text : unicode str after digits removal

    """

    return unicode(filter(lambda x: x not in '1234567890', text))


def remove_nonprintable_chars(text):
    """
    Remove non printable characters from input string

    Parameters:
    -----------
    text : input unicode str

    Returns:
    processed_text : unicode str after nonprintable chars removal

    """

    return unicode(filter(lambda x: x in string.printable, text))

