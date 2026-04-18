"""
A module that adds numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""

def add_numbers(a, b):
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b


def repeat_text(text, times):
    """
    This function will repeat certain text as many
    times as the user requests.
    
    Parameters
    ----------
    
    text : str
        the text that will be repeated
    times: int
        the number of times the text will be repeated
        
    Returns
    --------
    string
        A string containing the text input by users
        repeated as many times as user requested.
        
    Examples
    --------
    >>> repeat_text("abc",3)
    abcabcabc
    >>> repeat_text("text",2)
    texttext
    """
    return text*times 