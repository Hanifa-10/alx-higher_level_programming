#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """indentate text supplied with

    Arguments:
    text {[str]} -- text/string to be indented

    Raises:
    TypeError: text must be a string"
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    new_str = "".join([x if x not in".?:" else x + "\n\n" for x in text])
    print("\n".join([x.strip() for x in new_str.split("\n")]), end="")
