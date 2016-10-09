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


def remove_digits(text):
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
    --------
    processed_text : unicode str after nonprintable chars removal

    """

    return unicode(filter(lambda x: x in string.printable, text))


def sanitize(text, nonprintable=True, punctuation=True, digits=False):
    """
    It gets a text input and removes invalid symbols, punctuation and digits from it

    Parameters:
    -----------
    text : input unicode str

    Returns:
    --------
    processed_text : unicode str after sanitization process

    """
    if nonprintable:
        text = remove_nonprintable_chars(text)
    if punctuation:
        text = remove_punctuation(text)
    if digits:
        text = remove_digits(text)

    return unicode(text)

